# Configuration des applications

Pour configurer les applications sur votre serveur, suivez l'ordre recommandé pour optimiser l'intégration et la gestion de vos médias.
Pensez à remplacer "VOTRE_USER" par votre nom d'utilisateur créé au préalable !

## Plex

Accédez à Plex via `plex.votre_domaine.fr`, nommez votre serveur et assurer vous que la case “M'autoriser à accéder à mes médias en dehors de ma maison” est bien cochée.

- **Médiathèque** : Ajoutez vos dossiers de médias (Films, Séries, Films4K, Séries4K). Pour chaque type de média, sélectionnez le dossier approprié sous `/home/VOTRE_USER/Medias/`. Penser à désactivez la création de miniatures vidéo pour économiser de l'espace, cela se trouve dans les options avancés lorsque vous ajouter un dossier.
1. Dans l'interface utilisateur de Plex, cliquez sur `Ajouter une bibliothèque` pour commencer.
2. Sélectionnez `Films` ou `Séries TV` selon le type de dossier que vous souhaitez ajouter.
3. Vous pouvez renommer votre bibliothèque si nécessaire (par exemple, pour les dossiers "Films 4K" et "Séries 4K").
4. Cliquez sur `Ajouter des dossiers`.
5. Sélectionnez `Parcourir` et choisissez un dossier multimédia à ajouter. Les dossiers à ajouter se trouvent dans `/home/ubuntu/Medias`.
6. Cliquez sur le dossier désiré pour l'ouvrir (par exemple, "Films").
7. Confirmez en cliquant sur le bouton `Ajouter`.
8. Cliquez sur `Avancé` pour accéder aux paramètres supplémentaires.
9. Décochez l'option `Activer les miniatures des vidéos` pour économiser de l'espace et des ressources.
10. Puis vous pouvez ajuster les paramètres selon vos préférences.

En suivant ces étapes, vous aurez ajouté avec succès une nouvelle bibliothèque à votre serveur Plex et organisé selon vos préférences.

Vous pouvez cliquer sur suivant puis terminé.

Une fois arrivé sur l'accueil, entrer dans les paramètres du serveur puis dans le menu latéral de gauche rendez-vous dans :

- **Accès à distance** : Cocher “Spécifier un port public manuellement” (32400 par défaut) puis cliquer sur “Réessayer” pour permettre l'accès externe.
- **Bibliothèque** :
    - Analyser ma bibliothèque automatiquement : coché
        - Garder cette option cochée permet à Plex de détecter et d'intégrer automatiquement les nouveaux médias ajoutés à vos dossiers de bibliothèque, simplifiant la gestion de votre collection.
    - Lancer un scan partiel quand un changement est détecté : coché
        - Cette option optimise les ressources en ne scannant que les dossiers affectés par des modifications, au lieu de toute la bibliothèque, à chaque ajout de nouveau contenu.
    - Vider la corbeille automatiquement après chaque scan : décoché
        - La désactivation de cette option laissera le temps à Zurg de retrouver les contenus devenu manquant, cas de suppression de fichiers médias par Real-Debrid.
    - Autoriser la suppression de media : coché
        - En cochant cette option, vous permettez la gestion des fichiers médias directement depuis l'interface Plex, offrant une facilité de maintenance de votre bibliothèque.
    - Générer les aperçus vidéo miniatures : jamais
        - Régler cette option sur "jamais" réduit la charge sur le serveur et l'espace de stockage requis, car la génération de ces miniatures peut être très gourmande en ressources.
    - Générer les miniatures pour les chapitres : jamais
        - Tout comme les aperçus vidéo, ne pas générer de miniatures pour les chapitres économise les ressources du serveur et de l'espace de stockage sans impacter significativement l'expérience utilisateur.

---

## RDTClient

Rendez-vous sur `rdtclient.votre_domaine.fr`, créez votre compte et saisissez votre clé API Real-Debrid disponible sur `http://real-debrid/api`.

Une fois sur la page d’accueil, cliquer sur Settings, puis :

- **Dans General** :
    - **Maximum pallel downloads** : Mettez `100`.
    - **Maximum unpack processes** : Réglez aussi sur `100`.
    - Sauvegardez vos modifications en utilisant le bouton situé en bas.
- **Dans Download Client** :
    - **Download client** : Sélectionnez `Symlink Downloader`.
    - **Mapped path** : Indiquez `/home/VOTRE_USER/local`. (Remplacer VOTRE_USER par le vôtre)
    - **Rclone mount path** : Précisez `/home/VOTRE_USER/seedbox/zurg/torrents`. (Remplacer VOTRE_USER par le vôtre)
    - Sauvegardez vos modifications en utilisant le bouton situé en bas.
