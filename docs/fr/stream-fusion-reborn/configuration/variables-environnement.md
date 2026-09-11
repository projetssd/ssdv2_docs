# Variables d'environnement

Référence exhaustive de toutes les variables d'environnement de Stream Fusion Reborn, extraites de `stream_fusion/settings.py`.

??? tip "Conventions"
    - Les valeurs entre guillemets (ex: `"8080"`) sont des chaînes
    - Les valeurs sans guillemets (ex: `8080`) sont des entiers ou booléens
    - `None` = variable optionnelle (vaut `null` par défaut)
    - :fontawesome-solid-lock: = obligatoire pour le fonctionnement minimal

---

## Core

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `WORKERS_COUNT` | `int` | CPU×2 (2-8) | Nombre de workers Gunicorn |
| `PORT` | `int` | `8080` | Port d'écoute |
| `HOST` | `str` | `0.0.0.0` | Adresse d'écoute |
| `GUNICORN_TIMEOUT` | `int` | `180` | Timeout Gunicorn (s) |
| `AIOHTTP_TIMEOUT` | `int` | `7200` | Timeout HTTP client (2h) |
| `SESSION_KEY` | `str` | obligatoire* | Clé de session Starlette. Obligatoire en lancement direct ; l'entrypoint Docker en génère une forte au démarrage si elle est absente. En production, fournissez une valeur persistante pour conserver les sessions après recréation du conteneur. |
| `USE_HTTPS` | `bool` | `True` | Activer HTTPS pour les URLs |
| `ALLOW_DEBRID_DOWNLOAD` | `bool` | `True` | Afficher les streams non-cachés |
| `ALLOW_PUBLIC_KEY_REGISTRATION` | `bool` | `False` | Activer l'inscription publique des clés API |
| `NO_CACHE_VIDEO_LANGUAGE` | `str` | `FR` | Langue vidéo « indisponible » (`FR`/`EN`) |

## Sécurité :fontawesome-solid-lock:

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `SECRET_API_KEY` | `str` | `None` | :fontawesome-solid-lock: Clé d'authentification API |
| `ADMIN_SECRET_KEY` | `str` | `None` | :fontawesome-solid-lock: Clé dédiée à l'authentification de l'administration |
| `CONFIG_SECRET_KEY` | `str` | `None` | Clé active utilisée pour chiffrer les nouveaux tokens de configuration |
| `CONFIG_SECRET_KEY_PREVIOUS` | `str` | `None` | **Avancé — rotation uniquement.** Ancienne clé temporaire de déchiffrement ; absente du `.env` standard |
| `SECURITY_HIDE_DOCS` | `bool` | `True` | Masquer Swagger/ReDoc |

## Proxy

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `PROXY_URL` | `str` | `None` | URL proxy SOCKS5/HTTP pour les requêtes API |
| `PLAYBACK_PROXY` | `str` | `None` | Proxy pour les liens de streaming (voir [Proxy](proxy.md)) |
| `PROXIED_LINK` | `bool` | `False` | Activer la proxyfication des liens debrid (voir [Proxy](proxy.md)) |
| `PLAYBACK_LIMIT_REQUESTS` | `int` | `60` | Max requêtes lecture par fenêtre |
| `PLAYBACK_LIMIT_SECONDS` | `int` | `60` | Durée de la fenêtre (s) |

Voir la page [Proxy](proxy.md) pour une explication détaillée du fonctionnement.

## Peer

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `PEER_MASTER_KEY` | `str` | `""` | Clé maîtresse Fernet pour les secrets peer |
| `PEER_SYNC_DEFAULT_CRON` | `str` | `0 */6 * * *` | Cron sync par défaut (toutes les 6h) |

## Services Debrid

### Real-Debrid

!!! danger "Service en fin de vie"
    Real-Debrid est un service déconseillé : cache FR pauvre, résultats fréquemment faux, API restrictive. Son support est maintenu pour les comptes existants uniquement. La variable `RD_UNIQUE_ACCOUNT` permet de limiter le recours à Real-Debrid.

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `RD_TOKEN` | `str` | `None` | Token API Real-Debrid |
| `RD_UNIQUE_ACCOUNT` | `bool` | auto | Compte serveur unique (auto si token présent) |

