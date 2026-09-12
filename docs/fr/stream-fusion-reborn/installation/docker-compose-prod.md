# Déploiement production

Cette configuration utilise le même Docker Compose de référence que
le déploiement mono-instance, avec l'image publique Docker Hub :

```text
laster13/stream-fusion-reborn:latest
```

!!! info "Configuration commune"
    Les pages **Instance unique** et **Production** utilisent le même
    Docker Compose afin d'éviter toute divergence entre deux versions
    de la stack.

    En production, la différence repose principalement sur le reverse
    proxy, HTTPS/TLS, la supervision, les sauvegardes et les pratiques
    d'exploitation.

---

## Architecture

La stack comprend :

| Service | Fonction |
|---|---|
| `stream-fusion` | Application Stream Fusion Reborn |
| `taskiq-worker` | Exécution des tâches asynchrones |
| `taskiq-scheduler` | Planification Taskiq |
| `stremio-postgres` | PostgreSQL 17 |
| `stremio-redis` | Redis 7 |
| `meilisearch` | Recherche et indexation |
| `meili-init` | Préparation de Meilisearch |
| `postgres-security-init` | Sécurisation des rôles PostgreSQL |
| `pg-restore-secret-init` | Génération du secret de restauration |
| `warp` | Proxy WARP |

!!! warning "Taskiq Scheduler"
    `taskiq-scheduler` doit conserver une seule instance.

---

## Sécurité PostgreSQL

Le Compose sépare les responsabilités entre quatre rôles :

| Rôle | Fonction |
|---|---|
| `streamfusion_owner` | Propriétaire des objets |
| `streamfusion_runtime` | Connexion normale de l'application |
| `streamfusion_migration` | Exécution des migrations |
| `streamfusion_restore` | Opérations de restauration |

Le secret du rôle de restauration n'est pas stocké dans `.env`.

Il est généré automatiquement dans le volume :

```text
pg-restore-secret
```

---

## Réseau et reverse proxy

Le Compose utilise le réseau Docker externe :

```text
traefik_proxy
```

Vérifiez son existence :

```bash
docker network inspect traefik_proxy
```

S'il n'existe pas encore :

```bash
docker network create traefik_proxy
```

!!! warning "Port 8080"
    `stream-fusion` utilise `expose: 8080`.

    Le port n'est pas publié directement sur l'hôte par le Compose.
    Le reverse proxy doit être connecté au réseau `traefik_proxy`.

---

## Préparer le fichier `.env`

Créez `.env` dans le même répertoire que le Compose.

Pour générer une valeur secrète de 64 caractères hexadécimaux :

```bash
openssl rand -hex 32
```

Pour générer les secrets internes :

```bash
for name in \
  SECRET_API_KEY \
  CONFIG_SECRET_KEY \
  SESSION_KEY \
  PEER_MASTER_KEY \
  MEILI_MASTER_KEY \
  POSTGRES_PASSWORD \
  PG_PASS \
  PG_MIGRATION_PASS
do
  printf '%s=' "$name"
  openssl rand -hex 32
done
```

!!! danger "Secrets PostgreSQL distincts"
    `POSTGRES_PASSWORD`, `PG_PASS` et `PG_MIGRATION_PASS`
    doivent obligatoirement contenir trois valeurs différentes.

### `.env` complet

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
    Ne définissez pas `PG_RESTORE_PASS` dans `.env`.

    Le Compose crée automatiquement le secret de restauration.

---

## Docker Compose de production

Les services Stream Fusion utilisent l'image Docker Hub :

```text
laster13/stream-fusion-reborn:latest
```

Le Compose ci-dessous est identique à celui de la page
**Instance unique**.

### `docker-compose.yml`

