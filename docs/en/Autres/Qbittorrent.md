#Qbittorrent

## Qbittorrent settings

By default you must use as username (admin/adminadmin)

### File saving path

data source: /home/USER/local/qbittorrent/downloads/…

!! ATTENTION !!
If you use a specific path (for example /home/user/local/qbittorrent), you should remember to modify the configuration of cloudplow/crop so that the folder is not taken into account for uploads

> From the interface, you must use the full path `/home/USER/local/qbittorrent/downloads/...`  

We will start by securing and putting the interface in French

#### Language (Tools/Option/web interface)
![french](https://user-images.githubusercontent.com/64525827/107520001-33f4d980-6bb1-11eb-8690-249c3723710c.png)

Here we can change the default username and password and also disable auth with localhost
#### Authentication (Tools/Option/web interface)
<img width="662" alt="auth qbittorrent" src="https://user-images.githubusercontent.com/64525827/149655235-21ce21aa-1b30-414d-8307-01ae51514dce.png">


#### Download (Tools/Option/Downloads)
![record](https://user-images.githubusercontent.com/64525827/107518518-63a2e200-6baf-11eb-828b-2891a6c16588.png)


## Optimizations   


#### Settings: (Tools/Option/Advanced/libtorrent section)
you must deactivate the use of the cache as well as other changes (compare with the image)

<img width="675" alt="qbittorrent setting" src="https://user-images.githubusercontent.com/64525827/149655285-0102f79a-691d-4e9c-a213-4b9fc8a4de6c.png">


#### Connections (Tools/Option/Connection)   
![connections](https://user-images.githubusercontent.com/64525827/107518883-d2803b00-6baf-11eb-97da-bc94d2bc2baf.png)


#### Prioritization (Tools/Option/BitTorrent)   

![prioritization](https://user-images.githubusercontent.com/64525827/107518996-f774ae00-6baf-11eb-9a90-31e456974b22.png)

### Added Qbittorrent to Radarr and Sonarr (Download client - Remote Path Mappings)

<img width="1171" alt="radarr and sonarr remote" src="https://user-images.githubusercontent.com/64525827/149655523-da7b2ce7-f9b5-400d-a334-f3d7579393e6.png">

> Be careful you have to adapt the path according to your settings, personally I use the categories to move the content to a specific folder at the end, also I prefer to indicate the complete path but it also works with `/home/$USER/local`