### AllDebrid (recommandé)

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `AD_TOKEN` | `str` | `None` | Token API AllDebrid |
| `AD_UNIQUE_ACCOUNT` | `bool` | auto | Compte serveur unique (auto si token présent) |

### TorBox

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `TB_TOKEN` | `str` | `None` | Token API TorBox |
| `TB_UNIQUE_ACCOUNT` | `bool` | auto | Compte serveur unique (auto si token présent) |

### Premiumize

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `PM_TOKEN` | `str` | `None` | Token API Premiumize |

### Debrid-Link

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `DL_TOKEN` | `str` | `None` | Token API Debrid-Link |
| `DL_UNIQUE_ACCOUNT` | `bool` | auto | Compte serveur unique (auto si token présent) |
| `DL_BASE_URL` | `str` | `https://debrid-link.com/api/v2` | URL de l'API |
| `DL_CLIENT_ID` | `str` | `None` | Client ID OAuth2 pour le device-flow |

### Autres services

| Variable | Type | Description |
|---|---|---|
| `ED_TOKEN` | `str` | Token EasyDebrid |
| `OC_CREDENTIALS` | `str` | Identifiants Offcloud (`email:password`) |
| `PP_CREDENTIALS` | `str` | Identifiants PikPak (`email:password`) |
| `STREMTHRU_URL` | `str` | URL serveur StremThru (défaut: `https://stremthru.13377001.xyz`) |

??? info "Comptes uniques"
    Les variables `*_UNIQUE_ACCOUNT` sont automatiquement définies à `True` quand le token correspondant est présent dans l'environnement. Cela active le mode "compte serveur unique" où le token est partagé entre tous les utilisateurs.

    !!! warning "Usage privé uniquement"
        Si un compte debrid est configuré en variable d'environnement, il sera accessible par **tous les utilisateurs**. Pour une petite instance familiale, cela peut être acceptable. Pour une instance publique, laissez chaque utilisateur configurer son propre service depuis la page de configuration du plugin.

## Logging

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `LOG_LEVEL` | `str` | `INFO` | Niveau de log (`TRACE`/`DEBUG`/`INFO`/`WARNING`/`ERROR`/`FATAL`) |
| `LOG_PATH` | `str` | `/app/config/logs/stream-fusion.log` | Chemin du fichier de log |
| `LOG_REDACTED` | `bool` | `True` | Censure les secrets dans les logs |

## PostgreSQL

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `PG_HOST` | `str` | `stremio-postgres` | Hôte PostgreSQL |
| `PG_PORT` | `int` | `5432` | Port PostgreSQL |
| `PG_USER` | `str` | `streamfusion_runtime` | Rôle runtime interne ; ne pas modifier pour une installation standard |
| `PG_PASS` | `str` | — (requis) | Mot de passe PostgreSQL de l'application |
| `PG_BASE` | `str` | `streamfusion` | Base interne ; ne pas modifier pour une installation standard |
| `PG_MIGRATION_PASS` | `str` | — (requis) | Mot de passe dédié aux migrations automatiques |
| `PG_ECHO` | `bool` | `False` | Echo SQLAlchemy (debug) |
| `PG_POOL_SIZE` | `int` | `5` | Taille du pool |
| `PG_MAX_OVERFLOW` | `int` | `5` | Overflow max du pool |

## Redis

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `REDIS_HOST` | `str` | `redis` | Hôte Redis |
| `REDIS_PORT` | `int` | `6379` | Port Redis |
| `REDIS_DB` | `int` | `5` | DB Redis (cache SF) |
| `REDIS_EXPIRATION` | `int` | `604800` | TTL par défaut (7 jours) |
| `REDIS_PASSWORD` | `str` | `None` | Mot de passe Redis |

