# Configuration qbittorrent radarr/sonarr

![Untitled(2)](https://github.com/projetssd/ssdv2/assets/7422124/97e599c1-01d7-44f0-b562-7650f356cf4f)

### Remote Path Mappings

Toujours dans Download Clients penser à configurer le Remote Path Mappings en remplacant "user" par votre nom d'utilisateur

![Capture](https://github.com/projetssd/ssdv2/assets/7422124/b5217ecc-487a-4231-866f-315df2cb50ab)

### Root Folders

Enfin dans Media Management configurer le Root Folders en pointant sur le dossier Medias (ex pour radarr)

![Capture1](https://github.com/projetssd/ssdv2/assets/7422124/d226a4e3-c5fc-4faa-a82a-b9eef7425daa)

### Principe de fonctionnement

Radarr/Sonarr envoie le resultat de la recherche à rdtclient qui lui même lance les téléchargements, gère la création des symlinks qui seront stokés dans le dossier ```/home/user/local/radarr```. Au moment de l'importation par sonarr/radarr les symlinks seront déplacés dans le dossier ```/home/user/Medias```, dossier vers lequel PLex doit pointer.


 