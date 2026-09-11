# :material-code-braces: Intégration externe (cache Peer)

Guide complet pour intégrer le cache Stream Fusion dans une application tierce via l'API Peer.

---

## :material-numeric-1-circle: Obtenir une PeerKey

Demandez à l'administrateur de l'instance Stream Fusion de créer une PeerKey pour votre application. Vous recevrez :

| Information | Description |
|---|---|
| `key_id` | UUID identifiant la clé |
| `secret` | Secret 256-bit hex (**affiché une seule fois**) |

!!! warning "Conserver le secret"
    Le secret n'est affiché qu'une seule fois à la création. Stockez-le de manière sécurisée.

---

## :material-numeric-2-circle: Authentifier vos requêtes

=== "Python"

    ```python
    import hmac, hashlib, json, time, requests
    
    def make_authenticated_request(
        url: str,
        key_id: str,
        secret: str,
        payload: dict
    ) -> dict:
        body = json.dumps(payload).encode()
        timestamp = int(time.time())
        
        body_hash = hashlib.sha256(body).hexdigest()
        message = f"{timestamp}.{body_hash}"
        signature = hmac.new(
            secret.encode(), message.encode(), hashlib.sha256
        ).hexdigest()
        
        headers = {
            "Content-Type": "application/json",
            "X-Peer-Key-Id": key_id,
            "X-Peer-Timestamp": str(timestamp),
            "X-Peer-Signature": signature,
        }
        
        response = requests.post(url, headers=headers, data=body)
        return response.json()
    ```

=== "cURL"

    ```bash
    #!/bin/bash
    KEY_ID="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    SECRET="$(openssl rand -hex 32)"
    TIMESTAMP=$(date +%s)
    BODY='{"query":"matrix","limit":20}'
    
    BODY_HASH=$(echo -n "$BODY" | sha256sum | cut -d' ' -f1)
    MESSAGE="${TIMESTAMP}.${BODY_HASH}"
    SIGNATURE=$(echo -n "$MESSAGE" | openssl dgst -sha256 -hmac "$SECRET" | cut -d' ' -f2)
    
    curl -X POST https://sf.example.com/api/peer/public/search \
      -H "Content-Type: application/json" \
      -H "X-Peer-Key-Id: $KEY_ID" \
      -H "X-Peer-Timestamp: $TIMESTAMP" \
      -H "X-Peer-Signature: $SIGNATURE" \
      -d "$BODY"
    ```

---

## :material-numeric-3-circle: Déchiffrer les réponses

```python
import base64, hashlib, json
from cryptography.fernet import Fernet

def derive_fernet_key(secret: str) -> bytes:
    prefix = "sf-peer-cache-v1:"
    key_material = prefix + secret
    key = hashlib.sha256(key_material.encode()).digest()
    return base64.urlsafe_b64encode(key)

def decrypt_payload(secret: str, payload: str) -> dict:
    key = derive_fernet_key(secret)
    f = Fernet(key)
    decrypted = f.decrypt(payload.encode()).decode()
    return json.loads(decrypted)
```

---

## :material-numeric-4-circle: Exemples d'utilisation

### Recherche publique (Meilisearch)

```python
result = make_authenticated_request(
    url="https://sf.example.com/api/peer/public/search",
    key_id=KEY_ID, secret=SECRET,
    payload={"query": "matrix 1080p", "limit": 20}
)
data = decrypt_payload(SECRET, result["payload"])
# data = {"hits": [...], "total_hits": 99}
```

### Recherche privée (PostgreSQL)

```python
result = make_authenticated_request(
    url="https://sf.example.com/api/peer/private/search",
    key_id=KEY_ID, secret=SECRET,
    payload={"tmdb_id": 155, "limit": 20}
)
data = decrypt_payload(SECRET, result["payload"])
# data = {"items": [...], "total": 42}
```

### Export paginé (sync)

```python
# Première page
result = make_authenticated_request(
    url="https://sf.example.com/api/peer/private/export",
    key_id=KEY_ID, secret=SECRET,
    payload={"limit": 500, "since": last_sync_timestamp}
)
data = decrypt_payload(SECRET, result["payload"])
# data = {"items": [...], "next_cursor": "abc...", "count": 500}

# Page suivante
result = make_authenticated_request(
    url="https://sf.example.com/api/peer/private/export",
    key_id=KEY_ID, secret=SECRET,
    payload={"limit": 500, "cursor": data["next_cursor"]}
)
# Continuer tant que next_cursor n'est pas null
```

### Lookup IMDB

```python
result = make_authenticated_request(
    url="https://sf.example.com/api/peer/imdb/lookup",
    key_id=KEY_ID, secret=SECRET,
    payload={"imdb_id": "tt0111161", "limit": 10}
)
data = decrypt_payload(SECRET, result["payload"])
# data = {"results": [{"imdb_id": "tt0111161", "primary_title": "The Shawshank Redemption", ...}]}
```

---

## :material-alert-circle: Gestion des erreurs

| Code | Cause | Action |
|---|---|---|
| `200` | Succès | Déchiffrer le payload |
| `400` | Requête invalide | Vérifier le corps JSON |
| `401` | Auth échouée | Vérifier headers HMAC et timestamp (±60s) |
| `403` | Clé inactive/expirée | Contacter l'admin |
| `429` | Rate limiting | Attendre et réessayer |
| `500` | Erreur serveur | Réessayer plus tard |

---

## :material-lightbulb-on: Bonnes pratiques

- [ ] **Cachez les résultats** localement pour réduire les appels API
- [ ] **Utilisez `since` + `cursor`** pour la sync incrémentale (seul le delta)
- [ ] **Respectez le rate limiting** (attendre en cas de `429`)
- [ ] **Stockez le secret** dans un gestionnaire de secrets, jamais en clair dans le code
- [ ] **Planifiez une rotation** régulière des PeerKeys