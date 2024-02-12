# Ombi

> > The first thing is to remove authentication on Ombi so that other users can access the site.
Rest assured, there is already an integrated connection system on Ombi.

To remove authentication:
```
nano /home/pseudo/docker-compose.yml
```
![](https://i.imgur.com/o33y2R1.png)

Remove the entire line framed in red, save then type the following command:

```
docker-compose up -d ombi-pseudo
```
Once the configuration is complete, if you use Plex you must configure it in Ombi because the basic settings are not correct:

![](https://i.imgur.com/6oVRP24.png)

Carry out a test to see that the connection is successful.

To then configure Sonarr or Radarr, you need parameters, which you find via Sonarr or Radarr:
![](https://i.imgur.com/VtdFgKK.png)

Once this information has been retrieved, return to Ombi and select TV (for Sonarr) or Movies (for Radarr), and configure according to your settings:

![](https://i.imgur.com/OHnCvyj.png)

If you click on "Load Qualities" and you retrieve your profiles, the connection is successful, then it's up to you to configure as you wish and save.