### Préchargement d'épisodes

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `BG_REFRESH_INDEXER_TTL` | `int` | `21600` | TTL verrou refresh (6h) |
| `PREFETCH_EPISODE_LOCK_TTL` | `int` | `1200` | TTL verrou préchargement (20 min) |
| `MAX_CONCURRENT_SERIES_PREFETCH` | `int` | `2` | Max tâches prefetch simultanées |
| `PREFETCH_DEPTH` | `int` | `1` | Épisodes à précharger (1=N+1) |

## Meilisearch

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `MEILI_HOST` | `str` | `meilisearch` | Hôte Meilisearch |
| `MEILI_PORT` | `int` | `7700` | Port |
| `MEILI_MASTER_KEY` | `str` | `masterKey` | Clé maîtresse |
| `MEILI_CACHE_ENABLE` | `bool` | `True` | Activer le cache public local |

## Taskiq

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `TASKIQ_REDIS_DB` | `int` | `6` | DB Redis broker (≠ DB5 cache) |
| `TASKIQ_TORRENT_ORPHAN_MAX_AGE_DAYS` | `int` | `7` | Âge max orphelins (jours) |
| `TASKIQ_TMDB_MATCH_BATCH_SIZE` | `int` | `500` | Batch matching TMDB |
| `TASKIQ_IMDB_MATCH_BATCH_SIZE` | `int` | `500` | Batch matching IMDB |

## DMM Hashlists

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `DMM_REPO_URL` | `str` | URL DMM | URL du dépôt hashlists |
| `DMM_REPO_PATH` | `str` | `/data/dmm_hashlists` | Chemin local du clone |
| `DMM_SYNC_ENABLED` | `bool` | `True` | Master switch |
| `DMM_SYNC_SCHEDULE_ENABLED` | `bool` | `False` | Cron auto |
| `DMM_SYNC_CRON` | `str` | `0 2 * * *` | Horaire sync |

## U2P / Utopeer (Nostr NIP-35)

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `U2P_SYNC_ENABLED` | `bool` | `False` | Master switch |
| `U2P_SYNC_SCHEDULE_ENABLED` | `bool` | `False` | Cron auto |
| `U2P_SYNC_CRON` | `str` | `0 3 * * 0` | Horaire (dimanche 3h) |
| `UTOPEER_PASSKEY` | `str` | `None` | Passkey Utopeer (**déprécié**, ne plus utiliser) |
| `UTOPEER_RELAY_TIMEOUT` | `int` | `8` | Timeout relay (s) |
| `UTOPEER_ENABLED_CATEGORIES` | `str` | *(voir défaut)* | Catégories Nostr (CSV) |

## IMDB (DuckDB)

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `IMDB_DB_DIR` | `str` | `/data/imdb_db` | Répertoire DuckDB |
| `IMDB_MEMORY_LIMIT` | `str` | `5GB` | Limite mémoire DuckDB |
| `IMDB_THREADS` | `int` | `4` | Threads DuckDB |
| `IMDB_AKA_REGIONS` | `str` | `FR,BE,CH,CA,LU` | Régions AKA incluses |
| `IMDB_SYNC_ENABLED` | `bool` | `True` | Master switch |
| `IMDB_BUILD_SCHEDULE_ENABLED` | `bool` | `False` | Cron auto rebuild |
| `IMDB_BUILD_CRON` | `str` | `0 3 1,15 * *` | Bi-mensuel à 3h |
| `IMDB_ENRICH_SCHEDULE_ENABLED` | `bool` | `False` | Cron auto enrich |
| `IMDB_ENRICH_CRON` | `str` | `0 5 * * *` | Quotidien à 5h |

## TMDB

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `TMDB_API_KEY` | `str` | `None` | :fontawesome-solid-lock: Clé API TMDB |
| `TMDB_LANGUAGE` | `str` | `fr-FR` | Langue métadonnées TMDB |

