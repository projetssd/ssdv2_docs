# 🎬 Seerr — Gestion intelligente des demandes

> 🧠 Seerr permet aux utilisateurs de demander facilement des films et séries, tout en gardant un contrôle total côté administrateur.

---

## 🚀 Présentation

Seerr est une interface moderne permettant :

- 📩 La gestion des demandes de films et séries
- 🔍 La recherche via Radarr et Sonarr
- 👥 La validation par administrateur
- 🔐 Un accès sécurisé via authentification

Il simplifie la gestion des requêtes dans un environnement Seedbox.

---

## ⚙️ Fonctionnement Global

### 1️⃣ Demande utilisateur

- L’utilisateur recherche un film ou une série
- Il envoie une demande
- La demande est mise en attente de validation (selon configuration)

### 2️⃣ Validation

- L’administrateur accepte ou refuse la demande
- En cas d’acceptation, la requête est envoyée vers Radarr ou Sonarr

### 3️⃣ Téléchargement automatique

- Radarr / Sonarr prennent le relais
- Le téléchargement est lancé automatiquement

---

## 🔐 Sécurité & Accès

Seerr peut être sécurisé via :

- Authentification locale
- Authentification via proxy (Authelia / OAuth)
- Reverse proxy HTTPS
- Limitation des permissions utilisateurs

Il est recommandé d’utiliser :

- 🔒 HTTPS obligatoire
- 🛡 Authentification externe si exposition publique
- 🔁 Synchronisation avec Radarr/Sonarr sécurisée

---

## 🐳 Déploiement Docker

### 📦 Installation standard

Seerr est généralement déployé via Docker :

```bash
docker compose up -d seerr
```

Ou via le script SSDv2 :

```bash
launch_service seerr
```

---

## 🔄 Gestion du Container

### ▶️ Relance

```bash
docker restart seerr
```

### ♻️ Réinitialisation

- Restaure le fichier `.yml` d’origine
- Conserve les données utilisateurs

### 🗑 Suppression

```bash
suppression_appli seerr
```

---

## 📊 Intégration avec l’écosystème

| Service | Rôle |
|----------|------|
| Radarr | Gestion des films |
| Sonarr | Gestion des séries |
| Traefik | Reverse proxy |
| Authelia | Authentification |
| CrowdSec | Protection |

---

## 💡 Bonnes Pratiques

- 🔒 Toujours exposer Seerr derrière un reverse proxy HTTPS
- 👤 Activer l’approbation manuelle des demandes
- 🧩 Limiter les permissions utilisateurs
- 📈 Surveiller les logs en cas d’erreur API
- 🔁 Vérifier la connectivité Radarr / Sonarr

---

# 🎯 Résumé

Seerr apporte :

- Une interface moderne
- Une gestion centralisée des demandes
- Une intégration native avec Radarr/Sonarr
- Une meilleure expérience utilisateur

Il transforme votre Seedbox en plateforme collaborative contrôlée.