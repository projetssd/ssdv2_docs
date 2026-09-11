# :material-floor-plan: Architecture

Stream Fusion est une application FastAPI avec un système de cache multi-couches, des workers distribués et un mécanisme de peering crypté.

---

## :material-sitemap: Vue d'ensemble

```mermaid
graph TB
 Internet["Internet"]
 Traefik["Traefik<br/>TLS + Sticky"]
 
 subgraph App["Stream Fusion ×4"]
 SF["FastAPI<br/>Port 8080"]
 end
 
 subgraph Data["Services de données"]
 PG[(" PostgreSQL 17<br/>+ PgBouncer")]
 Redis[(" Redis 7<br/>Cache + Broker")]
 Meili[(" Meilisearch<br/>Full-text")]
 end
 
 subgraph BG["Tâches de fond"]
 TQW["Workers ×2"]
 TQS["Scheduler ×1"]
 end
 
 WARP["WARP<br/>SOCKS5"]
 
 Internet --> Traefik
 Traefik -->|Sticky| App
 App --- PG
 App --- Redis
 App --- Meili
 BG --- PG
 BG --- Redis
 BG --- Meili
 App -.->|optionnel| WARP
 
 style App fill:#311b92,color:#fff
 style Data fill:#1b5e20,color:#fff
 style BG fill:#bf360c,color:#fff
 style WARP fill:#e65100,color:#fff
```

---

## :material-swap-vertical: Flux d'une requête Stremio

```mermaid
graph TD
 A["Requête Stremio"] --> B{" L1: Redis<br/>~1ms"}
 B -->|Hit| Z["Réponse"]
 B -->|Miss| C{" L2: PostgreSQL<br/>~5ms"}
 C -->|Suffisant| Z
 C -->|Insuffisant| D["L3: Meilisearch<br/>~10ms"]
 D --> E["L4: Indexeurs privés<br/>~1-10s"]
 E --> F["Fusion + Filtrage"]
 F --> G["Vérif. Debrid"]
 G --> H["Mise en cache"]
 H --> Z
 
 style A fill:#311b92,color:#fff
 style Z fill:#1b5e20,color:#fff
```

---

## :material-view-list: Couches de données

<div class="grid cards" markdown>

-   :material-memory: **L1 : Redis**

    Cache hot, latence ~1ms, TTL 7 jours
    
    Résultats de recherche, streams, métadonnées

-   :material-database: **L2 : PostgreSQL**

    Persistance, requêtes structurées
    
    Torrents avec métadonnées, clés, config

-   :material-magnify: **L3 : Meilisearch**

    Recherche full-text, latence ~10ms
    
    Torrents publics indexés (DMM, Zilean, peers)

-   :material-database: **L4 : DuckDB**

    Base locale analytique, matching IMDB
    
    Voir [Cache et bases de données](../cache/index.md) pour les détails

</div>

---

## :material-cog-sync: Workers et scheduler

| Composant | Réplicas | Rôle |
|---|---|---|
| :material-web: **Stream Fusion** | 4 | Application FastAPI |
| :material-cog: **Taskiq Worker** | 2+ | Exécution des tâches de fond |
| :material-timer: **Taskiq Scheduler** | **1** | Planification cron |

!!! danger "Scheduler unique"
    Le scheduler doit toujours être en exactement **1 replica**. Scaler cause des tâches en double.

---

## :material-arrow-right: Sections détaillées

<div class="grid cards" markdown>

-   :material-magnify: **[Pipeline de recherche](pipeline-recherche.md)**
    
    Flux de recherche détaillé, filtrage, préchargement

-   :material-cog-sync: **[Tâches distribuées](taches-distribuees.md)**
    
    Workers Taskiq, scheduler, tâches cron, planification dynamique

-   :material-tune-variant: **[Système de configuration](systeme-configuration.md)**
    
    Configuration 2-couches : variables d'environnement + surcharges PostgreSQL

-   :fontawesome-solid-code: **[Conventions de code](conventions-code.md)**
    
    Async I/O obligatoire, logging Loguru, Redis DBs, conventions de nommage

-   :material-code-braces: **[Parsing RTN](parsing-rtn.md)**
    
    Double pipeline de parsing RTN (Meilisearch + PostgreSQL) avec règles DB-backed

-   :material-movie-search: **[Matching IMDB/TMDB](matching-imdb-tmdb.md)**
    
    Matchers PostgreSQL avec historique, batch processing et retry