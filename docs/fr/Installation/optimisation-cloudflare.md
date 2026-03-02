---
title: Optimisation Cloudflare — SSDV2 (Traefik / Docker)
description: Réglages Cloudflare recommandés (SSL/TLS, certificats de périphérie, firewall, vitesse, cache, page rules) pour un usage seedbox/Traefik, avec précautions (HSTS, TOS, bypass cache streaming).
tags:
  - ssdv2
  - cloudflare
  - traefik
  - security
  - tls
  - firewall
  - caching
  - plex
---

!!! abstract "Abstract"
    Cette page propose une configuration Cloudflare **recommandée** pour un environnement SSDV2 (Traefik/Docker) :  
    **SSL/TLS (Full)**, durcissement TLS (1.2+ / TLS 1.3), options de certificats de périphérie, règles firewall (pays/IP), réglages de sécurité (Bot Fight Mode, Browser Integrity Check) et surtout des **règles de contournement du cache** pour les services de streaming (Plex/Emby/Jellyfin).  
    Objectif : **sécurité + stabilité + conformité** (notamment sur le plan gratuit).

---

## TL;DR

1) 🔐 SSL/TLS = **Full**  
2) 🔁 Always Use HTTPS = **ON**  
3) 🧊 Cache = **Standard**, mais **bypass streaming** (Plex/Emby/Jellyfin)  
4) 🧱 Firewall = règles simples + whitelist IP maison/VPN  
5) ⚠️ HSTS = **uniquement après validation complète**

??? tip "Principe premium"
    Cloudflare = **edge security & TLS**.  
    Traefik = **routage & contrôle d’accès**.  
    Streaming = **pas de cache** côté Cloudflare.

---

## Objectif

- 🔐 Sécuriser les accès (TLS, HTTPS forcé, protections Cloudflare)
- 🧱 Réduire le trafic malveillant (firewall rules, bot protections)
- ⚡ Améliorer la performance quand pertinent (Brotli, optimisations)
- 🎬 Éviter les problèmes de cache/proxy sur les médias (Plex, etc.)
- ✅ Rester conforme aux règles Cloudflare (notamment en plan gratuit)

---

## Vue d’ensemble (ordre conseillé)

```mermaid
flowchart TD
  A["1) SSL/TLS"] --> B["2) Edge Certificates"]
  B --> C["3) Firewall (Rules/Tools/Settings)"]
  C --> D["4) Vitesse (minify/brotli/loader)"]
  D --> E["5) Caching (niveau/TTL/Always Online)"]
  E --> F["6) Règles de bypass streaming (Plex/Emby/Jellyfin)"]
  F --> G["Validation + (option) HSTS"]
```

---

## 1) SSL/TLS Options

### Mode SSL/TLS

Activez **Full SSL mode**.

