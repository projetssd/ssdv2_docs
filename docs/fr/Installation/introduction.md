---
title: Introduction & prérequis — SSDV2
description: Onboarding SSDV2 : architecture, prérequis, coûts et checklist. Format MkDocs Material premium avec TL;DR + Mermaid.
tags:
  - ssdv2
  - introduction
  - prerequis
  - vps
  - plex
  - real-debrid
  - domaine
---

!!! abstract "Abstract"
    SSDV2 vous guide de **zéro à un serveur opérationnel** : préparation (SSH, sécurité, environnement) → déploiement (Docker/Traefik) → intégrations (Plex, Arr, indexers, requêtes).  
    Le document est conçu pour être **suivi dans l’ordre**, avec des choix clairs et des garde-fous (anti lock-out, bonnes pratiques).

---

## TL;DR

- ✅ **Préparez** un serveur (≥ 4 vCPU / 8 Go RAM) + OS compatible
- ✅ **Prenez** un **nom de domaine** + (recommandé) **Cloudflare**
- ✅ **Créez** vos comptes : Real-Debrid (+ Plex Pass optionnel)
- ✅ **Suivez** l’ordre du guide : **sécurité → installation → configuration apps → optimisation**

!!! tip "Raccourci mental"
    **Domaine** = accès propre (sous-domaines) • **Serveur** = exécution (Docker) • **Apps** = services • **RD** = source contenu

---

## Introduction

Bienvenue dans ce guide complet d’installation et de configuration d’un serveur avec **SSDV2**.

Il est pensé pour :
- 👶 Débutants : étapes guidées, décisions simplifiées
- 🧠 Avancés : options, optimisations, bonnes pratiques

Objectif : un serveur **sécurisé**, **performant** et **personnalisé** pour :
- streaming,
- stockage,
- automatisation de médias.

---

## Aperçu (vidéo)

[![ScreenShot](https://user-images.githubusercontent.com/64525827/166642246-48c95b9e-c116-4d5b-b3e2-2e1305389f4f.png)](https://user-images.githubusercontent.com/64525827/166640750-3a9b032f-80b1-4aa0-8966-b7abd560f57d.mp4)

---

## Architecture globale

```mermaid
flowchart LR
  U["👤 Utilisateur"] --> O["🌐 Domaine + DNS\n(sous-domaines)"]
  U --> P["🖥️ VPS / Serveur\n(Ubuntu/Debian)"]
  P --> S["🔐 SSH\n(non-root)"]
  P --> D["🐳 Docker/Compose\n+ Traefik"]
  D --> A["🧩 Apps\nPlex, Arr, Prowlarr,\nOverseerr..."]
  A --> M["📚 Médias\nFilms/Séries/4K"]
  RD["⚡ Real-Debrid"] --> A
  A --> UX["✅ UX\nStreaming + Requests\n+ Automatisation"]
```

!!! info "Lecture rapide"
    - Le **domaine** sert à exposer des sous-domaines (panels/apps) proprement.
    - Le **serveur** héberge Docker et orchestre les stacks.
    - **Real-Debrid** alimente la chaîne selon votre pipeline.
    - Les apps s’interconnectent (Overseerr ↔ Arr ↔ Prowlarr ↔ client).

---

## Prérequis

Cette section couvre :
- 🖥️ serveur (ressources & réseau),
- 🧩 compatibilité OS/CPU,
- 🔑 comptes/services,
- 💶 estimation budgétaire.

---

## Serveur

### Recommandations (confort)

| Composant | Recommandé | Pourquoi |
|---|---:|---|
| CPU | **≥ 4 vCores** | indexations / scans / services multiples |
| RAM | **≥ 8 Go** | marge pour Docker + monitoring |
| Réseau | **1 Gb/s** | accès rapide + stabilité |
| Stockage | selon usage | dépend de vos besoins et stratégie |

!!! info "Direct play"
    Pour une expérience fluide, surtout en direct play, ces specs offrent un bon équilibre performance/coût.

### Pare-feu / ports

- Plex utilise classiquement **32400**
- Selon votre architecture (reverse proxy / tunnel), l’exposition peut varier

!!! warning "Exposition réseau"
    N’exposez jamais “tout”.  
    Ouvrez uniquement le nécessaire et privilégiez **80/443** via reverse proxy quand possible.

---

## Compatibilité processeurs & OS

### Cible principale

- **Ubuntu Server 20.04 (amd64)**

### Compatibilités annoncées

- Ubuntu Server **18.04 → 22.04**
- Debian **9 → 12**
- Architectures : **amd64** et **arm64**

!!! tip "Choix recommandé"
    Si vous partez de zéro : privilégiez une version stable et largement supportée (Ubuntu 20.04/22.04 ou Debian 11/12).

---

## Comptes & services

| Service | Obligatoire | Coût estimé | Rôle |
|---|:---:|---:|---|
| Real-Debrid | ✅ | ~32 €/an | source/accès contenus selon pipeline |
| Nom de domaine | ✅ | ~15 €/an | sous-domaines (apps/panels) |
| Plex Pass | ❌ | ~60 €/an | confort mobile Plex (selon usage) |

!!! tip "Priorité"
    Si vous devez arbitrer : **domaine + RD** en priorité. Plex Pass est un bonus.

---

## Coûts estimés

- **~21,41 € / mois**
- **~257 € / an**

!!! info "Variables"
    Le coût réel dépend surtout :
    - du VPS (principal poste),
    - du domaine,
    - des options (Plex Pass),
    - et de votre hébergement (payant vs free tier).

---

## Checklist “prêt à commencer” ✅

- [ ] Serveur prêt (≥ **4 vCores / 8 Go RAM**)
- [ ] OS compatible (Ubuntu/Debian, amd64/arm64)
- [ ] Compte **Real-Debrid**
- [ ] **Nom de domaine** + accès DNS
- [ ] Accès **SSH** fonctionnel
- [ ] Je suis prêt à suivre l’ordre : **sécurité → installation → intégrations**

---

## Onboarding (séquence)

```mermaid
sequenceDiagram
  autonumber
  actor U as Utilisateur
  participant VPS as Serveur (VPS)
  participant DNS as Domaine/DNS
  participant SSD as SSDV2
  participant Apps as Apps (Plex/Arr/Indexers)

  U->>VPS: Provisionner serveur + SSH
  U->>VPS: Préparer OS (updates, user non-root)
  U->>DNS: Configurer domaine + sous-domaines
  U->>SSD: Lancer installation SSDV2
  SSD->>Apps: Déployer apps (Docker)
  U->>Apps: Configurer Plex/Arr/Prowlarr/Overseerr
  Apps-->>U: Streaming + requests + automatisation OK
```

!!! success "Résultat attendu"
    Une plateforme stable :
    - accessible via sous-domaines,
    - sécurisée,
    - prête pour l’automatisation (qualité, indexers, notifications).