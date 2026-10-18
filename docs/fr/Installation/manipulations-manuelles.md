---
title: Manipulations manuelles — venv, account.yml et gestion des services (SSDV2)
description: Procédures premium pour charger l’environnement (venv), lire/écrire/supprimer des clés dans account.yml et installer/supprimer une application sans passer par le menu.
tags:
  - ssdv2
  - venv
  - account-yml
  - yaml
  - operations
  - cli
---

!!! abstract "Abstract"
    Cette page décrit les **manipulations manuelles** SSDV2 :  
    - chargement de l’environnement (`profile.sh`) et vérification du prompt `(venv)`  
    - lecture/écriture/suppression de clés dans `account.yml` via `get_from_account_yml` et `manage_account_yml`  
    - installation/désinstallation directe d’une application via `launch_service` et `suppression_appli`  
    - **mise à jour d’image seule** via `update_container` (sans playbook)  
    - **application de l’authentification** via `apply_auth_label` (label Traefik uniquement)  
    - sortie propre de l’environnement avec `deactivate`  
    ⚠️ Toutes les opérations doivent être effectuées **hors root**.

---

## TL;DR

1) ✅ **Non-root uniquement**  
2) `source profile.sh` → vous voyez `(venv)`  
3) Lire : `get_from_account_yml [clé]`  
4) Écrire : `manage_account_yml clé valeur`  
5) Supprimer : `manage_account_yml clé " "` (suppression récursive)  
6) Installer : `launch_service service`  
7) Désinstaller : `suppression_appli service`  
8) Mettre à jour (image seule) : `update_container service`  
9) Appliquer l’auth (label-only) : `apply_auth_label service`  
10) Quitter : `deactivate`

??? tip "Principe premium"
    **Toujours auditer avant de modifier** : un `get_from_account_yml` rapide évite d’écraser une valeur sensible.

---

## Règle absolue : ne pas être root

Pour toute opération, assurez-vous de **ne pas** être root.

!!! danger "Pourquoi ?"
    Exécuter ces commandes en root peut :
    - casser les permissions,
    - créer des fichiers appartenant à root,
    - provoquer des comportements inattendus (venv/Docker/scripts),
    - compliquer les corrections (chown à répétition).

---

## Charger l’environnement (venv)

Exécutez :

```bash
cd /opt/seedbox-compose
source profile.sh
```

Après cela, vous devriez voir **`(venv)`** devant l’invite de commande.

!!! success "Validation"
    Si le prompt affiche `(venv)`, l’environnement est chargé.

!!! warning "Si `(venv)` n’apparaît pas"
    - Vérifiez le chemin : `/opt/seedbox-compose`
    - Relancez `source profile.sh`
    - Évitez de lancer le script en root (permissions cassées)

---

## Comprendre `account.yml` (structure et clés)

Les clés sont séparées par des points.

Exemple YAML :

```yaml
user:
  domain: mydomain.net
```

La clé sera :

- `user.domain`  
et sa valeur :
- `mydomain.net`

!!! info "Pourquoi cette notation ?"
    Elle permet de manipuler le YAML facilement depuis la CLI, sans éditer le fichier à la main.

---

## Afficher tout le contenu de `account.yml`

Pour afficher dans le shell tout le contenu du fichier :

```bash
get_from_account_yml
```

??? tip "Bon usage"
    Avant une modification, faites toujours un dump complet (ou un dump du bloc parent) pour éviter les surprises.

---

## Manipuler `account.yml`

### Écrire une clé (create/overwrite)

Crée la clé si elle n’existe pas, ou l’écrase si elle existe :

```bash
manage_account_yml cle valeur
```

Exemple :

```bash
manage_account_yml user.domain mondomaine.com
```

!!! warning "Écrasement"
    Si la clé existe, la valeur précédente est remplacée (pas de merge).  
    Faites un `get_from_account_yml` avant si vous n’êtes pas sûr.

??? example "Pattern safe (lecture → écriture → relecture)"
    ```bash
    get_from_account_yml user.domain
    manage_account_yml user.domain mondomaine.com
    get_from_account_yml user.domain
    ```

### Effacer une clé (et ses sous-clés)

Efface la clé **et toutes les sous-clés associées** :

```bash
manage_account_yml cle " "
```

Exemple :

```bash
manage_account_yml user.domain " "
```

!!! danger "Suppression récursive"
    En supprimant une clé “parent”, vous supprimez aussi toute son arborescence.  
    Exemple : supprimer `user` peut supprimer **domain/mail/pass/etc.**

??? tip "Avant suppression"
    Affichez d’abord l’arbre :
    ```bash
    get_from_account_yml user
    ```

### Obtenir la valeur d’une clé

```bash
get_from_account_yml cle
```

Exemple :

```bash
get_from_account_yml user.domain
```

Retour attendu :

```text
mondomaine.com
```

Si la valeur n’est pas trouvée :

```text
notfound
```

### Obtenir une clé et toutes ses sous-clés

```bash
get_from_account_yml user
```

