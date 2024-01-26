# Configuration qbittorrent radarr/sonarr

![Untitled(2)](https://github.com/projetssd/ssdv2/assets/7422124/97e599c1-01d7-44f0-b562-7650f356cf4f)

### Remote Path Mappings

Still in Download Clients remember to configure the Remote Path Mappings by replacing "user" with your username

![Capture](https://github.com/projetssd/ssdv2/assets/7422124/b5217ecc-487a-4231-866f-315df2cb50ab)

### Root Folders

Finally in Media Management configure the Root Folders by pointing to the Media folder (eg for radarr)

![Capture1](https://github.com/projetssd/ssdv2/assets/7422124/d226a4e3-c5fc-4faa-a82a-b9eef7425daa)

### Operating principle

Radarr/Sonarr sends the search result to rdtclient which itself launches the downloads and manages the creation of symlinks which will be stored in the ```/home/user/local/radarr``` folder. When imported by sonarr/radarr the symlinks will be moved to the ```/home/user/Medias``` folder, the folder to which PLex must point.