- **Dans qBittorrent / *darr :**
    - **Post Torrent Download Action** : Choisissez `Download all files to host`.
    - **Post Download Action** : Sélectionnez `Remove Torrent From Client`.
    - Décochez **Only download available files on debrid provider**.
    - **Minimum file size to download** : Entrez `10`.
    - Sauvegardez vos modifications en utilisant le bouton situé en bas.

---

## Radarr

Allez sur `radarr.votre_domaine.fr` et définissez une authentification.

- **Gestion des médias** :
    - Dans `Settings` puis `Media Management`, cliquez sur `Add Root Folder` et ajoutez `/home/VOTRE_USER/Medias/Films/`.
- **Clients de téléchargement** :
    - Dans `Settings` puis `Download Clients`, ajoutez qBittorrent avec les paramètres suivants :
        - **Name**: `RDTClient`
        - **Host**: `rdtclient`
        - **Port**: `6500`
        - **Username**: Votre identifiant sur `rdtclient.votre_domaine.fr`
        - **Password**: Votre mot de passe sur `rdtclient.votre_domaine.fr`
        - **Category**: `radarr`

---

## Sonarr

Rendez-vous sur `sonarr.votre_domaine.fr` et configurez une authentification.

- **Gestion des médias** :
    - Dans `Settings` puis `Media Management`, cliquez sur `Add Root Folder` et insérez `/home/VOTRE_USER/Medias/Series/`.
- **Clients de téléchargement** :
    - Ajoutez qBittorrent comme pour Radarr mais avec la **Category** sur `sonarr`.

---

## Pour les setups 4K (Radarr4K / Sonarr4K)

Répétez les étapes ci-dessus pour vos instances 4K, en ajustant simplement :

- le **Root Folder** dans `Settings` puis `Media Management` par le dossier correspondant (Films4K / Series4K)
- la **Category** dans `Download Clients` sur `radarr4k` pour Radarr et `sonarr4k` pour Sonarr.

Puis utilisez les commandes SSH suivantes pour créer les répertoires nécessaires à RDTClient pour y placer les téléchargements:

```bash
mkdir /home/VOTRE_USER/local/radarr4k
```

```bash
mkdir /home/VOTRE_USER/local/sonarr4k
```

---

## Prowlarr

Rendez-vous sur `prowlarr.votre_domaine.fr` et définissez une authentification.

1. **Configuration de FlareSolverr** :
    - Allez dans `Settings`, puis dans `Indexers`.
    - Ajoutez FlareSolverr avec les paramètres suivants :
        - **Tags**: flaresolverr (appuyer sur entrée pour confirmer la création du tag dans la zone de texte, il doit apparaitre sous forme d’étiquette)
        - **Host**: http://flaresolverr:8191/
