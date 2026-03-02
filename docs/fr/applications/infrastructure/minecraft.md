# ⛏️ Minecraft — Présentation & Exploitation Premium (Serveur Java & Bedrock)

### Hébergement “pro” : performance, gouvernance, sauvegardes, mods, sécurité d’accès (sans recettes d’installation)
Optimisé pour reverse proxy / VPN existants • Qualité de config • Maintenance durable • Tests & Rollback

---

## TL;DR

- Un serveur Minecraft “premium” = **règles claires**, **perfs stables**, **sauvegardes fiables**, **mods maîtrisés**, **accès contrôlé**.
- Choix clé : **Java** (mods/plugins riches) vs **Bedrock** (cross-play consoles/mobile).
- Pour éviter 90% des soucis : **whitelist + backups + limites de distance + monitoring + discipline de version**.

---

## ✅ Checklists

### Pré-production (avant d’ouvrir aux joueurs)
- [ ] Choisir l’édition : Java / Bedrock (et version cible)
- [ ] Définir le “contrat serveur” : règles, horaires, monde (seed), difficulté, keepInventory, etc.
- [ ] Activer whitelist + ops minimal
- [ ] Fixer un budget perf : RAM/CPU, distances, view/simulation
- [ ] Mettre en place une stratégie backups (monde + configs)
- [ ] Décider : vanilla / Paper/Purpur / Fabric / Forge / modpack

### Post-configuration (qualité d’exploitation)
- [ ] Un redémarrage “clean” reproduit l’état attendu
- [ ] Test join/leave + test latence + test chunks
- [ ] Backups restaurables (test réel)
- [ ] Politique d’update (quand, comment, rollback)
- [ ] Runbook incident (lag, crash, corruption monde)

---

> [!TIP]
> La meilleure “feature” d’un serveur Minecraft stable, c’est une **discipline de versions** : ne mélange pas upgrades, mods et changements de config le même jour.

> [!WARNING]
> Les mondes deviennent vite “critiques”. Sans backups testés, le serveur finira en drame (corruption, suppression, grief, disque plein).

> [!DANGER]
> Éviter de laisser une console/gestion RCON accessible sans contrôle d’accès. Traite l’administration Minecraft comme de l’admin système.

---

# 1) Minecraft — Vision moderne (serveur “pro”)

Un serveur Minecraft n’est pas juste “un monde” :

- 🧱 **Un simulateur** (ticks, entités, redstone)
- 🧠 **Un système de règles** (game rules, permissions)
- 🧩 **Une plateforme extensible** (plugins/mods)
- 💾 **Une base de données de fait** (chunks + inventaires + progression)
- 🔄 **Un service** (disponibilité, mises à jour, support joueurs)

---

# 2) Architecture globale (référence)

```mermaid
flowchart LR
  Players["🎮 Joueurs"] -->|Java: TCP 25565\nBedrock: UDP 19132| Server["⛏️ Minecraft Server"]
  Admin["🧑‍💻 Admin"] --> Console["🧾 Console / RCON"]
  Console --> Server

  Server --> World["🌍 Monde (chunks)\nworld/ nether/ end/"]
  Server --> Config["⚙️ Configs\nserver.properties\nplugins/mods"]
  Server --> Logs["🧱 Logs\nlatest.log"]
  Backup["📦 Backups"] <-- World
  Backup <-- Config
  Monitor["📈 Monitoring"] --> Server
```

---

# 3) Choix du “type” de serveur (impact énorme)

## Java Edition — options courantes
- **Vanilla** : simplicité, fidélité, perfs OK mais limites
- **Paper** : performance + plugins Bukkit/Spigot
- **Purpur** : Paper + options gameplay/perf supplémentaires
- **Fabric** : mods “tech”/perf (Lithium, etc.) + mod ecosystem
- **Forge/NeoForge** : gros modpacks (attention ressources)

## Bedrock Edition — positionnement
- Cross-play (mobile/console/Win)
- Très pratique pour groupes mixtes
- Écosystème mods différent de Java

> [!TIP]
> “Le bon choix” = celui qui minimise les surprises :
> - communauté plugins → Paper/Purpur
> - gros modpack → Forge/NeoForge
> - optimisation + mods légers → Fabric
> - cross-play → Bedrock

---

# 4) Les 5 piliers d’une config premium

1. 🧭 **Gouvernance** : whitelist, ops minimaux, règles claires
2. ⚡ **Performance** : distances, entités, redstone, scheduling
3. 💾 **Backups** : versionnés, fréquents, restaurables
4. 🧩 **Extensions** : mods/plugins contrôlés (versions, compat)
5. 🛡️ **Accès admin** : console/RCON sous contrôle (réseau/SSO/VPN existants)

---

# 5) Configuration “cœur” (server.properties & règles)

## 5.1 Paramètres perfs (les plus rentables)
- `view-distance` (Java) : baisse = gain CPU/RAM
- `simulation-distance` (Java) : baisse = gain TPS (souvent le plus efficace)
- `max-tick-time` : attention (désactiver peut masquer des freeze)
- `spawn-protection` : utile pour éviter grief au spawn
- `difficulty`, `hardcore`, `pvp` : cohérence “contrat serveur”

> [!WARNING]
> Trop de view-distance = chunks + entités + redstone = TPS qui s’effondre, surtout avec plusieurs joueurs.

## 5.2 Gouvernance joueurs (anti-drama)
- whitelist activée
- ops limités (1–2 max)
- règles écrites (BookStack, Discord, MOTD)
- inventaire : décider `keepInventory` dès le départ (changer après = disputes)

---

# 6) Mods / Plugins (méthode premium : maîtriser le risque)