Exemple de retour :

```text
domain: mondomaine.com group: null groupid: 1001 htpwd: seed:xxxxxxxxxxxxxx mail: moi@mondomaine.com name: seed pass: xxxxxxxxxxxxxx userid: 1001
```

!!! tip "Usage"
    Pratique pour auditer rapidement un bloc (ex. `user`, `traefik`, `apps`, etc.).

---

## Installer / lancer une application sans passer par le menu

```bash
launch_service nomduservice
```

??? example "Exemples"
    ```bash
    launch_service plex
    launch_service radarr
    launch_service sonarr
    ```

!!! success "Résultat attendu"
    Le service est déployé/démarré conformément à la recette (yml + account).

---

## Désinstaller une application sans passer par le menu

```bash
suppression_appli nomduservice
```

??? example "Exemples"
    ```bash
    suppression_appli plex
    suppression_appli radarr
    suppression_appli sonarr
    ```

!!! warning "Impact"
    Selon le mode de suppression et l’implémentation, des éléments peuvent être retirés :
    - container,
    - fichiers `.yml`,
    - entrées `account.yml`,
    - et parfois données persistantes (selon options).

!!! tip "Avant suppression"
    Si vous avez un doute : privilégiez la **réinitialisation** (quand disponible) plutôt qu’une suppression destructrice.

---

## Mettre à jour une application (image seule) sans passer par le menu

```bash
update_container nomduservice
```

!!! tip "Environnement chargé"
    Comme toutes les fonctions de cette page, elle s’utilise après `source profile.sh` (section **Charger l’environnement (venv)**), exactement comme `launch_service`.

- tire la dernière image (`docker pull`) ;
- **recrée le container à l’identique** (config, volumes/binds, réseau, ports… conservés) ;
- **sans** exécuter le playbook ni les tâches de configuration.

??? example "Exemples"
    ```bash
    update_container plex
    update_container sonarr
    ```

!!! info "Équivalent ssdv2ctl"
    ```bash
    ssdv2ctl app update nomduservice
    ```

!!! success "Résultat attendu"
    Le service tourne avec l’image à jour, configuration et données conservées.

---

## Appliquer l’authentification d’une application (label-only)

L’authentification est stockée dans `account.yml` sous `sub.<app>.auth`. La fonction ci-dessous applique le type courant **sans rejouer le playbook** :

```bash
apply_auth_label nomduservice
```

!!! tip "Environnement chargé"
    À utiliser après `source profile.sh` (venv + fonctions), comme `update_container` et `launch_service`.

- lit `sub.<app>.auth` ;
- modifie **uniquement** le label `traefik.http.routers.<app>-rtr.middlewares` ;
- **recrée** le container (les routers secondaires et le reste de la config sont conservés).

!!! tip "Changer la valeur d’abord (si besoin)"
    ```bash
    manage_account_yml sub.nomduservice.auth oauth2-proxy
    apply_auth_label nomduservice
    ```

!!! info "Équivalent ssdv2ctl"
    ```bash
    ssdv2ctl auth apply nomduservice oauth2-proxy
    ```

!!! warning "Un restart ne suffit pas"
    Changer l’auth modifie un **label Docker** : il faut **recréer** le container (ce que fait `apply_auth_label`).

---

## Quitter l’environnement de manipulation

Pour sortir du venv :

```bash
deactivate
```

!!! success "Validation"
    Le préfixe `(venv)` disparaît : vous êtes sorti de l’environnement.

---

## Diagramme de flux (opérations manuelles)

```mermaid
flowchart TD
  A["Être non-root"] --> B["Charger venv\nsource profile.sh"]
  B --> C{"Besoin ?"}
  C -->|Lire account.yml| D["get_from_account_yml\n(avec ou sans clé)"]
  C -->|Écrire/supprimer clé| E["manage_account_yml\nclé valeur | clé \" \""]
  C -->|Installer/Lancer app| F["launch_service nomduservice"]
  C -->|Mettre à jour (image seule)| I["update_container nomduservice"]
  C -->|Appliquer l'auth (label-only)| J["apply_auth_label nomduservice"]
  C -->|Supprimer app| G["suppression_appli nomduservice"]
  D --> H["deactivate"]
  E --> H
  F --> H
  I --> H
  J --> H
  G --> H
```

---

## Diagramme de séquence (édition account.yml)

```mermaid
sequenceDiagram
  autonumber
  actor U as Utilisateur
  participant V as venv (profile.sh)
  participant A as account.yml
  participant C as CLI (manage/get)

  U->>V: source profile.sh
  V-->>U: Prompt affiche (venv)
  U->>C: get_from_account_yml user.domain
  C->>A: Lecture clé user.domain
  A-->>C: Valeur (ou notfound)
  C-->>U: Affiche résultat
  U->>C: manage_account_yml user.domain mondomaine.com
  C->>A: Écrit/écrase user.domain
  A-->>C: OK
  C-->>U: Confirmation implicite
  U->>V: deactivate
  V-->>U: Sortie du venv
```