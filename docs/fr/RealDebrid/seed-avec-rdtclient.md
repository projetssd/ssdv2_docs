# Seed les symlink téléchargé par RDTClient

## Changement apporté

Il est désormais possible de seeder les **symlink** des fichiers téléchargé par RDTClient.
Cette fonctionnalité se base sur le paramètre déjà existant "Copy added torrent files" qui a été revisité.
Si cette fonctionnalité est activée (en spécifiant un chemin dans les paramètres), RDTClient transférera les fichiers .torrent originaux vers un client dédié au seed. 
En cas de désactivation, RDTClient fonctionnera comme si aucune modification n'avait été apportée.

**Compatible avec AMD64 et ARM64.**
Image Docker : `systr0/rdt-client-2.0.39:latest`

Les images Docker sont donné à but informatif, vous avez la possibilité d'installer automatiquement cette version modifiée ainsi que Rtorrentvpn directement via le script !

## Configuration

1. **Configuration du chemin d'importation** :
   - Dans les paramètres de RDTClient, spécifiez le chemin où les fichiers .torrent doivent être copiés et importés.
![image](https://github.com/systr0/rdt-client-2.0.39/assets/158838664/e27f08ba-f8b7-44e3-950d-b6acc8f40de2)

2. **Installation d'un client torrent pour seed (ex : Rtorrentvpn)** :
   - Installez Rtorrentvpn (testé et compatible) ou un client torrent disposant des mêmes spécificités d'importation automatique.
Image Docker : `binhex/arch-rtorrentvpn:latest`

3. **Configuration du VPN** :
   - Ouvrez le port pour les connexions entrantes de votre client torrent **sur le VPN**.

4. **Exemple de configuration du client Rtorrentvpn** :
   - Activez AutoWatch dans les Paramètres sous AutoTools.
   - Définissez le chemin à surveiller, identique à celui configuré dans RDTClient pour la copie des fichiers .torrent.
   - Assurez-vous que l'option “Démarrer le téléchargement automatiquement” est activée.
![image](https://github.com/systr0/rdt-client-2.0.39/assets/158838664/f10a5814-72af-4c18-b579-ad8d3e708997)


5. **Adaptation pour autres clients torrent** :
   - Répétez l'étape 4 ci-dessus en adaptant selon le client torrent utilisé, de sorte à reproduire le procédé de surveillance d'un dossier, dans le but d'importer les fichiers .torrent déposés dedans.

## Explication du fonctionnement

Lorsqu'un chemin est spécifié dans les paramètres de RDTClient pour l'option "Copy added torrent files" :
- **Création de liens symboliques additionnels** : À la fin du téléchargement par RDTClient, lors de la création des symlink pour l’import par les *arrs, création de symlink additionnel pour le client de seed dans le path défini où doit être copié le fichier .torrent.

- **Gestion modifiée des fichiers .torrent** : 
  - Les fichiers .torrent sont temporairement stockés hors du path surveillé par le client de seed pour éviter les imports prématurés.
Un dossier est créé là où est défini le paramètre Mapped path dans Download Client de RDTClient.
Exemple: `Mapped_path_Download_Client/tempTorrentsFiles`
  - Suite à la création des liens symbolique déplacement du fichier .torrent dans le path surveillé par le client de seed pour qu’il importe.
  - Import puis début de la vérification des fichiers déjà présents dû au symlink qui pointe vers Real-Debrid, puis seed des fichiers.
  
- **En cas d'échec de création des symlink** : Le fichier .torrent ne sera pas déplacé du dossier temporaire 'tempTorrentFiles' pour éviter que le client de seed importe et télécharge (de nouveau si déjà téléchargé par RDTClient car non en cache) les fichiers.