## DB Dumps

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `DB_DUMP_SCHEDULE_ENABLED` | `bool` | `False` | Master switch création auto (DuckDB + Meilisearch) |
| `DB_DUMP_CRON` | `str` | `0 4 * * 0` | Cron création dumps (dimanche 4h) |
| `DB_DUMP_RETENTION` | `int` | `3` | Nombre de dumps conservés par type |
| `DB_DUMP_TOKEN_TTL` | `int` | `600` | TTL token téléchargement (secondes, Redis DB5) |
| `DB_DUMP_PG_SCHEDULE_ENABLED` | `bool` | `False` | Master switch dump PostgreSQL auto |
| `DB_DUMP_PG_CRON` | `str` | `0 3 * * *` | Cron dump PostgreSQL (quotidien 3h) |
| `DB_DUMP_PG_RETENTION` | `int` | `7` | Rétention dumps PostgreSQL (7 jours) |

!!! info "Répertoire de stockage"
    Tous les dumps sont stockés dans `BACKUPS_DB_DIR` (défaut: `/data/backups`), organisés par type : `/data/backups/duckdb/`, `/data/backups/meilisearch/`, `/data/backups/postgresql/`. Chaque répertoire contient un `manifest.json` listant les dumps disponibles avec leurs métadonnées (SHA-256, taille, timestamp).

## Tâches cron

| Variable | Défaut | Description |
|---|---|---|
| `TASK_CRON_DEBRID_CACHE_CLEANUP` | `0 */6 * * *` | Nettoyage cache debrid |
| `TASK_CRON_TORRENT_ORPHAN_CLEANUP` | `0 1 * * *` | Suppression orphelins |
| `TASK_CRON_TORRENT_DEDUP` | `0 2 * * *` | Dédoublonnage |
| `TASK_CRON_TORRENT_GROUP_HASH` | `0 3 * * *` | Groupement par hash |
| `TASK_CRON_TORRENT_GROUP_TITLE_SIZE` | `0 4 * * *` | Groupement titre/taille |
| `TASK_CRON_FIX_TYPE_INCONSISTENCIES` | `0 5 * * *` | Correction types |
| `TASK_CRON_API_KEYS_CLEANUP` | `0 */6 * * *` | Nettoyage clés API |
| `TASK_CRON_PEER_KEYS_CLEANUP` | `0 */6 * * *` | Nettoyage peer keys |
| `TASK_CRON_TMDB_ORPHAN_MATCHING` | `*/30 * * * *` | Matching TMDB |
| `TASK_CRON_IMDB_ORPHAN_MATCHING` | `*/30 * * * *` | Matching IMDB |
| `TASK_CRON_DB_DUMP_CREATE` | `0 4 * * 0` | Création dumps DuckDB + Meilisearch |
| `TASK_CRON_DB_DUMP_CREATE_PG` | `0 3 * * *` | Dump PostgreSQL quotidien |
| `TASK_CRON_TRASH_SYNC` | `0 */6 * * *` | Synchronisation TRaSH CFs + templates |
| `TASK_CRON_PG_RTN_PARSE` | `0 */6 * * *` | Parsing RTN PostgreSQL |
| `TASK_CRON_IMDB_TMDB_ENRICH_DUCK` | `0 4 * * *` | Enrichissement TMDB → DuckDB |
| `TASK_CRON_TMDB_ENRICH_MEILI` | `0 * * * *` | Backfill TMDB IDs Meilisearch |

### Flags d'activation

Chaque tâche possède un flag `TASK_SCHEDULE_ENABLED_*` (défaut: `True` pour les tâches DB, `False` pour les tâches de sync/build) pour l'activer/désactiver sans redémarrage via le panneau d'administration.

Chaque tâche possède un flag `TASK_SCHEDULE_ENABLED_*` (défaut: `True`) pour l'activer/désactiver sans redémarrage via le panneau d'administration.

## Indexeurs

### Flags d'activation serveur

| Variable | Défaut | Description |
|---|---|---|
| `C411_ENABLE` | `True` | Activer C411 |
| `TORR9_ENABLE` | `True` | Activer Torr9 |
| `LACALE_ENABLE` | `True` | Activer LaCale |
| `GENERATIONFREE_ENABLE` | `True` | Activer GenerationFree |
| `ABN_ENABLE` | `True` | Activer ABN |
| `G3MINI_ENABLE` | `True` | Activer G3mini |
| `THEOLDSCHOOL_ENABLE` | `True` | Activer TheOldSchool |
| `NOSTRADAMUS_ENABLE` | `True` | Activer Nostradamus |

