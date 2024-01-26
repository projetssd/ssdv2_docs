# Plex

## In case you use Gdrive or Sharedrive storage.
> You must indicate the following path for your libraries in order to then use [Plex_Autoscan](Plex-Autoscan.md)

<img width="721" alt="plex folder data" src="https://user-images.githubusercontent.com/64525827/105615683-c1bf7f00-5dd2-11eb-8570-3a899bae1654.png">

### Disable DLNA

![SHhl2TT](https://user-images.githubusercontent.com/64525827/105335857-d6d0be00-5bd8-11eb-929d-327bf1e75ea5.png)

### Disable thumbnail generation

Enable media removal to ensure plex_dupefinder works properly. Disable periodic scanning, manual scanning is no longer recommended since there is Plex Autoscan. Disable the “Empty trash automatically after each scan” option

![lGTktQl](https://user-images.githubusercontent.com/64525827/105335927-ecde7e80-5bd8-11eb-833a-0ff344c1c857.png)

### Network settings

![F64pHKz](https://user-images.githubusercontent.com/64525827/105335979-fb2c9a80-5bd8-11eb-9a63-668c92ca2e40.png)


***

> TIP If you need to generate a token for plex

```
/opt/seedbox-compose/includes/config/roles/plex_autoscan/plex_token.sh
```
 
enter your plex account and it gives you the token

***