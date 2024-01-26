# configuration rdtclient

Garder à l’esprit qu’aucun des torrents téléchargés par qbitttorrent ne sera physiquement sur votre serveur, tout est stocké sur les serveurs de Realdebrid. En clair vous n’avez pas besoin d’espace de stockage hormis celui nécessaire pour installer le script ainsi que les applications.

Go to http://localhost:6500/ ou https:[/](http://rdtclient:6500/)[/](http://rdtclient:6500/)[rdtclient.domain.com](http://rdtclient.domain.com/), puis enregistrez vous. Aller ensuite sur settings : 

Configurer Rdtclient exactement comme mentionner sur les images ci dessous

![Capture](https://github.com/projetssd/ssdv2/assets/7422124/368ef533-5d3b-4b46-ad29-ae05be76b6b9)

1. Compléter les catégories `radarr,sonarr` (vous pouvez en rajouter plus si vous le souhaitez)
2. Augmenter le nombre “parallel download” à 100, ainsi que le maximum unpack process

![Capture1](https://github.com/projetssd/ssdv2/assets/7422124/60057ea0-69c1-4a98-a369-3ac51bb91a8e)

1. Choisir Symlink Downloader sous Download client
2. mettre `/data/downloads` comme “download path”
3. mettre `/home/user/local` comme “mapped path”

!!! note
    💡 IMPORTANT : Le dossier mapped correspond au dossier local dans lequel les liens symboliques seront stockés.


![Capture2](https://github.com/projetssd/ssdv2/assets/7422124/8b3e52be-ce2c-4941-b19c-219f47bdc6a3)

!!! note
    Préciser le chemin de “Rclone mount path”, en remplacant "user" par votre nom d'utilisateur


![Capture3](https://github.com/projetssd/ssdv2/assets/7422124/267c93a6-5a33-4ec3-9699-cca4365eb039)

![Capture4](https://github.com/projetssd/ssdv2/assets/7422124/63384b2a-3b7e-4790-9d35-42005eba208b)


