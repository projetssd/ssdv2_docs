# :material-heart-pulse: Monitoring & Configuration

## :material-heart: Health Check

```
GET /api/monitoring/health
```

Retourne `200 OK` si l'application est en bonne santé.

```bash
curl http://localhost:8080/api/monitoring/health
```

---

## :material-lock: Chiffrement de configuration

```
POST /api/config/encode
```

Chiffre une configuration utilisateur en token Fernet pour les URLs Stremio.

```bash
curl -X POST http://localhost:8080/api/config/encode \
  -H "secret-key: VOTRE_SECRET_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"debrid": "realdebrid", ...}'
```

!!! note "CSRF"
    Cet endpoint est protégé par un token CSRF en plus du header `secret-key`.

---

## :material-book-open: Documentation interactive

| URL | Description |
|---|---|
| `/api/docs` | Swagger UI |
| `/api/redoc` | ReDoc |
| `/api/openapi.json` | Schéma OpenAPI JSON |

!!! warning "Disponibilité"
    Swagger UI et ReDoc sont masqués par défaut (`SECURITY_HIDE_DOCS=True`). Activez-les uniquement en développement :

    ```env
    SECURITY_HIDE_DOCS=False
    ```