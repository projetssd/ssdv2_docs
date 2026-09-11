# Premier démarrage

Ce guide vous accompagne pour déployer Stream Fusion Reborn en quelques minutes avec Docker.

!!! info "Image Docker uniquement"
    L'image Docker officielle est disponible sur [Docker Hub](https://hub.docker.com/r/laster13/stream-fusion-reborn). Pour obtenir l'accès au dépôt privé et participer au développement, venez vous présenter sur le [serveur Discord](https://discord.gg/87RV5DStEK).

---

## Prérequis

- **Docker** >= 20.10
- **Docker Compose** >= 2.20 (plugin `docker compose`)
- Une **clé API TMDB** ([en obtenir une gratuitement](https://developer.themoviedb.org/docs/getting-started))

!!! tip "Services debrid"
    Les services debrid ne sont pas obligatoires au démarrage. Vous pouvez les configurer plus tard depuis la page de configuration du plugin. Si un service debrid est configuré au niveau serveur (via variables d'environnement), il sera utilisé pour tous les utilisateurs.

---

## Étapes d'installation

### 1. Créer le répertoire de déploiement

```bash
mkdir stream-fusion && cd stream-fusion
```

### 2. Créer le fichier `.env`

```bash
cat > .env << 'EOF'
SECRET_API_KEY=    # openssl rand -hex 32
ADMIN_SECRET_KEY= # openssl rand -hex 32 ; différente de SECRET_API_KEY
CONFIG_SECRET_KEY= # python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
TMDB_API_KEY=      # Votre clé TMDB

PG_PASS=  # obligatoire ; accès applicatif ; openssl rand -hex 32
PG_MIGRATION_PASS=  # obligatoire ; migrations ; openssl rand -hex 32
POSTGRES_PASSWORD=  # obligatoire ; bootstrap PostgreSQL ; openssl rand -hex 32

MEILI_MASTER_KEY=  # openssl rand -hex 32

TZ=Europe/Paris
USE_HTTPS=true
PROXY_URL=http://warp:1080
EOF
```

Les variables **SECRET_API_KEY**, **CONFIG_SECRET_KEY**, **TMDB_API_KEY** et **MEILI_MASTER_KEY** sont obligatoires. Voir la page [Environnement](../installation/environnement.md) pour les commandes de génération de clés.

### 2b. (Optionnel) Activer un compte debrid ou indexeur partagé

Si vous souhaitez qu'un compte debrid ou une clé d'indexeur soit accessible à tous les utilisateurs de l'instance :

```bash
nano user.env  # utiliser le template de la page Environnement, décommenter les tokens souhaités
```

Puis décommenter les lignes `env_file: user.env` dans `docker-compose.yml` sur les services `stream-fusion` et `taskiq-worker`. Voir [Fichiers d'environnement](../installation/environnement.md#fichier-userenv-mode-unique_account) pour les détails.

### 3. Créer le `docker-compose.yml`

Choisissez votre configuration :

=== "Instance unique (recommandé pour débuter)"

    Voir la page [docker-compose simple](../installation/docker-compose-simple.md) pour le fichier complet.

=== "Production scalable"

    Voir la page [docker-compose production](../installation/docker-compose-prod.md) pour le fichier complet.

### 4. Lancer l'application

```bash
docker compose up -d
```

### 5. Vérifier l'installation

```bash
curl http://localhost:8080/api/monitoring/health
docker compose logs -f stream-fusion
```

### 6. Accéder aux interfaces

| URL | Description |
|---|---|
| `http://localhost:8080/` | Page de configuration du plugin Stremio |
| `http://localhost:8080/admin/` | Panneau d'administration |
| `http://localhost:8080/api/monitoring/health` | Health check |

Si vous utilisez un domaine avec HTTPS (ex: `sf.example.com`), l'interface d'administration est accessible à `https://sf.example.com/admin/`.

---

## Créer une clé API

=== "Via le panneau d'administration"

    1. Allez sur `https://votre-domaine.tld/admin/` (ou `http://localhost:8080/admin/`)
    2. Authentifiez-vous avec votre `SECRET_API_KEY`
    3. Allez dans l'onglet **Sécurité** puis **Clés API**
    4. Créez une nouvelle clé avec les options suivantes :
        - **Nom d'utilisateur** : identifiant optionnel
        - **Durée de validité** : date d'expiration optionnelle
        - **Proxyfication des flux** : activer/désactiver pour cette clé
        - **Permissions** : mettre en pause la clé à tout moment

=== "Via l'API"

    ```bash
    curl -X POST http://localhost:8080/api/auth/new \
      -H "secret-key: votre-secret-api-key" \
      -H "Content-Type: application/json" \
      -d '{"name": "ma-cle-stremio"}'
    ```

### Inscription publique

Vous pouvez activer l'inscription publique via le panneau d'administration ou la variable d'environnement `ALLOW_PUBLIC_KEY_REGISTRATION=True`. Dans ce cas, depuis la page de configuration du plugin Stremio, les utilisateurs pourront créer leur propre clé API automatiquement.

!!! warning "Instance publique"
    L'inscription publique est destinée aux instances ouvertes. Pour une instance privée, préférez créer les clés manuellement via le panneau d'administration.

---

## Configurer Stremio

Voir le guide détaillé : [Configuration Stremio](configuration-stremio.md).

---

## Prochaines étapes

<div class="grid cards" markdown>

-   :material-tune: **[Configuration complète](../configuration/variables-environnement.md)**

    Toutes les ~90 variables d'environnement détaillées

-   :material-share-variant: **[Peering](../peering/index.md)**

    Partager le cache entre plusieurs instances

-   :material-shield-lock: **[Sécurité](../securite.md)**

    Modèle de sécurité complet
