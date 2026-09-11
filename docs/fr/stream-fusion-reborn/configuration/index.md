# Configuration

Stream Fusion Reborn se configure principalement depuis le **panneau d'administration** (`/admin/`), qui permet de modifier la majorité des paramètres à chaud sans redémarrage. Les variables d'environnement servent de valeurs par défaut et sont utilisées au premier lancement.

---

## Méthodes de configuration

<div class="grid cards" markdown>

-   :material-monitor-dashboard: **Panneau d'administration**

    Runtime, appliqué immédiatement (persisté en DB)
    
    Accessible à `/admin/` avec votre `SECRET_API_KEY`

-   :material-code-tags: **Variables d'environnement**

    Portée globale, appliqué au redémarrage
    
    Voir [Variables d'environnement](variables-environnement.md)

-   :material-file-document-edit: **Fichier `.env`**

    Docker Compose, appliqué au redémarrage du conteneur
    
    Voir [Environnement](../installation/environnement.md)

</div>

---

## Sections

<div class="grid cards" markdown>

-   :material-format-list-bulleted: **[Variables d'environnement](variables-environnement.md)**

    Liste exhaustive des ~90 variables avec types, défauts et descriptions

-   :material-download: **[Services debrid](services-debrid.md)**

    AllDebrid, TorBox, Premiumize, Real-Debrid, Debrid-Link, EasyDebrid, Offcloud, PikPak, StremThru

-   :material-sitemap: **[Indexeurs](indexeurs.md)**

    C411, Torr9, LaCale, GenerationFree, ABN, G3mini, TheOldSchool, Zilean, Nostradamus

-   :material-star: **[TRaSH Scoring](../trash/index.md)**

    Variables d'environnement du moteur de scoring Custom Formats

-   :material-shield: **[Proxy](proxy.md)**

    PROXIED_LINK, PROXY_URL, PLAYBACK_PROXY, WARP, proxyfication des flux

-   :material-clock-outline: **[Tâches planifiées](taches-planifiees.md)**

    Crontab Taskiq, maintenance automatique, activation/désactivation