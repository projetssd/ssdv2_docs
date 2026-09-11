# :material-sitemap: Indexeurs

Stream Fusion intègre plusieurs **indexeurs francophones** pour la recherche de torrents. Chaque indexeur peut être activé/désactivé globalement.

---

## :material-format-list-bulleted: Types d'indexeurs

<div class="grid cards" markdown>

-   :material-api: **Torznab**

    API standardisée, facile à intégrer
    
    C411, Torr9, LaCale, Jackett

-   :material-web: **API propriétaires**

    API REST spécifiques à chaque tracker (pas du scraping)
    
    ABN, GenerationFree, G3mini, TheOldSchool

-   :material-crystal-ball: **Torznab privé**

    8ème indexeur privé francophone supplémentaire
    
    Nostradamus (pattern standard 3 fichiers)

-   :material-cloud-download: **API DMM**

    API Debrid Media Manager
    
    Zilean

-   :material-swap-vertical: **Nostr (NIP-35)**

    Relay décentralisés
    
    U2P / Utopeer

-   :material-database: **Cache Public Local**

    Cache Meilisearch partagé entre utilisateurs
    
    MeiliCache

</div>

---

## :material-layers: Architecture : indexeurs publics vs privés

Stream Fusion distingue deux catégories d'indexeurs avec des stratégies de persistance différentes :

<div class="grid cards" markdown>

-   :material-earth: **Indexeurs publics**

    **Aucun stockage PostgreSQL** — les résultats sont éphémères et recherchés à la volée.
    
    Interrogés en premier (plus rapides, résultats cachés). Les données pertinentes sont indexées dans Meilisearch pour le partage entre utilisateurs.
    
    *Zilean, Jackett, MeiliCache, UtoPeer*

-   :material-lock: **Indexeurs privés**

    Résultats **persistés dans PostgreSQL** pour optimiser les recherches ultérieures.
    
    Chaque indexeur suit un **pattern en 3 fichiers** :
    
    | Fichier | Rôle |
    |---|---|
    | `_api.py` | Client HTTP pour l'API du tracker |
    | `_result.py` | Dataclass pour les résultats parsés |
    | `_service.py` | Logique métier, cache, persistance DB |
    
    *C411, Torr9, LaCale, GenerationFree, ABN, G3mini, TheOldSchool, Nostradamus*

</div>

---

## :material-toggle-switch: Activation serveur

Chaque indexeur a un flag `*_ENABLE` contrôlant sa disponibilité pour **tous** les utilisateurs :

```env
# Désactiver un indexeur pour tout le monde
C411_ENABLE=False
TORR9_ENABLE=False

# Activer (défaut)
ABN_ENABLE=True
```

!!! warning "Impact global"
    Si un indexeur est désactivé au niveau serveur, il est **masqué** du panneau de configuration utilisateur, même si l'utilisateur possède ses propres identifiants.

---

## :material-format-list-numbered: Indexeurs

### C411

```env
C411_ENABLE=True                    # Activation serveur
C411_API_KEY=votre-cle-api          # Clé API Torznab
C411_PASSKEY=votre-passkey          # Passkey announce
```

### Torr9

```env
TORR9_ENABLE=True
TORR9_API_KEY=votre-cle-api
```

### LaCale

```env
LACALE_ENABLE=True
LACALE_API_KEY=votre-cle-api
```

### GenerationFree

```env
GENERATIONFREE_ENABLE=True
GENERATIONFREE_API_KEY=votre-cle-api
GENERATIONFREE_PASSKEY=votre-passkey
```

### ABN (Abnormal)

```env
ABN_ENABLE=True
ABN_API_KEY=votre-cle-api
ABN_PASSKEY=votre-passkey
```

### G3mini (Gemini Tracker)

```env
G3MINI_ENABLE=True
G3MINI_API_KEY=votre-cle-api
G3MINI_PASSKEY=votre-passkey
```

### TheOldSchool

