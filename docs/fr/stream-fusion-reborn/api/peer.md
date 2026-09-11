# API Peer

L'API Peer permet à des instances Stream Fusion distantes de **partager leurs torrents privés** de manière sécurisée. L'instance source exporte depuis PostgreSQL (base privée), l'instance cible insère dans Meilisearch (base publique). Pour l'intégration depuis une application tierce, voir [Intégration externe](../peering/integration-externe.md).

!!! info "Authentification HMAC-SHA256"
    Tous les endpoints nécessitent 3 headers : `X-Peer-Key-Id`, `X-Peer-Timestamp`, `X-Peer-Signature`. Voir [Sécurité](../peering/securite.md).

---

## Endpoints

### Vérification de cache Debrid

```
POST /api/peer/debrid/check
```

Vérifie la disponibilité de hashes sur un service debrid.

**Requête** (`PeerDebridCheckRequest`) :

| Champ | Type | Contrainte | Description |
|---|---|---|---|
| `hashes` | `list[string]` | 1-200 items | Info-hashes à vérifier |
| `service` | `string` | `realdebrid` / `alldebrid` / `torbox` | Service cible |

```json
{
  "hashes": ["abc123...", "def456..."],
  "service": "alldebrid"
}
```

**Réponse** (`PeerDebridCheckResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge utile chiffrée Fernet contenant `{"service": str, "debrid_cache": {hash: dict}}` |

---

### Recherche d'items par hashes

```
POST /api/peer/private/items
```

Récupère les items torrent correspondants aux hashes fournis.

**Requête** (`PeerPrivateItemsRequest`) :

| Champ | Type | Contrainte | Description |
|---|---|---|---|
| `hashes` | `list[string]` | 1-200 items | Info-hashes à rechercher |

**Réponse** (`PeerPrivateItemsResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge utile chiffrée Fernet contenant `{"torrent_items": {hash: TorrentItemOut}}` |

**TorrentItemOut** (modèle interne dans le payload chiffré) :

| Champ | Type | Description |
|---|---|---|
| `info_hash` | `string` | Hash du torrent |
| `raw_title` | `string` | Titre brut |
| `size` | `integer` | Taille en octets |
| `languages` | `list[string]` | Langues détectées |
| `seeders` | `integer` | Nombre de seeders |
| `indexer` | `string` ou `null` | Indexeur source |
| `type` | `string` ou `null` | Type (movie/series) |
| `imdb_id` | `string` ou `null` | ID IMDB |
| `tmdb_id` | `integer` ou `null` | ID TMDB |
| `created_at` | `integer` | Timestamp Unix |

---

### Recherche privée (PostgreSQL)

```
POST /api/peer/private/search
```

Recherche dans la base privée PostgreSQL. Exactement **un** champ de recherche requis.

**Requête** (`PeerPrivateSearchRequest`) :

| Champ | Type | Contrainte | Description |
|---|---|---|---|
| `query` | `string` ou `null` | ILIKE full-text | Recherche par titre |
| `tmdb_id` | `integer` ou `null` | Exact | Recherche par ID TMDB |
| `imdb_id` | `string` ou `null` | Exact | Recherche par ID IMDB |
| `info_hash` | `string` ou `null` | Exact | Recherche par hash unique |
| `limit` | `integer` | 1-200 (défaut: 20) | Résultats max |
| `offset` | `integer` | ≥ 0 (défaut: 0) | Pagination |

!!! warning "Validation"
    Le modèle exige exactement **un** des champs `query`, `tmdb_id`, `imdb_id` ou `info_hash`.

=== "Par titre"

    ```json
    { "query": "matrix", "limit": 20, "offset": 0 }
    ```

=== "Par TMDB ID"

    ```json
    { "tmdb_id": 155, "limit": 20, "offset": 0 }
    ```

=== "Par IMDB ID"

    ```json
    { "imdb_id": "tt0111161", "limit": 20, "offset": 0 }
    ```

=== "Par hash"

    ```json
    { "info_hash": "abc123def456...", "limit": 1, "offset": 0 }
    ```

**Réponse** (`PeerPrivateSearchResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge chiffrée contenant `{"items": [TorrentItemOut], "total": int}` |

---

### Export paginé (sync)

```
POST /api/peer/private/export
```

Export incrémental pour la synchronisation entre instances.

**Requête** (`PeerPrivateExportRequest`) :

| Champ | Type | Contrainte | Description |
|---|---|---|---|
| `since` | `integer` ou `null` | Timestamp Unix | Filtrer `created_at > since` |
| `cursor` | `string` ou `null` | - | Dernier hash reçu (keyset pagination) |
| `limit` | `integer` | 1-2000 (défaut: 500) | Résultats max |

```json
{
  "since": 1704067200,
  "cursor": null,
  "limit": 500
}
```

**Réponse** (`PeerPrivateExportResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge chiffrée contenant `{"items": [PeerExportItemOut], "next_cursor": str|null, "count": int}` |

**PeerExportItemOut** (sous-ensemble sûr, sans indexer/link/trackers) :

| Champ | Type | Description |
|---|---|---|
| `info_hash` | `string` | Hash du torrent |
| `raw_title` | `string` | Titre brut |
| `size` | `integer` | Taille en octets |
| `type` | `string` ou `null` | Type (movie/series) |
| `imdb_id` | `string` ou `null` | ID IMDB |
| `tmdb_id` | `integer` ou `null` | ID TMDB |
| `parsed_data` | `dict` ou `null` | Données parsées |
| `created_at` | `integer` | Timestamp Unix |

---

### Recherche publique (Meilisearch)

```
POST /api/peer/public/search
```

Recherche full-text dans les torrents publics (Meilisearch). Au moins un de `query` ou `imdb_id` requis.

**Requête** (`PeerPublicSearchRequest`) :

| Champ | Type | Contrainte | Description |
|---|---|---|---|
| `query` | `string` ou `null` | - | Recherche full-text |
| `imdb_id` | `string` ou `null` | - | Recherche par ID IMDB |
| `limit` | `integer` | 1-200 (défaut: 20) | Résultats max |
| `offset` | `integer` | ≥ 0 (défaut: 0) | Pagination |

```json
{
  "query": "matrix 1080p",
  "limit": 20,
  "offset": 0
}
```

**Réponse** (`PeerPublicSearchResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge chiffrée contenant `{"hits": [MeiliTorrentOut], "total_hits": int}` |

**MeiliTorrentOut** (document Meilisearch) :

| Champ | Type | Description |
|---|---|---|
| `hash` | `string` | Hash du torrent |
| `raw_title` | `string` | Titre brut |
| `type` | `string` ou `null` | Type |
| `size` | `integer` ou `null` | Taille en octets |
| `year` | `integer` ou `null` | Année |
| `resolution` | `string` ou `null` | Résolution |
| `languages` | `list[string]` ou `null` | Langues |
| `imdb_id` | `string` ou `null` | ID IMDB |
| `tmdb_id` | `integer` ou `null` | ID TMDB |
| `hash_source` | `string` ou `null` | Source (DMM, Peer, etc.) |
| `quality` | `string` ou `null` | Qualité vidéo |
| `codec` | `string` ou `null` | Codec |
| `audio` | `string` ou `null` | Format audio |
| `hdr` | `list[string]` ou `null` | Types HDR |

---

### Lookup IMDB (DuckDB)

```
POST /api/peer/imdb/lookup
```

Recherche dans la base IMDB locale. Au moins un de `imdb_id` ou `query` requis.

**Requête** (`PeerImdbRequest`) :

| Champ | Type | Contrainte | Description |
|---|---|---|---|
| `imdb_id` | `string` ou `null` | Exact | ID IMDB (ex: `tt0111161`) |
| `query` | `string` ou `null` | - | Recherche par titre |
| `limit` | `integer` | 1-50 (défaut: 10) | Résultats max |

```json
{
  "imdb_id": "tt0111161",
  "limit": 10
}
```

**Réponse** (`PeerImdbResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge chiffrée contenant `{"results": [ImdbTitleOut]}` |

**ImdbTitleOut** :

| Champ | Type | Description |
|---|---|---|
| `imdb_id` | `string` | ID IMDB |
| `title_type` | `string` ou `null` | Type (movie, series, etc.) |
| `primary_title` | `string` | Titre principal |
| `original_title` | `string` ou `null` | Titre original |
| `start_year` | `integer` ou `null` | Année de début |
| `average_rating` | `float` ou `null` | Note moyenne |
| `num_votes` | `integer` ou `null` | Nombre de votes |
| `tmdb_id` | `integer` ou `null` | ID TMDB correspondant |

---
    
## :material-database-export: Transfert de dumps DB

Ces endpoints permettent aux instances pair de partager leurs sauvegardes de bases de données (DuckDB et Meilisearch). Les dumps PostgreSQL ne sont **jamais** exposés via le peer — ils contiennent des secrets d'instance.

### Statut de base de données

```
POST /api/peer/db/{db_type}/status
```

Vérifie si une base de données est prête et disponible sur l'instance pair.

**Paramètres d'URL** :

| Paramètre | Type | Description |
|---|---|---|
| `db_type` | `string` | `duckdb` ou `meilisearch` |

**Réponse** (`PeerDbStatusResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge chiffrée Fernet contenant `{"ready": bool, "stats": {...}}` |

Les `stats` varient selon le type :
- **DuckDB** : `akas_count`, `basics_count`, `ratings_count`, `mapping_count`, `db_size_mb`
- **Meilisearch** : nombre de documents par index, taille de la base

---

### Liste des dumps disponibles

```
POST /api/peer/db/{db_type}/dumps
```

Liste les dumps disponibles pour un type de base de données, avec les statistiques live.

**Paramètres d'URL** :

| Paramètre | Type | Description |
|---|---|---|
| `db_type` | `string` | `duckdb` ou `meilisearch` |

**Réponse** (`PeerDbDumpsResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge Fernet contenant `{"dumps": [...], "db_stats": {...}}` |

Chaque entrée de `dumps` contient :

| Champ | Type | Description |
|---|---|---|
| `id` | `string` | Identifiant du dump (timestamp `YYYY-MM-DD_HH-MM`) |
| `filename` | `string` | Nom du fichier (ex: `2026-04-27_04-00.tar.gz`) |
| `created_at` | `integer` | Timestamp Unix de création |
| `size_bytes` | `integer` | Taille en octets |
| `sha256` | `string` | Empreinte SHA-256 du fichier |
| `db_stats` | `object` | Statistiques de la base au moment du dump |

---

### Demande de téléchargement

```
POST /api/peer/db/{db_type}/dump/download
```

Échange un `dump_id` contre un token de téléchargement à usage unique.

**Requête** (`PeerDbDumpDownloadRequest`) :

| Champ | Type | Description |
|---|---|---|
| `dump_id` | `string` | Identifiant du dump (depuis `/dumps`) |

```json
{
  "dump_id": "2026-04-27_04-00"
}
```

**Réponse** (`PeerDbDumpDownloadResponse`) :

| Champ | Type | Description |
|---|---|---|
| `payload` | `string` | Charge Fernet contenant `{"token": "...", "size": N, "sha256": "...", "expires_in": N}` |

Le token est stocké dans Redis DB5 avec un TTL configurable (`DB_DUMP_TOKEN_TTL`, défaut 600s).

---

### Téléchargement du fichier

```
GET /api/peer/db/{db_type}/dump/download/{token}
```

Télécharge le fichier de dump. Le token est à **usage unique** — GETDEL atomique garantit qu'un seul téléchargement est possible par token.

**Paramètres d'URL** :

| Paramètre | Type | Description |
|---|---|---|
| `db_type` | `string` | `duckdb` ou `meilisearch` |
| `token` | `string` | Token obtenu via `/dump/download` |

**Réponse** : StreamingResponse binaire (`application/gzip`) avec headers `Content-Disposition` et `Content-Length`.

**Codes d'erreur** :

| Code | Description |
|---|---|
| `200` | :fontawesome-solid-check: Streaming du fichier |
| `403` | :fontawesome-solid-xmark: `db_type` du token ne correspond pas |
| `404` | :fontawesome-solid-xmark: Token invalide, expiré ou déjà utilisé |
| `404` | :fontawesome-solid-xmark: Fichier dump introuvable sur le disque |

!!! warning "Token à usage unique"
    Le token est invalidé atomiquement (Redis `GETDEL`) lors du premier accès. Si le téléchargement échoue en cours de route, il faut redemander un nouveau token via `/dump/download`.

---

### Pull depuis un pair

```
POST /api/peer/db/{db_type}/pull
```

Déclenche un pull de dump depuis un pair (réservé à l'usage interne/admin).

Ce endpoint est orchestré par la tâche `db_peer_pull` dans `tasks/db_tasks.py` qui :
1. Récupère les credentials du pair depuis PostgreSQL
2. Appelle `/dump/download` pour obtenir un token
3. Télécharge le fichier via `/dump/download/{token}`
4. Vérifie l'intégrité SHA-256
5. Importe (DuckDB) ou stage (Meilisearch) le dump

---

## Sécurité et Rate limiting

!!! info "Rate limiting par clé"
    | Paramètre | Défaut | Description |
    |---|---|---|
    | `rate_limit` | 60 | Max requêtes par fenêtre |
    | `rate_window` | 60 | Durée de la fenêtre (s) |

### Codes d'erreur

| Code | Description |
|---|---|
| `200` | :fontawesome-solid-check: Succès (payload Fernet chiffré) |
| `400` | :fontawesome-solid-xmark: Requête invalide |
| `401` | :fontawesome-solid-xmark: Auth HMAC manquante/invalide |
| `403` | :fontawesome-solid-xmark: Clé inactive/expirée |
| `429` | :fontawesome-solid-xmark: Rate limiting dépassé |
| `500` | :fontawesome-solid-xmark: Erreur interne |