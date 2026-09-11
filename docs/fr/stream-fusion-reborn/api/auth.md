# Authentification API

Gestion des clés API utilisées par les clients Stremio et les applications tierces.

!!! info "Authentification requise"
    Tous les endpoints `/api/auth/*` nécessitent le header `secret-key`.

---

## Créer une clé

```
POST /api/auth/new
```

**Requête** (`APIKeyCreate`) :

| Champ | Type | Requis | Description |
|---|---|---|---|
| `name` | `string` | :fontawesome-solid-check: | Nom descriptif de la clé |
| `never_expire` | `boolean` | - | Pas de date d'expiration (défaut: `false`) |
| `proxied_links` | `boolean` | - | Proxyfier les flux debrid via le serveur (défaut: `false`) |

```bash
curl -X POST http://localhost:8080/api/auth/new \
  -H "secret-key: VOTRE_SECRET_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "ma-cle-stremio", "proxied_links": true}'
```

??? success "Réponse"
    ```json
    {
      "key": "sf_abc123...",
      "name": "ma-cle-stremio",
      "is_active": true,
      "proxied_links": true,
      "created_at": "2024-01-01T00:00:00Z"
    }
    ```

!!! danger "Secret à usage unique"
    Le secret n'est affiché **qu'une seule fois** à la création. Conservez-le précieusement.

---

## Consulter les clés

| Méthode | URL | Description |
|---|---|---|
| `GET` | `/api/auth/get/{api_key}` | Détails d'une clé |
| `GET` | `/api/auth/get_by_name/{name}` | Recherche par nom |
| `GET` | `/api/auth/list` | Liste des clés actives |
| `GET` | `/api/auth/check/{api_key}` | Vérifier si une clé est valide |

**Réponse** (`APIKeyInDB`) :

| Champ | Type | Description |
|---|---|---|
| `id` | `integer` | Identifiant interne |
| `api_key` | `UUID` | Identifiant unique de la clé |
| `is_active` | `boolean` | Si la clé est active |
| `never_expire` | `boolean` | Pas de date d'expiration |
| `expiration_date` | `datetime` ou `null` | Date d'expiration |
| `latest_query_date` | `datetime` ou `null` | Dernière utilisation |
| `total_queries` | `integer` | Nombre total de requêtes |
| `name` | `string` | Nom de la clé |
| `proxied_links` | `boolean` | Proxyfication des flux activée |

---

## Modifier les clés

| Méthode | URL | Description |
|---|---|---|
| `PUT` | `/api/auth/revoke/{api_key}` | Révoquer (désactiver sans supprimer) |
| `PUT` | `/api/auth/renew/{api_key}` | Renouveler (nouveau secret) |
| `PUT` | `/api/auth/update/{api_key}` | Mettre à jour les propriétés |
| `DELETE` | `/api/auth/delete/{api_key}` | Supprimer définitivement |
| `GET` | `/api/auth/logs` | Journaux d'utilisation |

**Requête de mise à jour** (`APIKeyUpdate`) :

| Champ | Type | Description |
|---|---|---|
| `is_active` | `boolean` ou `null` | Activer/désactiver la clé |
| `expiration_date` | `datetime` ou `null` | Nouvelle date d'expiration |
| `name` | `string` ou `null` | Nouveau nom |
| `proxied_links` | `boolean` ou `null` | Activer/désactiver la proxyfication |

---

## Journaux d'utilisation

```
GET /api/auth/logs
```

**Réponse** (`UsageLogs`) :

| Champ | Type | Description |
|---|---|---|
| `logs` | `list[UsageLog]` | Liste des journaux |

**UsageLog** :

| Champ | Type | Description |
|---|---|---|
| `api_key` | `UUID` | Identifiant de la clé |
| `name` | `string` ou `null` | Nom de la clé |
| `is_active` | `boolean` | Si la clé est active |
| `never_expire` | `boolean` | Pas d'expiration |
| `expiration_date` | `datetime` ou `null` | Date d'expiration |
| `latest_query_date` | `datetime` ou `null` | Dernière utilisation |
| `total_queries` | `integer` | Nombre total de requêtes |
| `proxied_links` | `boolean` | Proxyfication activée |

---

## Authentification Debrid

### Real-Debrid (Device Code)

```bash
# 1. Obtenir un device code
curl -X POST http://localhost:8080/api/auth/realdebrid/device_code \
  -H "secret-key: VOTRE_SECRET_API_KEY"

# 2. L'utilisateur valide sur https://real-debrid.com/device

# 3. Récupérer le token
curl -X POST http://localhost:8080/api/auth/realdebrid/token \
  -H "secret-key: VOTRE_SECRET_API_KEY"
```

### AllDebrid (PIN)

```bash
# 1. Obtenir un PIN
curl http://localhost:8080/api/auth/alldebrid/pin/get \
  -H "secret-key: VOTRE_SECRET_API_KEY"

# 2. Vérifier le PIN
curl "http://localhost:8080/api/auth/alldebrid/pin/check?checkpin=PIN&id=ID" \
  -H "secret-key: VOTRE_SECRET_API_KEY"
```