```env
THEOLDSCHOOL_ENABLE=True
THEOLDSCHOOL_API_KEY=votre-cle-api
THEOLDSCHOOL_PASSKEY=votre-passkey
```

### Nostradamus

```env
NOSTRADAMUS_ENABLE=True
NOSTRADAMUS_API_KEY=votre-cle-api
NOSTRADAMUS_PASSKEY=votre-passkey
```

Nostradamus est le **8ème indexeur privé** du catalogue Stream Fusion. Il s'agit d'un indexeur Torznab francophone supplémentaire qui suit le pattern standard en 3 fichiers (`nostradamus_api.py`, `nostradamus_result.py`, `nostradamus_service.py`).

**Sécurité des URLs de téléchargement** : comme pour les autres indexeurs privés, les credentials (clé API) sont **strippés des URLs de téléchargement** avant le stockage en base PostgreSQL. Les URLs sont nettoyées (paramètre `apikey` retiré) et les credentials sont **réinjectés au moment de servir** le lien à l'utilisateur. Cette séparation garantit que :

- La base PostgreSQL ne contient jamais de clés API en clair dans les colonnes de liens
- Les credentials restent confinés aux variables d'environnement
- Un dump PostgreSQL ne divulgue pas accidentellement les clés API Nostradamus

**Pattern Torznab standard** : Nostradamus expose une API Torznab classique (`/api?t=movie|tvsearch&q=...&apikey=...`), supportant la recherche par IMDB ID (films) et par mots-clés (films + séries). La réponse XML est parsée pour extraire les attributs Torznab (`seeders`, `size`, `magneturl`, `tmdbid`).

### Zilean (API DMM)

```env
ZILEAN_SCHEMA=https
ZILEAN_HOST=zileanfortheweebs.midnightignite.me
ZILEAN_PORT=8181
ZILEAN_MAX_WORKERS=4
ZILEAN_POOL_CONNECTIONS=10
ZILEAN_API_POOL_MAXSIZE=10
ZILEAN_MAX_RETRY=3
```

Zilean interroge l'API Debrid Media Manager pour rechercher des torrents publics déjà connus du réseau DMM. Contrairement aux indexeurs classiques, il ne scrape pas de trackers mais interroge une base de hashlists pré-indexée.

### Jackett (optionnel)

```env
JACKETT_HOST=jackett
JACKETT_PORT=9117
JACKETT_API_KEY=votre-cle-jackett
```

!!! note "Activation automatique"
    Jackett est activé automatiquement si `JACKETT_API_KEY` est défini.

### Cache Public Local (MeiliCache)

```env
MEILI_CACHE_ENABLE=True
```

Le **Cache Public Local** utilise Meilisearch pour stocker et partager les résultats de recherche entre tous les utilisateurs de l'instance. Quand un utilisateur recherche un contenu, les résultats sont indexés dans Meilisearch et deviennent immédiatement disponibles pour les autres utilisateurs sans nouvel appel aux indexeurs.

!!! tip "Priorité Phase 1"
    Dans la configuration utilisateur, `meiliCachePriority=True` place le Cache Public en **Phase 1** (interrogé en priorité). Sinon il est utilisé en **Phase 4** (fallback public).

---

## :material-sitemap-outline: Synchronisation DMM

La sync DMM clone le dépôt GitHub et indexe les torrents publics dans Meilisearch :

```env
DMM_SYNC_ENABLED=True            # Master switch
DMM_SYNC_SCHEDULE_ENABLED=False   # Cron auto (désactivé par défaut)
DMM_SYNC_CRON=0 2 * * *         # Quotidien à 2h
```

## :material-swap-vertical: U2P / Utopeer (Nostr NIP-35)

Synchronisation via relais Nostr décentralisés :

```env
U2P_SYNC_ENABLED=False            # Master switch
U2P_SYNC_SCHEDULE_ENABLED=False   # Cron auto
U2P_SYNC_CRON=0 3 * * 0         # Dimanche à 3h

UTOPEER_RELAY_TIMEOUT=8           # Timeout par requête (s)
```