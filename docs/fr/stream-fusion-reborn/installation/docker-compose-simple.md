# Déploiement instance unique

Configuration pour un déploiement mono-instance, sans PgBouncer. Le Compose utilise le réseau Docker externe `traefik_proxy` pour raccorder Stream Fusion Reborn au reverse proxy. Cette configuration est adaptée à un usage personnel ou à un petit groupe.

!!! tip "Pour commencer"
    C'est la configuration recommandée pour un premier déploiement. Passez à la [configuration scalable](docker-compose-prod.md) uniquement si vous avez besoin de haute disponibilité.

---

## Lancement

```bash
# 1. Créer le répertoire
mkdir stream-fusion && cd stream-fusion

# 2. Créer le .env (voir la page Environnement pour le template complet)
nano .env

# 3. (Optionnel) Créer user.env pour le mode unique_account (debrid/indexeurs partagés)
# nano user.env

# 4. Créer le docker-compose.yml (copier le contenu ci-dessous)
nano docker-compose.yml

# 5. Lancer
docker compose up -d

# 6. Suivre les logs
docker compose logs -f stream-fusion
```

---

## Accès aux services

| Service | URL |
|---|---|
| Application | Via le domaine configuré sur votre reverse proxy |
| Admin | `https://votre-domaine/admin/` |
| PostgreSQL | `localhost:5432` (non exposé par défaut) |
| Redis | `localhost:6379` (non exposé par défaut) |

!!! warning "Exposition réseau"
    Le Compose ne publie pas directement le port `8080` sur l'hôte. Le service `stream-fusion` est accessible via le réseau Docker externe `traefik_proxy`. PostgreSQL, Redis et Meilisearch ne doivent pas être exposés publiquement.

---

## Préparer le fichier `.env`

Avant de démarrer la stack, créez un fichier `.env` à côté du
`docker-compose.yml`.

Les valeurs utilisateur sont :

- `ADMIN_SECRET_KEY` : clé d'accès à l'interface d'administration ;
- `TMDB_API_KEY` : clé API TMDB.

Les autres valeurs sont des secrets internes et doivent être générées
indépendamment.

!!! danger "Secrets PostgreSQL"
    `POSTGRES_PASSWORD`, `PG_PASS` et `PG_MIGRATION_PASS` doivent être
    **trois secrets différents**, composés chacun de **64 caractères
    hexadécimaux**.

### Générer un secret

La commande suivante génère une valeur hexadécimale aléatoire de
64 caractères :

```bash
openssl rand -hex 32
```

### Générer tous les secrets internes

Vous pouvez générer toutes les valeurs nécessaires en une seule fois :

```bash
for name in \
  SECRET_API_KEY \
  CONFIG_SECRET_KEY \
  SESSION_KEY \
  PEER_MASTER_KEY \
  POSTGRES_PASSWORD \
  PG_PASS \
  PG_MIGRATION_PASS
do
  printf '%s=' "$name"
  openssl rand -hex 32
done
```

!!! warning "Ne réutilisez pas la même valeur"
    Chaque secret doit recevoir sa propre valeur aléatoire.
    En particulier, `POSTGRES_PASSWORD`, `PG_PASS` et
    `PG_MIGRATION_PASS` doivent obligatoirement être différents.

### Exemple complet de `.env`

Créez le fichier :

```bash
nano .env
```

Puis utilisez le modèle suivant en remplaçant les valeurs d'exemple :

