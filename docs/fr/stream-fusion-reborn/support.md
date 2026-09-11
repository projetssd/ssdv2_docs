# Support et développement

Besoin d'aide, vous avez trouvé un bug, ou vous voulez contribuer ? Voici les ressources disponibles.

---

## Communauté et support

### Discord

Le serveur Discord est le point de contact principal pour :

- **Support d'installation** : aide au déploiement et à la configuration
- **Signalement de bugs** : remontez les problèmes rencontrés
- **Discussion** : échanges avec les développeurs et la communauté
- **Contribution** : participez au développement du projet

[:fontawesome-brands-discord: Rejoindre le serveur Discord](https://discord.gg/r3Nw4GAkJG){ .md-button .md-button--primary }

---

## Signaler un problème

Si vous rencontrez un bug ou un comportement inattendu :

1. **Vérifiez les logs** : `docker compose logs -f stream-fusion`
2. **Consultez le health check** : `curl http://localhost:8080/api/monitoring/health`
3. **Rejoignez le Discord** pour en discuter avec les développeurs

---

## Participer au développement

Le dépôt est privé, mais toute personne souhaitant contribuer est la bienvenue ! Rejoignez le [serveur Discord](https://discord.gg/87RV5DStEK) pour vous présenter et obtenir l'accès au dépôt.

Les contributions peuvent prendre plusieurs formes :

- **Documentation** : corrections, traductions, nouvelles pages
- **Bug fixes** : corrections de problèmes identifiés
- **Fonctionnalités** : nouvelles idées et implémentations
- **Tests** : retours sur les nouvelles versions
- **Indexeurs** : ajout de nouveaux indexeurs francophones

---

## Guide: Ajouter un indexeur privé

L'ajout d'un nouvel indexeur privé (tracker Torznab) nécessite de toucher environ **14 fichiers** dans la codebase. Cette section détaille la checklist complète.

### Pattern 3 fichiers

Chaque indexeur privé suit un pattern dans `indexers/private/{nom}/` :

| Fichier | Rôle | Règles obligatoires |
|---|---|---|
| `{nom}_api.py` | Client HTTP bas niveau | Retourne `List[{Name}RawResult]`. Strippe les credentials du `torrent_download`. `privacy = "private"` toujours. |
| `{nom}_result.py` | Modèle de résultat | `from_api_item(raw, media) → self`. `convert_to_torrent_item() → TorrentItem`. Display name fixé comme `"{Name} - API"`. |
| `{nom}_service.py` | Orchestrateur | `search(media) → List[Result]`. Résolution des credentials : `unique_account → server-side key`, sinon `user config → server default`. |

### Checklist des fichiers à modifier

1. **`settings.py`** — Ajouter dans le bloc `SERVER-SIDE INDEXER ENABLE FLAGS` : `{name}_enable: bool = True`. Ajouter un bloc dédié avec `{name}_url`, `{name}_api_key`, `{name}_passkey` (si announce URL), `{name}_unique_account`.

2. **`services/settings/settings_registry.py`** — Ajouter `SettingDef("{name}_enable", "bool", "Activer {Name}", "indexers", ...)` après le dernier indexeur.

3. **`indexers/__init__.py`** — La checklist complète est documentée en commentaire dans ce fichier (lignes 22-121). Consultez-la pour la référence exhaustive.

4. **`utils/infrastructure/config/parse_config.py`** — `DEFAULT_INDEXER_CATEGORIES` : `"{name}": "fallback_private"` (ou `priority_private` / `intermediary_private`).

5. **`utils/torrent/torrent_item.py`** — `_PRIVATE_CREDENTIAL_INDEXERS` : ajouter `"{Name} - API"`. `_TORBOX_PREFERRED_INDEXERS` : ajouter `"{Name} - API"`. `to_debrid_stream_query()` : ajouter bloc `elif` pour reconstruire les credentials.

6. **`web/root/search/views.py`** — Importer le service. Ajouter dans `_POSTGRES_INDEXERS`, `_INDEXER_CONFIG_KEY`, les fonctions `_fetch_{name}()` (movie + series), et `ALL_FETCHERS`.

7. **`tasks/search_tasks.py`** — Importer le service. Ajouter `_fetch_{name}()` dans `background_db_refresh` et `prefetch_next_episode`. Ajouter dans `FETCHERS` / `ALL_FETCHERS`.

8. **`static/admin/config_indexers.html`** — Ajouter une ligne `<tr>` dans la table des indexeurs avec toggle + champ URL.

9. **`static/index.html`** — Ajouter une section indexeur avec :
    - Toggle avec `data-unique-account` et `onchange="updateProviderFields()"`
    - Ligne de catégorie avec `<select>`
    - Champs de credentials (conditionnes par `unique_account` dans le template Jinja2)
    - Bumper la version du cache JS : `config.js?v=N → config.js?v=N+1`

10. **`static/config.js`** — Ajouter dans : `handleUniqueAccounts()`, `updateProviderFields()`, `defaultConfig`, `restore/load`, `_defaultCats`, `serialization`, `validation`.

11. **`web/root/config/views.py`** — Ajouter dans le contexte du template : `"{name}_enable"`, `"{name}_unique_account"`.

12. **Templates d'administration** — Si l'indexeur nécessite une page de configuration admin, créer les templates Jinja2.

13. **Modèle PostgreSQL** — Si l'indexeur utilise une table dédiée, créer le modèle SQLAlchemy et la migration Alembic.

14. **`web/admin/`** — Ajouter les vues admin pour la gestion de l'indexeur (configuration, statistiques).

!!! tip "Indexeurs publics"
    Les indexeurs publics (`indexers/public/`) sont plus simples : seuls les fichiers API et service sont nécessaires. Pas de stockage PostgreSQL, pas d'intégration dans `views.py` ou `config.js`.

---

## Liens utiles

| Ressource | Lien |
|---|---|
| Image Docker | [laster13/stream-fusion-reborn](https://hub.docker.com/r/laster13/stream-fusion-reborn) |
| Discord | [https://discord.gg/87RV5DStEK](https://discord.gg/r3Nw4GAkJG) |
| TMDB API | [Obtenir une clé](https://developer.themoviedb.org/docs/getting-started) |
