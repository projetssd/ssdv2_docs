---
title: Invites utilisateur — marqueur SSDV2_PROMPT (menu CLI & WebUI)
description: Contrat du marqueur SSDV2_PROMPT pour des questions fiables et des secrets masqués, depuis le menu CLI comme depuis l’interface Web.
tags:
  - ssdv2
  - prompt
  - cli
  - webui
  - secret
  - ansible
  - bash
---

!!! abstract "Abstract"
    Cette page décrit le **marqueur `SSDV2_PROMPT`**, émis juste avant une question dans les applications SSDV2 :  
    - **pourquoi** il existe (menu CLI **et** interface Web)  
    - son **format** et le rôle de chaque champ  
    - comment l’utiliser en **Ansible** (`pause:`) et en **Bash** (`read`)  
    - les **erreurs à éviter** et les règles à retenir.

---

## TL;DR

1) ✅ Toute **question réelle** émet un marqueur `SSDV2_PROMPT` **juste avant** la lecture  
2) 🧩 `id` stable et unique, au format `app.champ` (ex. `ygege.password`)  
3) 🔐 Toute donnée sensible : `secret: true` **et** écho coupé (`echo: no` / `read -s`)  
4) 🚫 Ne jamais placer une saisie obligatoire derrière `pause()`  
5) 🖥️ Le comportement reste **identique au menu CLI** : le marqueur n’est qu’une information lue en plus par l’interface Web

---

## Pourquoi ce marqueur

Les applications SSDV2 sont lancées de **deux façons** :

- depuis le **menu CLI** (terminal) ;
- depuis l’**interface Web**, qui exécute `launch_service`/`relance_container` dans un terminal interne et doit savoir **quelle question poser** et **comment** la poser.

Sans indication, l’interface **devine** l’invite d’après le texte : c’est fragile (un libellé modifié casse la détection) et elle ne peut pas savoir qu’un champ est **secret**.

Le marqueur `SSDV2_PROMPT` résout ça :

- **détection fiable** (identifiant stable, pas de devinette) ;
- **type de saisie** : texte, mot de passe, oui/non, choix ;
- **masquage des secrets** : le champ est masqué **et la valeur est retirée des journaux**.

---

## Format

Une **ligne** émise juste avant de lire :

```text
SSDV2_PROMPT {"id":"ygege.password","label":"Mot de passe YGG","kind":"secret","secret":true}
```

| Champ | Rôle |
|---|---|
| `id` (obligatoire) | Identifiant stable et unique, de préférence `app.champ` (ex. `ygege.username`) |
| `label` | Texte court affiché à l’utilisateur |
| `kind` | `text` (défaut), `secret`, `confirm` (oui/non ou Entrée), `choice` |
| `secret` | `true` pour mot de passe/token/clé → champ masqué + valeur redactée |
| `options` | Pour `choice` : `["openvpn","wireguard"]` ou `[{"value":"5","label":"oauth2-proxy"}]` |

!!! info "Côté interface Web"
    L’interface affiche la question dans un panneau « Action requise » et renvoie la réponse ; la
    ligne du marqueur est **filtrée des logs**.

---

## Utiliser le marqueur

### Ansible (`pause:`)

Le marqueur va en **première ligne** du `prompt` (bloc `|`). Pour un secret : `echo: no` **et**
`no_log: true`.

```yaml
- name: Demander le mot de passe YGG
  ansible.builtin.pause:
    prompt: |
      SSDV2_PROMPT {"id":"ygege.password","label":"Mot de passe YGG","kind":"secret","secret":true}
      Enter value for YGG_PASSWORD (your YGG account password)
    echo: no
  register: ygg_password
  no_log: true
```

### Bash (`read`)

Émettre le marqueur sur **stderr** juste avant la lecture ; `read -s` pour un secret.

```bash
printf 'SSDV2_PROMPT %s\n' '{"id":"plex.login","label":"Login Plex","kind":"text","secret":false}' >&2
printf 'Votre login Plex : ' >&2
read -r PLEX_LOGIN

printf 'SSDV2_PROMPT %s\n' '{"id":"plex.password","label":"Mot de passe Plex","kind":"secret","secret":true}' >&2
printf 'Votre mot de passe Plex : ' >&2
read -rs PLEX_PASSWORD
```

!!! warning "Toujours couper l’écho d’un secret"
    Ansible : `echo: no` (+ `no_log: true`). Bash : `read -s`. Sans cela, la valeur apparaît
    dans les journaux.

---

## Erreurs à ne pas faire

!!! danger "À éviter"
    - **Ne pas marquer une question.** L’interface repasse en heuristique : ça marche parfois, mais casse au moindre changement de libellé (constaté sur `alfred`, `ygege`).
    - **`echo: yes` sur un secret.** La valeur est échotée dans les logs. Toujours `echo: no` (+ `no_log: true` en Ansible, `read -s` en bash).
    - **Mauvais `secret`.** Un mot de passe/token/clé doit être `secret: true` ; sinon il s’affiche en clair. Inversement, ne pas tout marquer secret (un chemin, un email restent `text`).
    - **Placer une saisie obligatoire derrière `pause()`.** `pause()` est un simple « appuyer sur Entrée », **sauté en contexte non interactif** ; il ne doit jamais servir à recueillir une information.
    - **`id` instable, générique ou dupliqué.** Utiliser `app.champ` ; éviter `login`, `password` seuls (risque de collision/ambiguïté).
    - **JSON invalide.** Guillemets doubles autour des clés/valeurs ; une ligne, pas de retour à la ligne dans le JSON.
    - **Marqueur mal placé.** Il doit précéder **immédiatement** la lecture ; sinon l’interface peut l’associer à la mauvaise étape.
    - **`options` inadaptées.** Pour `choice`, `options` doit contenir **les valeurs attendues par le script** (`"1".."5"`), pas seulement un libellé — d’où la forme `{"value":"5","label":"oauth2-proxy"}`.
    - **Cacher le marqueur.** Ne pas l’enfermer dans un `no_log` global : l’interface doit pouvoir le lire (le `no_log` se met sur la tâche de lecture, pas sur le marqueur).
    - **Confondre avec une pause de courtoisie.** Un simple « press Enter » n’a pas besoin de marqueur ; ne pas le transformer en question.

---

## À retenir

!!! success "Règles d’or"
    - Toute **question réelle** → un marqueur `SSDV2_PROMPT` juste avant la lecture.
    - Toute **donnée sensible** → `secret: true` + écho coupé.
    - Le comportement reste **identique au menu CLI** : le marqueur n’est qu’une information en plus lue par l’interface Web.