??? info "Si désactivé"
    Quand un indexeur est désactivé au niveau serveur, il est masqué du panneau de configuration pour **tous** les utilisateurs, même s'ils ont leurs propres identifiants.

### Identifiants privés

!!! warning "Identifiants partagés"
    Si les identifiants d'un indexeur sont définis en variable d'environnement, ils seront utilisés par **tous les utilisateurs**. Pour une petite instance familiale, cela peut être acceptable. Pour une instance publique, laissez chaque utilisateur configurer ses propres identifiants depuis la page de configuration du plugin.

| Variable | Description |
|---|---|
| `C411_API_KEY` / `C411_PASSKEY` | Identifiants C411 |
| `TORR9_API_KEY` | Clé API Torr9 |
| `LACALE_API_KEY` | Clé API LaCale |
| `GENERATIONFREE_API_KEY` / `GENERATIONFREE_PASSKEY` | Identifiants GenerationFree |
| `ABN_API_KEY` / `ABN_PASSKEY` | Identifiants ABN |
| `G3MINI_API_KEY` / `G3MINI_PASSKEY` | Identifiants G3mini |
| `THEOLDSCHOOL_API_KEY` / `THEOLDSCHOOL_PASSKEY` | Identifiants TheOldSchool |
| `NOSTRADAMUS_API_KEY` / `NOSTRADAMUS_PASSKEY` | Identifiants Nostradamus |

### Zilean (API DMM)

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `ZILEAN_SCHEMA` | `str` | `https` | Protocole |
| `ZILEAN_HOST` | `str` | `zileanfortheweebs.midnightignite.me` | Hôte |
| `ZILEAN_PORT` | `int` | `None` | Port (défaut interne 8181) |
| `ZILEAN_MAX_WORKERS` | `int` | `4` | Workers parallèles |
| `ZILEAN_POOL_CONNECTIONS` | `int` | `10` | Connexions du pool |
| `ZILEAN_API_POOL_MAXSIZE` | `int` | `10` | Taille max du pool |
| `ZILEAN_MAX_RETRY` | `int` | `3` | Tentatives max en cas d'échec |

## TRaSH Custom Formats

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `TRASH_SCORING_ENABLED` | `bool` | `False` | Master switch du scoring (hot-reloadable) |
| `TRASH_SYNC_ENABLED` | `bool` | `True` | Active la sync planifiée du miroir |
| `TRASH_SYNC_CRON` | `str` | `0 */6 * * *` | Fréquence de sync (toutes les 6h) |
| `TRASH_MIRROR_REPO_URL` | `str` | `https://github.com/LimeHubs/streamfusion-trash-mirror.git` | URL du dépôt miroir |
| `TRASH_MIRROR_BRANCH` | `str` | `main` | Branche Git à utiliser |
| `TRASH_DEFAULT_TEMPLATE_SLUG` | `str` | `balanced` | Template par défaut si aucun n'est marqué défaut en DB |

## Nostradamus

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `NOSTRADAMUS_ENABLE` | `bool` | `True` | Master switch de l'indexeur Nostradamus |
| `NOSTRADAMUS_URL` | `str` | `https://nostradamus.foo` | URL de l'API Torznab |
| `NOSTRADAMUS_API_KEY` | `str` | `None` | Clé API Torznab |
| `NOSTRADAMUS_PASSKEY` | `str` | `None` | Passkey pour les announce URLs |
| `NOSTRADAMUS_UNIQUE_ACCOUNT` | `bool` | auto | Compte serveur unique (auto si `API_KEY` présent) |

## Administration et Développement

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `ADMIN_TEMPLATE_DIR` | `str` | `/app/stream_fusion/static/admin` | Chemin templates admin |
| `DEBUG` | `bool` | `False` | Mode debug |
| `DEVELOP` | `bool` | `False` | Mode développement |
| `RELOAD` | `bool` | `False` | Rechargement à chaud |
| `DEV_HOST` | `str` | `0.0.0.0` | Hôte dev |
| `DEV_PORT` | `int` | `8080` | Port dev |