```yaml
---
networks:
  proxy_network:
    external: true
    name: traefik_proxy

services:

  meili-init:
    image: laster13/stream-fusion-reborn:latest
    user: "0:0"
    entrypoint: ["/bin/sh", "-c"]
    command:
      - |
        set -eu

        echo "[meili-init] Préparation"

        mkdir -p /meili_wrapper
        mkdir -p /meili_restore_control

        cp \
          /opt/streamfusion/meili-auto-restore.sh \
          /meili_wrapper/.meili-auto-restore.sh.tmp

        chmod 0555 \
          /meili_wrapper/.meili-auto-restore.sh.tmp

        mv -f \
          /meili_wrapper/.meili-auto-restore.sh.tmp \
          /meili_wrapper/meili-auto-restore.sh

        chown -R 1000:1000 \
          /meili_restore_control

        chmod 0770 \
          /meili_restore_control

        find /meili_restore_control \
          -type f \
          -exec chmod 0660 {} \;

        echo "[meili-init] Terminé"
    volumes:
      - meili-wrapper:/meili_wrapper
      - meili-restore-control:/meili_restore_control
    network_mode: "none"
    restart: "no"

  meilisearch:
    image: getmeili/meilisearch:v1.41.0
    container_name: meilisearch
    environment:
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY:?Provide MEILI_MASTER_KEY}
      MEILI_ENV: production
      MEILI_EXPERIMENTAL_DUMPLESS_UPGRADE: "true"
      MEILI_DB_PATH: /meili_data/data.ms
    expose:
      - 7700
    volumes:
      - meili-data:/meili_data
      - sfr-db-backups:/imports:ro
      - meili-wrapper:/meili_wrapper:ro
      - meili-restore-control:/meili_restore_control
    command: ["/meili_wrapper/meili-auto-restore.sh"]
    depends_on:
      meili-init:
        condition: service_completed_successfully
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:7700/health >/dev/null || exit 1"]
      interval: 5s
      timeout: 5s
      retries: 10
      start_period: 5s
    restart: unless-stopped
    networks:
      - proxy_network

  pg-restore-secret-init:
    image: postgres:17-alpine
    command:
      - /bin/sh
      - -ec
      - |
        set -eu
        umask 077

        secret=/run/pg-restore-secret/pg_restore_pass
        tmp="$${secret}.tmp.$$$$"

        if [ ! -s "$$secret" ]; then
          rm -f "$$tmp"
          od -An -N32 -tx1 /dev/urandom | tr -d ' \n' > "$$tmp"
          test "$$(wc -c < "$$tmp" | tr -d ' ')" -eq 64
          chmod 0444 "$$tmp"
          mv -f "$$tmp" "$$secret"
        fi

        test "$$(wc -c < "$$secret" | tr -d ' ')" -eq 64
        grep -Eq '^[0-9a-f]{64}$' "$$secret"
        chmod 0444 "$$secret"
    volumes:
      - pg-restore-secret:/run/pg-restore-secret
    network_mode: "none"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    read_only: true
    restart: "no"

  stremio-postgres:
    image: postgres:17-alpine
    container_name: stremio-postgres
    restart: unless-stopped
    environment:
      PGDATA: /var/lib/postgresql/data/pgdata
      POSTGRES_USER: streamfusion
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}
      POSTGRES_DB: streamfusion
    expose:
      - 5432
    volumes:
      - stremio-postgres:/var/lib/postgresql/data/pgdata
    healthcheck:
      test:
        - CMD-SHELL
        - >-
          PGPASSWORD="$$POSTGRES_PASSWORD"
          psql -h 127.0.0.1
          -U "$$POSTGRES_USER"
          -d "$$POSTGRES_DB"
          -X -qAt -v ON_ERROR_STOP=1
          -c "SELECT 1"
          | grep -qx 1
      interval: 5s
      timeout: 5s
      retries: 20
      start_period: 5s
    networks:
      - proxy_network

  postgres-security-init:
    image: postgres:17-alpine
    restart: "no"
    environment:
      POSTGRES_USER: streamfusion
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}
      POSTGRES_DB: streamfusion
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_MIGRATION_PASS: ${PG_MIGRATION_PASS:?PG_MIGRATION_PASS is required}
      PG_RESTORE_PASS_FILE: /run/pg-restore-secret/pg_restore_pass
    volumes:
      - pg-restore-secret:/run/pg-restore-secret:ro
    depends_on:
      pg-restore-secret-init:
        condition: service_completed_successfully
      stremio-postgres:
        condition: service_healthy
    command:
      - /bin/sh
      - -ec
      - |
        set -eu

        echo "[postgres-security] Configuration des rôles Stream Fusion"

        : "$${POSTGRES_USER:?POSTGRES_USER manquant}"
        : "$${POSTGRES_DB:?POSTGRES_DB manquant}"
        : "$${POSTGRES_PASSWORD:?POSTGRES_PASSWORD manquant}"
        : "$${PG_PASS:?PG_PASS manquant}"
        : "$${PG_MIGRATION_PASS:?PG_MIGRATION_PASS manquant}"

        RESTORE_PASS_FILE="$${PG_RESTORE_PASS_FILE:-/run/pg-restore-secret/pg_restore_pass}"

        validate_hex64() {
          name="$$1"
          value="$$2"

          if [ "$${#value}" -ne 64 ]; then
            echo "[postgres-security] ERREUR : $$name doit contenir exactement 64 caractères hexadécimaux"
            exit 1
          fi

          case "$$value" in
            *[!0-9a-f]*)
              echo "[postgres-security] ERREUR : $$name doit être hexadécimal en minuscules"
              exit 1
              ;;
          esac
        }

        validate_hex64 "POSTGRES_PASSWORD" "$$POSTGRES_PASSWORD"
        validate_hex64 "PG_PASS" "$$PG_PASS"
        validate_hex64 "PG_MIGRATION_PASS" "$$PG_MIGRATION_PASS"

        if [ ! -s "$$RESTORE_PASS_FILE" ]; then
          echo "[postgres-security] ERREUR : secret restore absent : $$RESTORE_PASS_FILE"
          exit 1
        fi

        RESTORE_PASS="$$(cat "$$RESTORE_PASS_FILE")"
        validate_hex64 "PG_RESTORE_PASS" "$$RESTORE_PASS"

        if [ "$$POSTGRES_PASSWORD" = "$$PG_PASS" ] || \
           [ "$$POSTGRES_PASSWORD" = "$$PG_MIGRATION_PASS" ] || \
           [ "$$POSTGRES_PASSWORD" = "$$RESTORE_PASS" ] || \
           [ "$$PG_PASS" = "$$PG_MIGRATION_PASS" ] || \
           [ "$$PG_PASS" = "$$RESTORE_PASS" ] || \
           [ "$$PG_MIGRATION_PASS" = "$$RESTORE_PASS" ]; then
          echo "[postgres-security] ERREUR : les quatre secrets PostgreSQL doivent être distincts"
          exit 1
        fi

        export PGPASSWORD="$$POSTGRES_PASSWORD"

        psql \
          --host=stremio-postgres \
          --username="$$POSTGRES_USER" \
          --dbname="$$POSTGRES_DB" \
          --no-psqlrc \
          --set=ON_ERROR_STOP=1 \
          --set=runtime_password="$$PG_PASS" \
          --set=migration_password="$$PG_MIGRATION_PASS" \
          --set=restore_password="$$RESTORE_PASS" <<'SQL'
        DO $$$$
        BEGIN
          IF NOT EXISTS (
            SELECT 1 FROM pg_roles
            WHERE rolname = 'streamfusion_owner'
          ) THEN
            CREATE ROLE streamfusion_owner;
          END IF;

          IF NOT EXISTS (
            SELECT 1 FROM pg_roles
            WHERE rolname = 'streamfusion_runtime'
          ) THEN
            CREATE ROLE streamfusion_runtime LOGIN;
          END IF;

          IF NOT EXISTS (
            SELECT 1 FROM pg_roles
            WHERE rolname = 'streamfusion_migration'
          ) THEN
            CREATE ROLE streamfusion_migration LOGIN;
          END IF;

          IF NOT EXISTS (
            SELECT 1 FROM pg_roles
            WHERE rolname = 'streamfusion_restore'
          ) THEN
            CREATE ROLE streamfusion_restore LOGIN;
          END IF;
        END
        $$$$;

        ALTER ROLE streamfusion_owner
          WITH NOLOGIN NOSUPERUSER CREATEDB NOCREATEROLE NOINHERIT NOREPLICATION NOBYPASSRLS;

        ALTER ROLE streamfusion_runtime
          WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION NOBYPASSRLS
          PASSWORD :'runtime_password';

        ALTER ROLE streamfusion_migration
          WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION NOBYPASSRLS
          PASSWORD :'migration_password';

        ALTER ROLE streamfusion_restore
          WITH LOGIN NOSUPERUSER CREATEDB NOCREATEROLE NOINHERIT NOREPLICATION NOBYPASSRLS
          PASSWORD :'restore_password';

        GRANT streamfusion_owner
          TO streamfusion_migration
          WITH INHERIT FALSE, SET TRUE;

        GRANT streamfusion_owner
          TO streamfusion_restore
          WITH INHERIT FALSE, SET TRUE;

        GRANT pg_signal_backend
          TO streamfusion_restore
          WITH INHERIT TRUE, SET TRUE;

        DO $$$$
        BEGIN
          IF EXISTS (
            SELECT 1
            FROM pg_auth_members m
            JOIN pg_roles parent ON parent.oid = m.roleid
            JOIN pg_roles member ON member.oid = m.member
            WHERE parent.rolname = 'streamfusion_owner'
              AND member.rolname = 'streamfusion_runtime'
          ) THEN
            EXECUTE 'REVOKE streamfusion_owner FROM streamfusion_runtime';
          END IF;
        END
        $$$$;

        ALTER DATABASE streamfusion OWNER TO streamfusion_owner;
        ALTER SCHEMA public OWNER TO streamfusion_owner;

        DO $$$$
        DECLARE
          obj record;
          ddl text;
        BEGIN
          FOR obj IN
            SELECT
              n.nspname,
              c.relname,
              c.relkind
            FROM pg_class c
            JOIN pg_namespace n ON n.oid = c.relnamespace
            WHERE n.nspname = 'public'
              AND pg_get_userbyid(c.relowner) = 'streamfusion'
              AND c.relkind IN ('r', 'p', 'S', 'v', 'm', 'f')
              AND NOT EXISTS (
                SELECT 1
                FROM pg_depend d
                WHERE d.classid = 'pg_class'::regclass
                  AND d.objid = c.oid
                  AND d.deptype = 'e'
              )
            ORDER BY
              CASE c.relkind
                WHEN 'S' THEN 2
                ELSE 1
              END,
              c.relname
          LOOP
            ddl := CASE obj.relkind
              WHEN 'S' THEN format(
                'ALTER SEQUENCE %I.%I OWNER TO streamfusion_owner',
                obj.nspname, obj.relname
              )
              WHEN 'v' THEN format(
                'ALTER VIEW %I.%I OWNER TO streamfusion_owner',
                obj.nspname, obj.relname
              )
              WHEN 'm' THEN format(
                'ALTER MATERIALIZED VIEW %I.%I OWNER TO streamfusion_owner',
                obj.nspname, obj.relname
              )
              WHEN 'f' THEN format(
                'ALTER FOREIGN TABLE %I.%I OWNER TO streamfusion_owner',
                obj.nspname, obj.relname
              )
              ELSE format(
                'ALTER TABLE %I.%I OWNER TO streamfusion_owner',
                obj.nspname, obj.relname
              )
            END;

            EXECUTE ddl;
          END LOOP;
        END
        $$$$;

        REVOKE ALL ON DATABASE streamfusion FROM PUBLIC;

        GRANT CONNECT ON DATABASE streamfusion
          TO streamfusion_runtime, streamfusion_migration, streamfusion_restore;

        REVOKE CREATE ON SCHEMA public FROM PUBLIC;
        REVOKE CREATE ON SCHEMA public FROM streamfusion_runtime;
        GRANT USAGE ON SCHEMA public TO streamfusion_runtime;

        GRANT SELECT, INSERT, UPDATE, DELETE
          ON ALL TABLES IN SCHEMA public
          TO streamfusion_runtime;

        GRANT USAGE, SELECT, UPDATE
          ON ALL SEQUENCES IN SCHEMA public
          TO streamfusion_runtime;

        ALTER DEFAULT PRIVILEGES FOR ROLE streamfusion_owner IN SCHEMA public
          GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO streamfusion_runtime;

        ALTER DEFAULT PRIVILEGES FOR ROLE streamfusion_owner IN SCHEMA public
          GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO streamfusion_runtime;
        SQL

        result="$$(psql \
          --host=stremio-postgres \
          --username="$$POSTGRES_USER" \
          --dbname="$$POSTGRES_DB" \
          --no-psqlrc \
          --tuples-only \
          --no-align \
          --set=ON_ERROR_STOP=1 <<'SQL'
        SELECT CASE
        WHEN
          EXISTS (
            SELECT 1
            FROM pg_roles
            WHERE rolname = 'streamfusion_owner'
              AND NOT rolcanlogin
              AND NOT rolsuper
              AND rolcreatedb
              AND NOT rolcreaterole
              AND NOT rolinherit
              AND NOT rolreplication
              AND NOT rolbypassrls
          )
          AND EXISTS (
            SELECT 1
            FROM pg_roles
            WHERE rolname = 'streamfusion_runtime'
              AND rolcanlogin
              AND NOT rolsuper
              AND NOT rolcreatedb
              AND NOT rolcreaterole
              AND NOT rolinherit
              AND NOT rolreplication
              AND NOT rolbypassrls
          )
          AND EXISTS (
            SELECT 1
            FROM pg_roles
            WHERE rolname = 'streamfusion_migration'
              AND rolcanlogin
              AND NOT rolsuper
              AND NOT rolcreatedb
              AND NOT rolcreaterole
              AND NOT rolinherit
              AND NOT rolreplication
              AND NOT rolbypassrls
          )
          AND EXISTS (
            SELECT 1
            FROM pg_roles
            WHERE rolname = 'streamfusion_restore'
              AND rolcanlogin
              AND NOT rolsuper
              AND rolcreatedb
              AND NOT rolcreaterole
              AND NOT rolinherit
              AND NOT rolreplication
              AND NOT rolbypassrls
          )
          AND EXISTS (
            SELECT 1
            FROM pg_auth_members m
            JOIN pg_roles parent ON parent.oid = m.roleid
            JOIN pg_roles member ON member.oid = m.member
            WHERE parent.rolname = 'streamfusion_owner'
              AND member.rolname = 'streamfusion_migration'
              AND NOT m.inherit_option
              AND m.set_option
          )
          AND EXISTS (
            SELECT 1
            FROM pg_auth_members m
            JOIN pg_roles parent ON parent.oid = m.roleid
            JOIN pg_roles member ON member.oid = m.member
            WHERE parent.rolname = 'streamfusion_owner'
              AND member.rolname = 'streamfusion_restore'
              AND NOT m.inherit_option
              AND m.set_option
          )
          AND pg_has_role('streamfusion_restore', 'pg_signal_backend', 'MEMBER')
          AND pg_has_role('streamfusion_restore', 'pg_signal_backend', 'USAGE')
          AND (
            SELECT pg_get_userbyid(datdba)
            FROM pg_database
            WHERE datname = 'streamfusion'
          ) = 'streamfusion_owner'
          AND (
            SELECT pg_get_userbyid(nspowner)
            FROM pg_namespace
            WHERE nspname = 'public'
          ) = 'streamfusion_owner'
          AND NOT EXISTS (
            SELECT 1
            FROM pg_class c
            JOIN pg_namespace n ON n.oid = c.relnamespace
            WHERE n.nspname = 'public'
              AND pg_get_userbyid(c.relowner) = 'streamfusion'
              AND c.relkind IN ('r', 'p', 'S', 'v', 'm', 'f')
              AND NOT EXISTS (
                SELECT 1
                FROM pg_depend d
                WHERE d.classid = 'pg_class'::regclass
                  AND d.objid = c.oid
                  AND d.deptype = 'e'
              )
          )
        THEN 'OK'
        ELSE 'ERROR'
        END;
        SQL
        )"

        test "$$result" = "OK"

        echo "[postgres-security] Configuration validée"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp:mode=1777
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
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 10
    restart: unless-stopped
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

  taskiq-worker:
    image: laster13/stream-fusion-reborn:latest
    container_name: taskiq-worker
    command: python -m taskiq worker stream_fusion.worker:broker
    # env_file: user.env        # uncomment to enable unique_account mode (debrid/indexers)
    environment:
      SECRET_API_KEY: ${SECRET_API_KEY:?Provide SECRET_API_KEY}
      CONFIG_SECRET_KEY: ${CONFIG_SECRET_KEY:?Provide CONFIG_SECRET_KEY}
      SESSION_KEY: ${SESSION_KEY:?Provide SESSION_KEY}
      PEER_MASTER_KEY: ${PEER_MASTER_KEY:?Provide PEER_MASTER_KEY}
      TMDB_API_KEY: ${TMDB_API_KEY:?Provide TMDB_API_KEY}
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY:?Provide MEILI_MASTER_KEY}

      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_BASE: streamfusion

      PG_RESTORE_USER: streamfusion_restore
      PG_RESTORE_PASS_FILE: /run/pg-restore-secret/pg_restore_pass
      PG_OWNER_ROLE: streamfusion_owner

      TZ: ${TZ:-Europe/Paris}
      PROXY_URL: ${PROXY_URL:-http://warp:1080}

      REDIS_HOST: stremio-redis
      PG_HOST: stremio-postgres
      MEILI_HOST: meilisearch
      MEILI_PORT: "7700"
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
      - meili-data:/meili_data:ro
      - meili-restore-control:/meili_restore_control
      - taskiq-logs:/app/config/logs
    depends_on:
      postgres-security-init:
        condition: service_completed_successfully
      stremio-redis:
        condition: service_healthy
      meilisearch:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - proxy_network

  taskiq-scheduler:
    image: laster13/stream-fusion-reborn:latest
    container_name: taskiq-scheduler
    command: python -m taskiq scheduler stream_fusion.tkq:scheduler
    environment:
      SESSION_KEY: ${SESSION_KEY:?Provide SESSION_KEY}

      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_BASE: streamfusion

      TZ: ${TZ:-Europe/Paris}

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
      postgres-security-init:
        condition: service_completed_successfully
      stremio-redis:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - proxy_network
    # IMPORTANT: replicas must always be 1

  stream-fusion:
    image: laster13/stream-fusion-reborn:latest
    container_name: stream-fusion
    # env_file: user.env        # uncomment to enable unique_account mode (debrid/indexers)
    environment:
      RUN_MIGRATIONS: "true"

      SECRET_API_KEY: ${SECRET_API_KEY:?Provide SECRET_API_KEY}
      ADMIN_SECRET_KEY: ${ADMIN_SECRET_KEY:?Provide ADMIN_SECRET_KEY}
      CONFIG_SECRET_KEY: ${CONFIG_SECRET_KEY:?Provide CONFIG_SECRET_KEY}
      SESSION_KEY: ${SESSION_KEY:?Provide SESSION_KEY}
      PEER_MASTER_KEY: ${PEER_MASTER_KEY:?Provide PEER_MASTER_KEY}
      TMDB_API_KEY: ${TMDB_API_KEY:?Provide TMDB_API_KEY}
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY:?Provide MEILI_MASTER_KEY}

      PG_USER: streamfusion_runtime
      PG_PASS: ${PG_PASS:?PG_PASS is required}
      PG_BASE: streamfusion

      PG_MIGRATION_USER: streamfusion_migration
      PG_MIGRATION_PASS: ${PG_MIGRATION_PASS:?PG_MIGRATION_PASS is required}
      PG_OWNER_ROLE: streamfusion_owner

      TZ: ${TZ:-Europe/Paris}
      USE_HTTPS: ${USE_HTTPS:-true}
      PROXY_URL: ${PROXY_URL:-http://warp:1080}

      REDIS_HOST: stremio-redis
      PG_HOST: stremio-postgres
      MEILI_HOST: meilisearch
      MEILI_PORT: "7700"
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
      postgres-security-init:
        condition: service_completed_successfully
      stremio-redis:
        condition: service_healthy
      meilisearch:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - proxy_network

volumes:
  stremio-postgres:
  stremio-redis:
  stream-fusion:
  warp-data:
  meili-data:
  dmm-hashlists:
  sfr-db-backups:
  meili-restore-control:
  meili-wrapper:
  imdb-db:
  torrent-cache:
  taskiq-logs:
  pg-restore-secret:
```

---

## Validation de la configuration

Avant le démarrage :

```bash
docker compose config
```

Puis vérifiez le réseau :

```bash
docker network inspect traefik_proxy
```

---

## Démarrage

```bash
docker compose up -d
```

Vérifiez l'état de la stack :

```bash
docker compose ps
```

Logs de l'application :

```bash
docker compose logs -f stream-fusion
```

Logs Taskiq :

```bash
docker compose logs -f taskiq-worker taskiq-scheduler
```

---

## Mise à jour

Récupérez les dernières images :

```bash
docker compose pull
```

Puis recréez les conteneurs :

```bash
docker compose up -d
```

---

## Vérifications après mise à jour

```bash
docker compose ps
docker compose logs --tail=100 stream-fusion
docker compose logs --tail=100 taskiq-worker
docker compose logs --tail=100 taskiq-scheduler
```

Vérifiez que :

- PostgreSQL est healthy ;
- Redis est healthy ;
- Meilisearch est healthy ;
- `postgres-security-init` se termine correctement ;
- `stream-fusion` démarre sans erreur ;
- `taskiq-worker` démarre sans erreur ;
- `taskiq-scheduler` reste à une seule instance.