![SSL/TLS Full](https://user-images.githubusercontent.com/64525827/105626452-ebf35a00-5e2f-11eb-991f-a491e98fd1b5.png)

!!! tip "Pourquoi Full ?"
    Le trafic est chiffré :
    - entre l’utilisateur et Cloudflare,
    - et entre Cloudflare et votre serveur.

---

## 2) Edge Certificates (Certificats de périphérie)

Dans **Certificats de périphérie**, appliquez :

![](https://user-images.githubusercontent.com/64525827/105626484-3543a980-5e30-11eb-8d2d-37657b581a0a.png)

- **Always Use HTTPS** : **ON**
- **Minimum TLS Version** : **1.2**
- **TLS 1.3** : **ON**
- **Automatic HTTPS Rewrites** : **ON**
- **Certificate Transparency Monitoring** : **ON**

### HSTS (avec prudence)

- **HTTP Strict Transport Security (HSTS)** : **Enable** *(seulement quand stable)*

!!! danger "HSTS : risque de lock-out (web)"
    Activez HSTS **uniquement après** validation complète :
    - tous les sous-domaines OK,
    - certificats OK,
    - aucun besoin “temporaire” de repasser en HTTP,
    - plan de secours prêt (accès direct `IP:PORT` si nécessaire).

---

## 3) Firewall

### Firewall Rules (plan gratuit : 5 règles)

Sous **Règles de pare-feu**, le plan gratuit permet jusqu’à 5 règles.

Cas d’usage typiques :
- bloquer des pays à fort bruit (si cohérent avec votre usage)
- autoriser uniquement les pays où vous vous connectez
- bloquer le reste

![Firewall Rules](https://user-images.githubusercontent.com/64525827/105626846-f5ca8c80-5e32-11eb-94a7-663d277006a4.png)

!!! tip "Stratégie premium"
    **Whitelist** (IP maison/VPN) + **restrictions pays** (si applicable) = grosse réduction du bruit et des scans.

---

### Firewall Tools (whitelist IP)

Dans **Outils**, vous pouvez whitelist une IP (ex : IP WAN de votre domicile).

![IP whitelist](https://user-images.githubusercontent.com/64525827/105626853-febb5e00-5e32-11eb-8322-8bb965180b13.png)

!!! warning "IP dynamique"
    Si votre IP WAN change souvent, privilégiez :
    - un VPN à IP fixe,
    - ou une plage IP (si dispo),
    - ou adaptez la whitelist quand nécessaire.

---

### Firewall Settings (réglages recommandés)

- **Security Level** : **High**
- **Bot Fight Mode** : **ON**
- **Challenge Passage** : **30 Minutes**
- **Browser Integrity Check** : **ON**

!!! warning "Compatibilité clients"
    Un niveau de challenge trop agressif peut perturber certains clients/applications.  
    En cas de souci : baissez le niveau ou whitelist votre IP.

---

## 4) Vitesse

Impact généralement modéré pour une seedbox/Traefik.

Réglages recommandés :

- **Auto Minify** : **OFF**
- **Brotli** : **ON**
- **Rocket Loader** : **OFF**

![](https://user-images.githubusercontent.com/64525827/105626862-14c91e80-5e33-11eb-866e-87f642d14ef1.png)

!!! info "Pourquoi Minify OFF ?"
    Sur des apps web “complexes”, minifier côté Cloudflare peut parfois casser JS/CSS.

---

## 5) Caching

- **Caching Level** : **Standard**
- **Browser Cache TTL** : **1 hour**
- **Always Online** : **OFF**

!!! tip "Pattern recommandé"
    Cache standard global + exceptions via règles/bypass pour les apps sensibles (notamment streaming).

---

## 6) Règles de bypass streaming (indispensable)

Pour Docker + Traefik, surtout en serveur média (Plex / Emby / Jellyfin), c’est un réglage majeur.

Objectif :
- éviter cache/proxy “inadaptés” sur le streaming
- éviter bugs de lecture et comportements inattendus
- préserver la conformité Cloudflare (plan gratuit)

Illustrations :

![](https://camo.githubusercontent.com/cda7414ca78e8e8d5ea5754390e57c0681fce71b/68747470733a2f2f692e696d6775722e636f6d2f513433304c6b7a2e706e67)

![](https://camo.githubusercontent.com/c2cb6903c9a1279b99daeddf09430589bfe29913/68747470733a2f2f692e696d6775722e636f6d2f706c57456c6b662e706e67)

### Recommandation (à appliquer)

Créez des règles (Page Rules ou équivalents selon l’UI Cloudflare) pour **désactiver cache / optimiser** sur :

- `plex.votre_domaine.fr/*`
- `emby.votre_domaine.fr/*`
- `jellyfin.votre_domaine.fr/*`

!!! danger "Conformité Cloudflare (plan gratuit)"
    Utiliser Cloudflare comme proxy/caching pour du streaming média sans exceptions adaptées peut être incompatible avec les conditions Cloudflare et vous exposer à un **ban**.  
    La règle pratique : **bypass cache** sur les services de streaming.

---

## Checklist (validation)

- [ ] SSL/TLS mode = **Full**
- [ ] Always Use HTTPS = **ON**
- [ ] Minimum TLS = **1.2**
- [ ] TLS 1.3 = **ON**
- [ ] Automatic HTTPS Rewrites = **ON**
- [ ] CT Monitoring = **ON**
- [ ] Firewall Security Level = **High**
- [ ] Bot Fight Mode = **ON**
- [ ] Browser Integrity Check = **ON**
- [ ] Brotli = **ON**
- [ ] Auto Minify = **OFF**
- [ ] Rocket Loader = **OFF**
- [ ] Cache Level = **Standard**
- [ ] Browser Cache TTL = **1 hour**
- [ ] Bypass streaming actif (Plex/Emby/Jellyfin)
- [ ] HSTS activé **uniquement** après validation complète

!!! success "Résultat attendu"
    - Navigation HTTPS stable (apps/panels)  
    - Moins de bruit/attaques  
    - Aucun effet de bord sur le streaming  
    - Posture “clean” côté Cloudflare

---

## Diagramme de séquence (requête via Cloudflare)

```mermaid
sequenceDiagram
  autonumber
  actor U as Utilisateur
  participant CF as Cloudflare
  participant T as Traefik
  participant S as Service (Plex/Apps)

  U->>CF: Requête HTTPS (domaine)
  alt Règle bypass streaming
    CF-->>T: Proxy direct (pas de cache media)
  else Trafic standard
    CF->>CF: Cache/optimisations selon règles
    CF-->>T: Forward vers Traefik
  end
  T-->>S: Routage vers service interne
  S-->>U: Réponse (panel/stream)
```