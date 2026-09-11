# Fichiers d'environnement

La configuration repose sur **deux fichiers** placés dans le même répertoire que votre `docker-compose.yml` :

| Fichier | Rôle | Obligatoire |
|---|---|---|
| `.env` | Secrets et réglages de déploiement | Oui |
| `user.env` | Comptes partagés debrid / indexeurs | Non — uniquement en mode `unique_account` |

Le fichier `.env` est chargé automatiquement par Docker Compose pour la substitution `${VAR}` dans le YAML.
Le fichier `user.env` est injecté dans les containers `stream-fusion` et `taskiq-worker` via `env_file:` uniquement si vous l'activez (voir ci-dessous).

---

## Générer des clés secrètes

=== "Linux / Mac"

    ```bash
    # Clé secrète (SECRET_API_KEY, MEILI_MASTER_KEY)
    openssl rand -hex 32

    # Clé Fernet (CONFIG_SECRET_KEY)
    python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

    # Mot de passe PostgreSQL
    openssl rand -hex 16
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Clé secrète
    -join ((1..64) | ForEach-Object { [char](Get-Random -Minimum 33 -Maximum 126) })

    # UUID pour SECRET_API_KEY
    [guid]::NewGuid().ToString()

    # Mot de passe PostgreSQL
    -join ((1..32) | ForEach-Object { [char](Get-Random -Minimum 33 -Maximum 126) })
    ```

---

## Fichier `.env`

Créez un fichier `.env` dans votre répertoire de déploiement et copiez-y le contenu ci-dessous :

```env title=".env — Template"
# ─── Secrets obligatoires ────────────────────────────────────────────────────
SECRET_API_KEY=générer-avec-openssl-rand-hex-32
ADMIN_SECRET_KEY=générer-avec-openssl-rand-hex-32
CONFIG_SECRET_KEY=générer-avec-Fernet-generate_key
TMDB_API_KEY=votre-cle-api-tmdb
MEILI_MASTER_KEY=générer-avec-openssl-rand-hex-32

# ─── Base de données ─────────────────────────────────────────────────────────
# Utiliser trois mots de passe PostgreSQL distincts.
POSTGRES_PASSWORD=générer-avec-openssl-rand-hex-32
PG_PASS=générer-avec-openssl-rand-hex-32
PG_MIGRATION_PASS=générer-avec-openssl-rand-hex-32

# ─── Réglages de déploiement ─────────────────────────────────────────────────
TZ=Europe/Paris
USE_HTTPS=true
PROXY_URL=http://warp:1080

# ─── Production uniquement ───────────────────────────────────────────────────
# DOMAIN=stream.votredomaine.com
```

### Variables obligatoires

