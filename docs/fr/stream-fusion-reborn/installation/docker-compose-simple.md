# Déploiement instance unique

Configuration simple pour un déploiement mono-instance, sans Traefik ni PgBouncer. Adapté pour un usage personnel ou un petit groupe.

!!! tip "Pour commencer"
    C'est la configuration recommandée pour un premier déploiement. Passez à la [configuration scalable](docker-compose-prod.md) uniquement si vous avez besoin de haute disponibilité.

---

## Différences avec la production scalable

| Aspect | Instance unique | Production scalable |
|---|---|---|
| PgBouncer | Non | Oui |
| Traefik | Non (ports exposés) | Oui (reverse-proxy + TLS) |
| Replicas app | 1 | 4 |
| Replicas worker | 1 | 2 |
| Sécurité Docker | Standard | `read_only`, `cap_drop ALL` |
| WARP proxy | Non | Oui (optionnel) |
| Sticky sessions | Non | Oui |

---

## Lancement

```bash
# 1. Créer le répertoire
mkdir stream-fusion && cd stream-fusion

# 2. Créer le .env (voir la page Environnement pour le template complet)
nano .env

# 3. (Optionnel) Créer user.env pour le mode unique_account (debrid/indexeurs partagés)
# nano user.env

# 4. Créer le docker-compose.yml (copier le contenu ci-dessous)
nano docker-compose.yml

# 5. Lancer
docker compose up -d

# 6. Suivre les logs
docker compose logs -f stream-fusion
```

---

## Accès aux services

| Service | URL |
|---|---|
| Application | `http://localhost:8080` |
| Admin | `http://localhost:8080/admin/` |
| Meilisearch | `http://localhost:7700` (non exposé par défaut) |
| PostgreSQL | `localhost:5432` (non exposé par défaut) |
| Redis | `localhost:6379` (non exposé par défaut) |

!!! warning "En production"
    En production, seul le port 8080 (ou Traefik) doit être exposé publiquement. Les autres ports ne doivent être accessibles que via le réseau Docker interne.

---

## Docker Compose complet

Copiez ce contenu dans un fichier `docker-compose.yml` :

Le fichier `deploy/docker-compose.yml` fourni par le projet est la
configuration communautaire de référence. Utilisez ce fichier plutôt
qu'une ancienne copie du Compose présente dans la documentation.

```bash
cd deploy
cp example.env .env

# Renseigner les valeurs requises dans .env,
# puis démarrer la stack :
docker compose up -d
```

Les noms des rôles PostgreSQL sont configurés automatiquement.

Le rôle utilisé pour la restauration PostgreSQL et son secret sont
également créés automatiquement. Aucune variable `PG_RESTORE_PASS`
n'est à renseigner dans `.env`.

---

## Mise à jour

```bash
docker compose pull
docker compose up -d
```
