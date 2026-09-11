# :material-cog: Configuration du peering

Guide pas-à-pas pour configurer le partage de cache entre deux instances Stream Fusion.

---

## :material-check-circle: Prérequis

- Deux instances Stream Fusion accessibles mutuellement via HTTP(S)
- `PEER_MASTER_KEY` configuré sur **les deux** instances
- `SECRET_API_KEY` sur chaque instance

---

## :material-numeric-1-circle: Étape 1 : Créer une PeerKey sur l'Instance A

Sur l'**Instance A** (celle qui partage son cache) :

=== ":material-monitor-dashboard: Interface admin"

    1. Allez sur `https://instance-a.example.com/admin/`
    2. Authentifiez-vous avec `SECRET_API_KEY`
    3. **Peer Keys** → **Créer une PeerKey**
    4. Nommez-la (ex: `Instance-B`)
    5. Configurez le rate limiting
    6. **Copiez immédiatement le `key_id` et le `secret`**

=== ":material-console: API"

    ```bash
    curl -X POST https://instance-a.example.com/admin/create-peer-key \
      -H "secret-key: VOTRE_SECRET_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"name": "Instance-B"}'
    ```

!!! danger "Secret à usage unique"
    Le secret n'est affiché **qu'une seule fois**. Si vous le perdez, il faudra révoquer la clé et en recréer une.

---

## :material-numeric-2-circle: Étape 2 : Créer une PeerInstance sur l'Instance B

Sur l'**Instance B** (celle qui importe le cache) :

1. Allez sur `https://instance-b.example.com/admin/`
2. **Peer Instances** → **Créer une PeerInstance**
3. Remplissez :

| Champ | Valeur |
|---|---|
| Nom | `Instance-A` (descriptif) |
| URL | `https://instance-a.example.com` |
| Key ID | Le `key_id` copié à l'étape 1 |
| Secret | Le `secret` copié à l'étape 1 |
| Actif | :fontawesome-solid-check: |
| Sync activé | :fontawesome-solid-check: |
| Cron | `0 */6 * * *` (toutes les 6h) |

4. Cliquez sur **Tester la connexion** pour vérifier

---

## :material-numeric-3-circle: Étape 3 : Persistance et planification automatique

La PeerInstance est persistée dans la table PostgreSQL `peer_instances` avec son schedule cron. Au démarrage du worker Taskiq, la fonction `seed_peer_schedules_from_db()` lit toutes les PeerInstances actives depuis PostgreSQL et enregistre automatiquement leurs schedules dans Redis.

Cela signifie que :

- :material-check: Les schedules survivent aux **redémarrages** sans reconfiguration via l'admin
- :material-check: Les modifications de cron prennent effet au **prochain démarrage du scheduler**
- :material-check: L'activation/désactivation (`sync_enabled`) est lue depuis PG à chaque exécution (effet immédiat)
- :material-check: Aucune variable d'environnement n'est nécessaire pour la persistance

Modifiez le cron depuis le panneau d'administration → **Peer Sync**, ou directement dans la base de données.

---

## :material-swap-horizontal: Étape 4 (optionnel) : Peering bidirectionnel

Pour que l'Instance A importe aussi le cache de B, répétez les étapes 1-2 en inversant les rôles :

1. Créez une PeerKey sur **B** pour **A**
2. Créez une PeerInstance sur **A** pointant vers **B**

```mermaid
graph LR
 A["Instance A"] -->|"Sync →"| B["Instance B"]
 B -->|"Sync →"| A
 
 style A fill:#311b92,color:#fff
 style B fill:#1b5e20,color:#fff
```

---

## :material-package-variant-closed: Transfert de dump (DuckDB / Meilisearch)

En complément de la sync incrémentale, Stream Fusion supporte le transfert de **snapshots complets** de bases DuckDB et Meilisearch entre pairs.

### Principe

Le transfert de dump permet à une instance de récupérer l'intégralité de la base DuckDB ou Meilisearch d'un pair, plutôt que de synchroniser uniquement le delta de torrents. C'est particulièrement utile pour :

- L'**initialisation** d'une nouvelle instance (pas besoin de rebuild DuckDB)
- La **réplication complète** de l'index Meilisearch d'un pair
- La **synchronisation** de la table `imdb_tmdb` (mappings IMDB↔TMDB)

### Flux

1. L'instance **source** crée périodiquement des dumps (tâche cron `db_dump_create`)
2. L'instance **cible** consulte les dumps disponibles via l'API peer
3. Un **token de téléchargement** est échangé (HMAC-SHA256 + Fernet)
4. Le dump est téléchargé et restauré via `db_dump_restore`

### Configuration

| Paramètre | Description |
|---|---|
| `db_dump_schedule_enabled` | Active la création automatique de dumps |
| `db_dump_cron` | Fréquence de création des dumps (défaut: `0 4 * * 0` pour DuckDB/Meilisearch) |
| `db_dump_create_pg_cron` | Fréquence de dump PostgreSQL (défaut: `0 3 * * *` quotidien) |

### Depuis l'admin

1. Allez sur `/admin/meta` → section **Dumps**
2. Cliquez sur **Peer Dumps** pour lister les dumps disponibles chez les pairs
3. Sélectionnez un dump et cliquez sur **Pull** pour lancer le transfert
4. La progression est visible en temps réel

Voir la page [Sauvegarde DuckDB](../cache/sauvegarde-duckdb.md) pour les détails techniques sur la création et la restauration des dumps.

---

## :material-monitor-dashboard: Monitoring

Depuis le panneau d'administration → **Peer Sync** :

- :material-play-circle: Démarrer une sync manuellement
- :material-stop-circle: Arrêter une sync en cours
- :material-delete-sweep: Purger les données importées d'un pair
- :material-text-box: Voir les logs de synchronisation

---

## :material-help-circle: Dépannage

??? question "La connexion échoue"
    - Vérifiez que les deux instances sont accessibles mutuellement
    - Vérifiez le firewall
    - Utilisez le bouton **Tester la connexion** dans l'admin

??? question "Erreurs 429 (rate limiting)"
    - Augmentez `rate_limit` et `rate_window` dans la PeerKey
    - Ou diminuez la fréquence du cron de sync

??? question "Données non indexées"
    - Vérifiez que Meilisearch fonctionne
    - Consultez les logs du Taskiq Worker