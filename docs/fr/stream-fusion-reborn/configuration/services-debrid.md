# Services Debrid

Stream Fusion Reborn supporte **9 services debrid** + 1 proxy (StremThru). Vous pouvez configurer zéro, un ou plusieurs services simultanément.

---

## Modes de configuration

<div class="grid cards" markdown>

-   :material-server: **Compte serveur unique**

    Un token partagé entre tous les utilisateurs. Configuré via les variables d'environnement.
    
    Activé automatiquement quand `*_TOKEN` est défini.

-   :material-account: **Comptes utilisateur**

    Chaque utilisateur configure son propre token dans la page de configuration du plugin.
    
    Aucune variable d'environnement nécessaire.

</div>

!!! warning "Compte serveur unique"
    Si un service debrid est configuré en variable d'environnement, il sera partagé entre **tous les utilisateurs**. Pour une petite instance familiale, cela peut être acceptable. Pour une instance publique, **c'est fortement déconseillé** : les services debrid sont à bas coût pour les utilisateurs, et un compte utilisé par de nombreuses personnes risque d'être banni.

    Préférez laisser chaque utilisateur configurer son propre service depuis la page de configuration du plugin.

---

## Services supportés

<div class="grid cards" markdown>

-   :material-alpha-a-box: **AllDebrid (recommandé)**

    Le debrideur avec les meilleurs services et le plus de cache FR
    
    `AD_TOKEN=votre-token`
    
    [:material-open-in-new: Obtenir un token](https://alldebrid.com)

-   :material-alpha-t-box: **TorBox**

    Torrent cloud populaire
    
    `TB_TOKEN=votre-token`
    
    [:material-open-in-new: Obtenir un token](https://torbox.app)

-   :material-alpha-p-box: **Premiumize**

    Service debrid rapide
    
    `PM_TOKEN=votre-token`
    
    [:material-open-in-new: Obtenir un token](https://premiumize.me)

-   :material-alpha-r-box: **Real-Debrid (déconseillé)**

    !!! danger "Service en fin de vie"
        Real-Debrid n'est plus recommandé. Son cache FR est pauvre, il renvoie fréquemment de faux résultats, et son API est extrêmement restrictive. Le support est maintenu pour les comptes existants uniquement. Vous pouvez limiter le recours à Real-Debrid via la variable `RD_UNIQUE_ACCOUNT`.

    `RD_TOKEN=votre-token`
    
    [:material-open-in-new: Obtenir un token](https://real-debrid.com)

-   :material-alpha-d-box: **Debrid-Link**

    Service français avec authentification OAuth2 device-flow
    
    `DL_TOKEN=votre-token`
    
    [:material-open-in-new: Obtenir un token](https://debrid-link.com)

-   :material-alpha-e-box: **EasyDebrid**

    Debrid simple et rapide
    
    `ED_TOKEN=votre-token`

-   :material-alpha-o-box: **Offcloud**

    Format: `email:password`
    
    `OC_CREDENTIALS=email:password`

-   :material-alpha-k-box: **PikPak**

    Format: `email:password`
    
    `PP_CREDENTIALS=email:password`

-   :material-swap-horizontal: **StremThru**

    Proxy debrid multi-service — un token unique pour tous les backends
    
    `STREMTHRU_URL=https://stremthru.13377001.xyz`
    
    [:material-arrow-right: Documentation StremThru](stremthru.md)

</div>

---

## Authentification via l'API

!!! note "Développeurs uniquement"
    L'authentification déportée via l'API est destinée aux développeurs intégrant Stream Fusion dans leur application. Les utilisateurs standards n'ont pas besoin de l'utiliser — la configuration se fait depuis la page de configuration du plugin ou le panneau d'administration.

=== "Real-Debrid (Device Code)"

    ```bash
    # 1. Obtenir un device code
    curl -X POST http://localhost:8080/api/auth/realdebrid/device_code \
      -H "secret-key: votre-secret-api-key"
    
    # 2. L'utilisateur valide sur https://real-debrid.com/device
    
    # 3. Récupérer le token
    curl -X POST http://localhost:8080/api/auth/realdebrid/token \
      -H "secret-key: votre-secret-api-key"
    ```

=== "AllDebrid (PIN)"

    ```bash
    # 1. Obtenir un PIN
    curl http://localhost:8080/api/auth/alldebrid/pin/get \
      -H "secret-key: votre-secret-api-key"
    
    # 2. L'utilisateur valide sur alldebrid.com
    
    # 3. Vérifier le PIN
    curl "http://localhost:8080/api/auth/alldebrid/pin/check?checkpin=PIN&id=ID" \
      -H "secret-key: votre-secret-api-key"
    ```

=== "Debrid-Link (Device Code)"

    ```bash
    # 1. Obtenir un device code
    curl -X POST http://localhost:8080/api/auth/debridlink/device_code \
      -H "secret-key: votre-secret-api-key"

    # 2. L'utilisateur valide sur https://debrid-link.com/device

    # 3. Récupérer le token
    curl -X POST http://localhost:8080/api/auth/debridlink/token \
      -H "secret-key: votre-secret-api-key"
    ```

    Debrid-Link utilise le flux OAuth2 **device-code**, similaire à Real-Debrid. L'utilisateur reçoit un code court qu'il valide sur le site de Debrid-Link. Le système sonde ensuite l'API pour récupérer le token une fois la validation effectuée. Le flux est implémenté dans `services/dl_conn/token_manager.py` :

    - **`DebridLinkService`** — client OAuth2 bas niveau (`/api/oauth/device/code`, `/api/oauth/token`)
    - **`DLTokenManager`** — gestion du cycle de vie du token (refresh, expiration, persistance)

---

!!! warning "Sécurité"
    Les tokens sont chiffrés en base de données. Ne partagez jamais votre `SECRET_API_KEY` ou `CONFIG_SECRET_KEY`.