## 6.1 Règles d’or
- 1 changement = 1 déploiement
- snapshot backup avant toute modification
- ne pas mélanger upgrade de version + ajout mods dans le même créneau
- maintenir une liste “golden” (mods/plugins validés)

## 6.2 Typologie d’extensions (pour choisir lucidement)
- **Qualité de vie** : homes, claims, permissions (plugins Paper)
- **Performance** : optimisation tick, entités (Fabric mods / configs Paper)
- **Contenu** : nouveaux items/biomes (modpacks)
- **Admin** : anti-cheat, logs, audit

> [!TIP]
> Pour serveurs publics/amis : préfère 10 plugins stables à 60 “gadgets” inconnus.

---

# 7) Sauvegardes (stratégie premium)

## 7.1 Ce qu’on sauvegarde
- Monde : `world/`, `world_nether/`, `world_the_end/` (ou équivalents)
- Config : `server.properties`, `whitelist.json`, `ops.json`, permissions
- Plugins/mods : dossiers + configs
- Logs (optionnel) : utile pour post-mortems

## 7.2 Backups “simples et robustes” (exemple logique)
- fréquence : toutes les X heures + avant changements
- rétention : 7 jours + 4 semaines (à adapter)
- stocker une copie hors machine (NAS / cloud / autre host)

### Exemple (backup archive)
```bash
# Exemple générique : adapte les chemins à ton setup
TS="$(date +%F_%H%M%S)"
tar -czf "/backups/mc_${TS}.tgz" \
  /srv/minecraft/world \
  /srv/minecraft/world_nether \
  /srv/minecraft/world_the_end \
  /srv/minecraft/server.properties \
  /srv/minecraft/whitelist.json \
  /srv/minecraft/ops.json \
  /srv/minecraft/plugins \
  /srv/minecraft/mods
```

> [!WARNING]
> Une sauvegarde n’existe pas tant que tu n’as pas fait **un test de restauration**.

---

# 8) Exploitation & “Runbook” (comment diagnostiquer vite)

## 8.1 Signaux classiques
- Lag ressenti → TPS bas / tick long
- Téléportations/rollback entités → surcharge
- Crash loop → mod/plugin incompatible, RAM insuffisante, corruption

## 8.2 Checklist incident “lag”
- réduire `view-distance` / `simulation-distance`
- vérifier entités (fermes, animaux, items au sol)
- identifier les chunks problématiques (spawn, farms)
- si Paper/Purpur : revoir configs de despawn/merge items
- vérifier GC / mémoire / CPU saturation

## 8.3 Pattern de logs utiles
- `Can't keep up!` (Java) → surcharge tick
- `OutOfMemoryError` → RAM/flags
- erreurs de mod loader (Fabric/Forge) → compat versions

---

# 9) Validation / Tests / Rollback

## 9.1 Tests de validation (après changement)
```bash
# Vérifie que le port répond (exemples)
# Java (TCP 25565) :
nc -zv SERVER_IP 25565

# Bedrock (UDP 19132) :
# (selon outils dispo) :
# nc -zvu SERVER_IP 19132
```

Tests fonctionnels (manuel) :
- join 2 joueurs
- déplacement + chargement chunks
- interaction redstone simple
- vérifier que whitelist/permissions s’appliquent

## 9.2 Rollback (stratégie)
- rollback “contenu” : restaurer backup monde + configs
- rollback “binaire/stack” : revenir à la version précédente (server jar / modpack / image)
- rollback “mod/plugin” : retirer l’extension et restaurer la config correspondante

> [!DANGER]
> Toujours conserver un backup “juste avant” le changement, et ne pas le réutiliser pour autre chose.

---

# 10) Sources — Images Docker (urls brutes uniquement)

## 10.1 Image communautaire la plus citée (Java)
- `itzg/minecraft-server` (Docker Hub) : https://hub.docker.com/r/itzg/minecraft-server  
- Doc officielle (ReadTheDocs) : https://docker-minecraft-server.readthedocs.io/  
- Repo de packaging (référence de l’image) : https://github.com/itzg/docker-minecraft-server  

## 10.2 Bedrock (officiel Mojang téléchargé au démarrage, via image)
- `itzg/minecraft-bedrock-server` (Docker Hub) : https://hub.docker.com/r/itzg/minecraft-bedrock-server  
- Repo de packaging (référence de l’image) : https://github.com/itzg/docker-minecraft-bedrock-server  

## 10.3 Proxies (réseau multi-serveurs : Bungee/Velocity)
- `itzg/mc-proxy` (Docker Hub) : https://hub.docker.com/r/itzg/mc-proxy  
- Doc itzg (section proxy) : https://docker-minecraft-server.readthedocs.io/  

## 10.4 LinuxServer.io (LSIO) — statut à connaître
- Il n’y a pas d’image LSIO “minecraft-server” dédiée dans leur catalogue principal (à date). Catalogue : https://www.linuxserver.io/our-images  
- Image LSIO liée à l’écosystème (panel McMyAdmin2) — **dépréciée** : `linuxserver/mcmyadmin2` (Docker Hub) : https://hub.docker.com/r/linuxserver/mcmyadmin2  

---

# ✅ Conclusion

Minecraft “premium” = une expérience stable parce que tu as :
- des règles (gouvernance),
- des perfs cadrées (distances/entités),
- des backups restaurables,
- une stratégie mods/plugins disciplinée,
- un vrai plan de validation + rollback.

Si tu me donnes ton contexte (Java vs Bedrock, vanilla vs mods, nombre de joueurs, hardware), je peux te générer une section “paramètres recommandés” calibrée — toujours sans installation.