```dotenv
# =============================================================================
# Stream Fusion Reborn — Environment Configuration
# =============================================================================
#
# ADMIN_SECRET_KEY = clé choisie par l'utilisateur pour l'interface admin.
# Les autres secrets internes doivent être générés séparément.
#
# Génération d'un secret interne :
#   openssl rand -hex 32
#
# IMPORTANT :
# POSTGRES_PASSWORD, PG_PASS et PG_MIGRATION_PASS doivent être des valeurs
# hexadécimales de 64 caractères et toutes différentes.
# =============================================================================

# ── Valeurs utilisateur ────────────────────────────────────────────────────────

ADMIN_SECRET_KEY=replace-with-your-admin-key-at-least-32-characters
TMDB_API_KEY=replace-with-your-tmdb-api-key


# ── Secrets internes ──────────────────────────────────────────────────────────

SECRET_API_KEY=RANDOM_64_HEX
CONFIG_SECRET_KEY=RANDOM_64_HEX
SESSION_KEY=RANDOM_64_HEX
PEER_MASTER_KEY=RANDOM_64_HEX
MEILI_MASTER_KEY=RANDOM_64_HEX


# ── PostgreSQL ────────────────────────────────────────────────────────────────

POSTGRES_PASSWORD=RANDOM_64_HEX
PG_PASS=RANDOM_64_HEX
PG_MIGRATION_PASS=RANDOM_64_HEX


# ── Déploiement ───────────────────────────────────────────────────────────────

TZ=Europe/Paris
USE_HTTPS=true
PROXY_URL=http://warp:1080
```

!!! info "PG_RESTORE_PASS"
    Aucun `PG_RESTORE_PASS` n'est à définir dans `.env`.

    Le Compose génère automatiquement un quatrième secret PostgreSQL,
    dédié à la restauration, dans le volume Docker
    `pg-restore-secret`.

    Ce secret est ensuite utilisé par le rôle
    `streamfusion_restore`.

---

## Docker Compose complet

Le fichier ci-dessous correspond au fichier
`deploy/docker-compose.yml` utilisé actuellement par Stream Fusion
Reborn.

!!! info "Source de référence"
    Lors des futures mises à jour de Stream Fusion Reborn, le fichier
    `deploy/docker-compose.yml` présent dans le dépôt reste la source
    de référence.

### Réseau Docker requis

Le Compose utilise un réseau Docker externe nommé `traefik_proxy`.

Vérifiez d'abord s'il existe :

```bash
docker network inspect traefik_proxy
```

S'il n'existe pas encore, créez-le :

```bash
docker network create traefik_proxy
```

!!! warning "Reverse proxy"
    Le service `stream-fusion` utilise `expose: 8080` et non un
    mapping `ports:` vers l'hôte.

    Le reverse proxy doit donc être connecté au réseau Docker
    `traefik_proxy` pour joindre l'application.

### `docker-compose.yml`

Copiez le contenu suivant dans votre fichier `docker-compose.yml` :

