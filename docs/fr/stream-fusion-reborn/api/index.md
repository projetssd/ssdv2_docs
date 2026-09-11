# :material-api: API

Stream Fusion expose plusieurs ensembles d'endpoints REST via FastAPI.

---

## :material-sitemap: Vue d'ensemble

<div class="grid cards" markdown>

-   :material-television: **Stremio** `/`

    Endpoints addon : manifest, streams, catalog, meta
    
    [:material-arrow-right: Détails](stremio.md)

-   :material-key: **Auth** `/api/auth`

    Gestion clés API, auth debrid
    
    [:material-arrow-right: Détails](auth.md)

-   :material-share-variant: **Peer** `/api/peer`

    Échange de cache chiffré entre instances
    
    [:material-arrow-right: Détails](peer.md)

-   :material-heart-pulse: **Monitoring** `/api/monitoring`

    Health check, config, docs
    
    [:material-arrow-right: Détails](monitoring.md)

-   :material-shield-account: **Admin** `/admin`

    Panneau d'administration HTML (session + CSRF)

-   :material-pencil-plus: **Enregistrement** `/register`

    Auto-inscription publique (rate-limited)

</div>

---

## :material-lock: Authentification

=== ":material-key-variant: Clé API (Stremio)"

    Token Fernet encodé dans l'URL :
    
    ```
    /{config}/stream/{type}/{id}
    /{config}/manifest.json
    ```

=== ":material-shield-lock: Clé secrète (API JSON)"

    Header `secret-key` avec `SECRET_API_KEY` :
    
    ```bash
    curl -H "secret-key: votre-secret-api-key" \
      http://localhost:8080/api/auth/list
    ```

=== ":material-fingerprint: HMAC-SHA256 (Peer)"

    3 headers : `X-Peer-Key-Id`, `X-Peer-Timestamp`, `X-Peer-Signature`
    
    Voir [Peering - Sécurité](../peering/securite.md)

=== ":material-cookie: Session (Admin)"

    Cookie de session Starlette + CSRF pour les formulaires POST

---

## :material-book-open: Documentation interactive

| URL | Condition |
|---|---|
| `/api/docs` | `SECURITY_HIDE_DOCS=False` |
| `/api/redoc` | `SECURITY_HIDE_DOCS=False` |
| `/api/openapi.json` | Toujours accessible |

!!! warning "Sécurité"
    `SECURITY_HIDE_DOCS` est `True` par défaut en production. Passez-le à `False` uniquement en développement.