| Variable | Description | Génération |
|---|---|---|
| `SECRET_API_KEY` | Authentification API | `openssl rand -hex 32` |
| `ADMIN_SECRET_KEY` | Authentification de l'administration | `openssl rand -hex 32` |
| `CONFIG_SECRET_KEY` | Clé active de chiffrement des tokens de config | `Fernet.generate_key()` |
| `CONFIG_SECRET_KEY_PREVIOUS` | **Avancé — rotation uniquement.** Ancienne clé temporaire de déchiffrement | Ne pas ajouter au `.env` d'une installation neuve |
| `TMDB_API_KEY` | Clé API TheMovieDB | [tmdb.org/settings/api](https://www.themoviedb.org/settings/api) |
| `MEILI_MASTER_KEY` | Clé maîtresse Meilisearch | `openssl rand -hex 32` |
| `POSTGRES_PASSWORD` | Bootstrap PostgreSQL | `openssl rand -hex 32` |
| `PG_PASS` | Accès PostgreSQL normal de l'application | `openssl rand -hex 32` |
| `PG_MIGRATION_PASS` | Migrations automatiques du schéma | `openssl rand -hex 32` |

---

## Fichier `user.env` — Mode unique_account

Ce fichier est **optionnel**. Il ne sert que si vous souhaitez qu'un compte debrid ou une clé d'indexeur soit **partagé entre tous les utilisateurs** de l'instance.

!!! warning "Compte serveur vs compte personnel"
    Quand un token est défini dans `user.env`, il est utilisé pour **tous les utilisateurs** de l'instance sans exception. Pour une petite instance familiale, c'est acceptable. Pour une instance publique, **c'est fortement déconseillé** : les services debrid sont à bas coût individuellement et un compte partagé par de nombreux utilisateurs risque d'être banni.

    Préférez laisser chaque utilisateur configurer son propre service depuis la page de configuration du plugin Stremio.

**Pourquoi deux containers ?** Le worker Taskiq s'exécute dans un container séparé. Si vous configurez un debrid global, le `user.env` garantit que les tâches de fond (refresh, préfetch) utilisent les mêmes credentials que le container web.

### Activation

1. Créez un fichier `user.env` dans votre répertoire de déploiement (voir le template plus bas dans cette page)
2. Décommentez les tokens/clés souhaités dans `user.env`
3. Activez l'injection dans `docker-compose.yml` en décommentant les lignes `env_file: user.env` sur les services `stream-fusion` et `taskiq-worker`

### Debrid

=== "AllDebrid (recommandé)"

    ```env
    AD_TOKEN=votre-token-alldebrid
    ```

=== "TorBox"

    ```env
    TB_TOKEN=votre-token-torbox
    ```

=== "Premiumize"

    ```env
    PM_TOKEN=votre-token-premiumize
    ```

=== "Real-Debrid (déconseillé)"

    ```env
    RD_TOKEN=votre-token-real-debrid
    ```

    !!! danger "Service en fin de vie"
        Real-Debrid est déconseillé : cache FR pauvre, résultats fréquemment incorrects, API restrictive. Le support est maintenu pour les comptes existants uniquement.

=== "Autres"

    ```env
    DL_TOKEN=votre-token-debrid-link
    ED_TOKEN=votre-token-easydebrid
    OC_CREDENTIALS=email:password
    PP_CREDENTIALS=email:password
    ```

### Indexeurs privés

```env
C411_API_KEY=votre-cle-c411
TORR9_API_KEY=votre-cle-torr9
LACALE_API_KEY=votre-cle-lacale
GENERATIONFREE_API_KEY=votre-cle-generationfree
ABN_API_KEY=votre-cle-abn
G3MINI_API_KEY=votre-cle-g3mini
THEOLDSCHOOL_API_KEY=votre-cle-theoldschool
NOSTRADAMUS_API_KEY=votre-cle-nostradamus
```

### Template complet `user.env`

Créez un fichier `user.env` dans votre répertoire de déploiement et copiez-y le contenu ci-dessous :

```env title="user.env — Template"
# =============================================================================
# user.env — Comptes partagés (mode unique_account)
#
# Décommentez les services que vous souhaitez activer.
# Quand un token est défini ici, il est utilisé pour TOUS les utilisateurs.
#
# Activez l'injection dans docker-compose.yml en décommentant les lignes
# "env_file: user.env" sur les services stream-fusion et taskiq-worker.
# =============================================================================


# ── Services debrid ───────────────────────────────────────────────────────────
# ATTENTION : partagé par TOUS les utilisateurs de l'instance.

# AD_TOKEN=votre-token-alldebrid
# TB_TOKEN=votre-token-torbox
# PM_TOKEN=votre-token-premiumize
# DL_TOKEN=votre-token-debrid-link
# ED_TOKEN=votre-token-easydebrid
# OC_CREDENTIALS=email:password       # Offcloud
# PP_CREDENTIALS=email:password       # PikPak

# Real-Debrid — token OAuth2 bearer (support unique_account limité, déconseillé)
# RD_TOKEN=votre-token-realdebrid


# ── Clés API indexeurs privés ─────────────────────────────────────────────────
# Quand définies, tous les utilisateurs accèdent à ces indexeurs sans credentials.

# C411_API_KEY=votre-cle-c411
# TORR9_API_KEY=votre-cle-torr9
# LACALE_API_KEY=votre-cle-lacale
# GENERATIONFREE_API_KEY=votre-cle-generationfree
# ABN_API_KEY=votre-cle-abn
# G3MINI_API_KEY=votre-cle-g3mini
# THEOLDSCHOOL_API_KEY=votre-cle-theoldschool
# NOSTRADAMUS_API_KEY=votre-cle-nostradamus
```

---

## Proxy

Par défaut, `PROXY_URL=http://warp:1080` dans `.env` pointe vers le container Cloudflare WARP inclus dans la stack. Les debrideurs bloquent parfois les IPs de datacenter ; WARP contourne ce problème.

```env
# Proxy pour les requêtes API vers les debrideurs (dans .env)
PROXY_URL=http://warp:1080

# Proxifier également les liens de streaming — utilise plus de bande passante (optionnel)
# PLAYBACK_PROXY=http://warp:1080
```

Voir la page [Proxy](../configuration/proxy.md) pour les détails sur `PROXIED_LINK`, `PROXY_URL` et `PLAYBACK_PROXY`.

---

## Pour aller plus loin

Pour la liste exhaustive de toutes les variables, consultez la page [Variables d'environnement](../configuration/variables-environnement.md).