```yaml
---
---
networks:
  proxy_network:
    external: true

services:

  pg-restore-secret-init:
    image: postgres:17-alpine
    command:
      - /bin/sh
      - -ec
      - |
        umask 077
        secret=/run/pg-restore-secret/pg_restore_pass
        tmp="$${secret}.tmp"

        if [ ! -s "$$secret" ]; then
          rm -f "$$tmp"
          od -An -N32 -tx1 /dev/urandom | tr -d ' \n' > "$$tmp"
          test "$$(wc -c < "$$tmp")" -eq 64
          chmod 0444 "$$tmp"
          mv "$$tmp" "$$secret"
        fi

        test "$$(wc -c < "$$secret")" -eq 64
        chmod 0444 "$$secret"
    volumes:
      - pg-restore-secret:/run/pg-restore-secret
    network_mode: none
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    read_only: true
    restart: "no"

  taskiq-worker:
    image: ghcr.io/laster13/stream-fusion-reborn:latest
    container_name: taskiq-worker
    command: python -m taskiq worker stream_fusion.worker:broker
    # env_file: user.env        # uncomment to enable unique_account mode (debrid/indexers)
    environment:
      SECRET_API_KEY: ${SECRET_API_KEY:?Provide SECRET_API_KEY}
      CONFIG_SECRET_KEY: ${CONFIG_SECRET_KEY:?Provide CONFIG_SECRET_KEY}
      PEER_MASTER_KEY: ${PEER_MASTER_KEY:-}
      TMDB_API_KEY: ${TMDB_API_KEY:?Provide TMDB_API_KEY}
      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_BASE: streamfusion
      PG_RESTORE_USER: streamfusion_restore
      PG_RESTORE_PASS_FILE: /run/pg-restore-secret/pg_restore_pass
      PG_OWNER_ROLE: streamfusion_owner
      TZ: ${TZ}
      PROXY_URL: ${PROXY_URL}
      # Service-to-service wiring — not configurable by the user
      REDIS_HOST: stremio-redis
      PG_HOST: stremio-postgres
      TASKIQ_REDIS_DB: "6"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp:mode=1777,size=4g
      - /home/appuser:uid=1000,gid=1000,mode=0700
    volumes:
      - dmm-hashlists:/data/dmm_hashlists
      - imdb-db:/data/imdb_db
      - sfr-db-backups:/data/backups
      - pg-restore-secret:/run/pg-restore-secret:ro
      - taskiq-logs:/app/config/logs
    depends_on:
      pg-restore-secret-init:
        condition: service_completed_successfully
      stremio-postgres:
        condition: service_healthy
      stremio-redis:
        condition: service_started
    restart: unless-stopped
    networks:
      - proxy_network

  taskiq-scheduler:
    image: ghcr.io/laster13/stream-fusion-reborn:latest
    container_name: taskiq-scheduler
    command: python -m taskiq scheduler stream_fusion.tkq:scheduler
    environment:
      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_BASE: streamfusion
      TZ: ${TZ}
      # Service-to-service wiring — not configurable by the user
      REDIS_HOST: stremio-redis
      PG_HOST: stremio-postgres
      TASKIQ_REDIS_DB: "6"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp:mode=1777
      - /home/appuser:uid=1000,gid=1000,mode=0700
    volumes:
      - taskiq-logs:/app/config/logs
    depends_on:
      stremio-postgres:
        condition: service_healthy
      stremio-redis:
        condition: service_started
    restart: unless-stopped
    networks:
      - proxy_network
    # IMPORTANT: replicas must always be 1

  stream-fusion:
    image: ghcr.io/laster13/stream-fusion-reborn:latest
    container_name: stream-fusion
    # env_file: user.env        # uncomment to enable unique_account mode (debrid/indexers)
    environment:
      # Container-specific flag
      RUN_MIGRATIONS: "true"
      SECRET_API_KEY: ${SECRET_API_KEY:?Provide SECRET_API_KEY}
      ADMIN_SECRET_KEY: ${ADMIN_SECRET_KEY:?Provide ADMIN_SECRET_KEY}
      CONFIG_SECRET_KEY: ${CONFIG_SECRET_KEY:?Provide CONFIG_SECRET_KEY}
      PEER_MASTER_KEY: ${PEER_MASTER_KEY:-}
      TMDB_API_KEY: ${TMDB_API_KEY:?Provide TMDB_API_KEY}
      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_BASE: streamfusion
      PG_MIGRATION_USER: streamfusion_migration
      PG_MIGRATION_PASS: ${PG_MIGRATION_PASS:?PG_MIGRATION_PASS is required}
      PG_OWNER_ROLE: streamfusion_owner
      TZ: ${TZ}
      USE_HTTPS: ${USE_HTTPS}
      PROXY_URL: ${PROXY_URL}
      # Service-to-service wiring — not configurable by the user
      REDIS_HOST: stremio-redis
      PG_HOST: stremio-postgres
      TASKIQ_REDIS_DB: "6"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp:mode=1777
      - /home/appuser:uid=1000,gid=1000,mode=0700
    expose:
      - 8080
    volumes:
      - stream-fusion:/app/config
      - taskiq-logs:/app/config/logs
      - torrent-cache:/var/cache/torrents
      - imdb-db:/data/imdb_db
      - sfr-db-backups:/data/backups
    depends_on:
      stremio-postgres:
        condition: service_healthy
      stremio-redis:
        condition: service_started
    restart: unless-stopped
    networks:
      - proxy_network

  stremio-redis:
    image: redis:7-alpine
    container_name: stremio-redis
    expose:
      - 6379
    volumes:
      - stremio-redis:/data
    command: redis-server --appendonly yes
    restart: unless-stopped
    networks:
      - proxy_network

  stremio-postgres:
    image: postgres:17-alpine
    container_name: stremio-postgres
    restart: unless-stopped
    environment:
      PGDATA: /var/lib/postgresql/data/pgdata
      POSTGRES_USER: streamfusion
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}
      POSTGRES_DB: streamfusion
      PG_BASE: streamfusion
      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_MIGRATION_USER: streamfusion_migration
      PG_MIGRATION_PASS: ${PG_MIGRATION_PASS:?PG_MIGRATION_PASS is required}
      PG_RESTORE_USER: streamfusion_restore
      PG_RESTORE_PASS_FILE: /run/pg-restore-secret/pg_restore_pass
      PG_OWNER_ROLE: streamfusion_owner
    depends_on:
      pg-restore-secret-init:
        condition: service_completed_successfully
    expose:
      - 5432
    volumes:
      - stremio-postgres:/var/lib/postgresql/data/pgdata
      - pg-restore-secret:/run/pg-restore-secret:ro
      - ./postgres-init/10-streamfusion-security.sh:/docker-entrypoint-initdb.d/10-streamfusion-security.sh:ro
    healthcheck:
      test:
        - CMD-SHELL
        - >-
          PGPASSWORD="$$PG_PASS"
          psql -h 127.0.0.1
          -U "$$PG_USER"
          -d "$$POSTGRES_DB"
          -X -qAt -v ON_ERROR_STOP=1
          -c "SELECT CASE WHEN
          EXISTS (SELECT 1 FROM pg_roles WHERE rolname='streamfusion_runtime' AND rolcanlogin AND NOT rolsuper AND NOT rolcreatedb AND NOT rolcreaterole)
          AND EXISTS (SELECT 1 FROM pg_roles WHERE rolname='streamfusion_migration' AND rolcanlogin AND NOT rolsuper AND NOT rolcreatedb AND NOT rolcreaterole)
          AND EXISTS (SELECT 1 FROM pg_roles WHERE rolname='streamfusion_restore' AND rolcanlogin AND NOT rolsuper AND rolcreatedb AND NOT rolcreaterole)
          AND EXISTS (SELECT 1 FROM pg_roles WHERE rolname='streamfusion_owner' AND NOT rolcanlogin AND NOT rolsuper AND rolcreatedb AND NOT rolcreaterole)
          AND (SELECT pg_get_userbyid(datdba) FROM pg_database WHERE datname=current_database())='streamfusion_owner'
          THEN 1 ELSE 0 END"
          | grep -qx 1
      interval: 5s
      timeout: 5s
      retries: 20
      start_period: 5s
    networks:
      - proxy_network

  warp:
    image: caomingjun/warp:latest
    container_name: warp
    restart: always
    expose:
      - 1080
    environment:
      - WARP_SLEEP=2
    cap_add:
      - NET_ADMIN
    sysctls:
      - net.ipv6.conf.all.disable_ipv6=0
      - net.ipv4.conf.all.src_valid_mark=1
    volumes:
      - warp-data:/var/lib/cloudflare-warp
    networks:
      - proxy_network

volumes:
  stremio-postgres:
  stremio-redis:
  stream-fusion:
  warp-data:
  dmm-hashlists:
  sfr-db-backups:
  imdb-db:
  torrent-cache:
  taskiq-logs:
  pg-restore-secret:
```

---

## Mise à jour

```bash
docker compose pull
docker compose up -d
```