2. **Configuration des indexers** :
    
    Une fois FlareSolverr ajouté, retournez à la page d'accueil de Prowlarr pour ajouter vos indexers.
    
    Si vous rencontrez ce message lors de l’ajout d’un indexer, c’est qu’il est nécessaire d’utiliser Flaresolverr pour qu’il fonctionne.
    
    ![Untitled](https://i.imgur.com/WBJcOsw.png)
    
    Il vous suffit de rajouter le tag que vous avez créé au préalable dans la zone correspondante.
    
    ![Untitled](https://i.imgur.com/OwZBRIN.png)

3. **Configuration des applications** :
    - Allez dans `Settings` puis `Apps`.
    - Ajoutez vos instances Radarr (et Radarr4K) et Sonarr (et Sonarr4K) comme suit :
        - Exemple pour Radarr :
            - **Prowlarr Server**: http://prowlarr:9696/
            - **Radarr Server**: http://radarr:7878
            - **API Key**: Récupérable ici https://radarr.votre_domaine.fr/settings/general
        - Exemple pour Radarr4K :
            - **Prowlarr Server**: http://prowlarr:9696
            - **Radarr Server**: http://radarr4k:7878
            - **API Key**: Récupérable ici https://radarr4k.votre_domaine.fr/settings/general
    - Cliquez ensuite sur `Sync App Indexers` pour synchroniser les indexeurs que vous avez ajouté à l’étape 2 sur toutes vos instances.

---

## Overseerr

Rendez-vous sur `overseerr.votre_domaine.fr` et connectez-vous avec votre compte Plex.

- **Configuration du serveur Plex** :
    - Entrez les informations suivantes :
        - **Hostname or IP Address**: plex
        - **Port**: 32400
    - Cliquez sur "Save Changes".
- **Sélection des bibliothèques** :
    - Cochez toutes vos bibliothèques Plex.
    - Cliquez sur "Continue".
- **Ajout des instances Radarr(4K) / Sonarr(4K)** :
    - Pour Radarr :
        - Cochez "Default Server".
        - Laissez "4K Server" décoché.
        - Remplissez les détails suivants :
            - **Server Name**: Radarr
            - **Hostname or IP Address**: radarr
            - **Port**: 7878
            - **Use SSL**: décoché
            - **API Key**: Récupérable ici https://radarr.votre_domaine.fr/settings/general
                - Une fois renseigné cliquer sur le bouton “Test” pour débloquer la suite.
            - **URL Base**: vide
            - **Quality Profile**: selon votre préférence
            - **Root Folder**: le choix proposé
            - **Minimum Availability**: selon votre préférence
            - **Tags**: vide
            - **Enable Scan**: coché
            - **Enable Automatic Search**: coché
            - **Tag Requests**: décoché
    - Pour Sonarr :
        - Cochez "Default Server".
        - Laissez "4K Server" décoché.
        - Remplissez les détails suivants :
            - **Server Name**: Sonarr
            - **Hostname or IP Address**: sonarr
            - **Port**: 8989
            - **Use SSL**: décoché
            - **API Key**: Récupérable ici https://sonarr.votre_domaine.fr/settings/general
                - Une fois renseigné cliquer sur le bouton “Test” pour débloquer la suite.
            - **URL Base**: vide
            - **Quality Profile**: selon votre préférence
            - **Root Folder**: le choix proposé
            - **Language Profile**: Deprecated
            - **Tags**: vide
            - **Anime Quality Profile**: selon votre préférence
            - **Anime Root Folder**: le choix proposé
            - **Season Folders**: coché
            - **Enable Scan**: coché
            - **Enable Automatic Search**: coché
            - **Tag Requests**: décoché

### Configuration des instances Radarr(4K) / Sonarr(4K)

- **Ajout d'instances Radarr(4K) / Sonarr(4K)**
    
    Si vous avez configuré des instances Radarr(4K) / Sonarr(4K) dans votre système, voici comment les intégrer à Overseerr :
    
    - **Default Server** : Cochez la case "Default Server" pour chaque instance Radarr(4K) / Sonarr(4K) pour indiquer qu'il s'agit de votre serveur principal.
    - **4K Server** : Cochez également la case "4K Server" pour spécifier que ces instances sont dédiées aux contenus en 4K.
    - **Server Name** : Pour chaque instance, indiquez le nom du serveur comme suit :
        - Pour Radarr4K : "Radarr 4K"
        - Pour Sonarr4K : "Sonarr 4K"
    - **Hostname or IP Address** : Utilisez les adresses suivantes en fonction de l'instance que vous configurez :
        - Pour Radarr4K : "radarr4k"
        - Pour Sonarr4K : "sonarr4k"
    - **API Key** : Récupérez la clé API respective à partir des liens suivants :
        - Pour Radarr4K : https://radarr4k.votre_domaine.fr/settings/general
        - Pour Sonarr4K : https://sonarr4k.votre_domaine.fr/settings/general

En suivant ces étapes, vous configurerez avec succès vos nouvelles instances Radarr4K / Sonarr4K dans Overseerr, en veillant à ce que les paramètres soient adaptés à chaque instance, y compris la clé API spécifique. Cela vous permettra de gérer les contenus en 4K de manière distincte.

### Configuration des paramètres généraux d'Overseerr

- **Configuration des paramètres généraux** :
    - Allez dans `Paramètres`.
    - Sous "Display Language", sélectionnez "Français".
    - Sous "Discover Region", choisissez "France".
    - Sous "Discover Language", sélectionnez "all languages".
    - Cliquez sur "Sauvegarder les changements".
- **Validation automatique des demandes** (Optionnel) :
    - Si vous souhaitez que les demandes de vos utilisateurs soient automatiquement validées, allez dans `Utilisateurs` et cochez "Valider automatiquement".
    - Vous pouvez également cocher "Signaler des problèmes" pour activer la fonctionnalité de signalement.
    - Cliquez sur "Sauvegarder".