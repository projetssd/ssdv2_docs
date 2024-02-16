# Application configuration

To configure applications on your server, follow the recommended order to optimize your media integration and management.
Remember to replace “YOUR_USER” with your previously created username!

## Plex

Access Plex via `plex.votre_domaine.fr`, name your server and make sure the “Allow me to access my media outside my home” box is checked.

- **Media Library**: Add your media folders (Films, Series, 4K Films, 4K Series). For each media type, select the appropriate folder under `/home/YOUR_USER/Medias/`. Consider disabling the creation of video thumbnails to save space, this can be found in the advanced options when you add a folder.

Step by step :
1. In Plex UI, click `Add Library` to get started.
2. Select `Movies` or `TV Shows` depending on the type of folder you want to add.
3. You can rename your library if necessary (for example, for the "4K Movies" and "4K Series" folders).
4. Click `Add Folders`.
5. Select `Browse` and choose a media folder to add. The folders to add are located in `/home/ubuntu/Medias`.
6. Click on the desired folder to open it (for example, "Movies").
7. Confirm by clicking on the `Add` button.
8. Click `Advanced` to access additional settings.
9. Uncheck the `Enable video thumbnails` option to save space and resources.
10. Then you can adjust the settings according to your preferences.

By following these steps, you will have successfully added a new library to your Plex server and organized according to your preferences.

You can click next then done.

  Once you arrive at home, enter the server settings then in the left side menu go to:

- **Remote access**: Check “Specify a public port manually” (32400 by default) then click on “Try again” to allow external access.
- **Library** :
     - Analyze my library automatically: checked
         - Keeping this option checked allows Plex to automatically detect and integrate new media added to your library folders, simplifying management of your collection.
     - Run a partial scan when a change is detected: checked
         - This option optimizes resources by only scanning folders affected by changes, instead of the entire library, each time new content is added.
     - Empty the trash automatically after each scan: unchecked
         - Deactivating this option will give Zurg time to find missing content in the event of deletion of media files by Real-Debrid.
     - Allow media deletion: checked
         - By checking this option, you allow the management of media files directly from the Plex interface, providing ease of maintenance of your library.
     - Generate thumbnail video previews: never
         - Setting this option to "never" reduces the load on the server and the storage space required, as generating these thumbnails can be very resource intensive.
     - Generate thumbnails for chapters: never
         - Just like video previews, not generating thumbnails for chapters saves server resources and storage space without significantly impacting the user experience.

---

## RDTClient

Go to `rdtclient.votre_domaine.fr`, create your account and enter your Real-Debrid API key available at `http://real-debrid/api`.

Once on the home page, click on Settings, then:

- **In General**:
     - **Maximum pallel downloads**: Put `100`.
     - **Maximum unpack processes**: Also set to `100`.
     - Save your changes using the button at the bottom.
- **In Download Client**:
     - **Download client**: Select `Symlink Downloader`.
     - **Mapped path**: Indicate `/home/YOUR_USER/local`. (Replace YOUR_USER with yours)
     - **Rclone mount path**: Specify `/home/YOUR_USER/seedbox/zurg/torrents`. (Replace YOUR_USER with yours)
     - Save your changes using the button at the bottom.
- **In qBittorrent / *darr:**
     - **Post Torrent Download Action**: Choose `Download all files to host`.
     - **Post Download Action**: Select `Remove Torrent From Client`.
     - Uncheck **Only download available files on debrid provider**.
     - **Minimum file size to download**: Enter `10`.
     - Save your changes using the button at the bottom.

---

## Radarr

Go to `radarr.votre_domaine.fr` and set an authentication.

- **Media management**:
     - In `Settings` then `Media Management`, click on `Add Root Folder` and add `/home/VOTRE_USER/Medias/Films/`.
- **Download clients**:
     - In `Settings` then `Download Clients`, add qBittorrent with the following parameters:
         - **Name**: `RDTClient`
         - **Host**: `rdtclient`
         - **Port**: `6500`
         - **Username**: Your identifier on `rdtclient.votre_domaine.fr`
         - **Password**: Your password on `rdtclient.votre_domaine.fr`
         - **Category**: `radarr`

---

## Sonarr

Go to `sonarr.votre_domaine.fr` and configure authentication.

- **Media management**:
     - In `Settings` then `Media Management`, click on `Add Root Folder` and insert `/home/VOTRE_USER/Medias/Series/`.
- **Download clients**:
     - Add qBittorrent as for Radarr but with the **Category** on `sonarr`.

---

## For 4K setups (Radarr4K / Sonarr4K)

Repeat the steps above for your 4K instances, simply adjusting:

- the **Root Folder** in `Settings` then `Media Management` by the corresponding folder (Films4K / Series4K)
- the **Category** in `Download Clients` on `radarr4k` for Radarr and `sonarr4k` for Sonarr.

Then use the following SSH commands to create the directories needed for RTTClient to place the downloads:

```bash
mkdir /home/YOUR_USER/local/radarr4k
```

```bash
mkdir /home/YOUR_USER/local/sonarr4k
```

---

## Prowlarr

Go to `prowlarr.votre_domaine.fr` and set up authentication.

1. **FlareSolverr configuration**:
     - Go to `Settings`, then to `Indexers`.
     - Add FlareSolverr with the following parameters:
         - **Tags**: flaresolverr (press enter to confirm the creation of the tag in the text box, it must appear as a label)
         - **Host**: http://flaresolverr:8191/
2. **Indexer configuration**:
    
     Once FlareSolverr is added, return to the Prowlarr home page to add your indexers.
    
     If you encounter this message when adding an indexer, you need to use Flaresolverr for it to work.
    
     ![Untitled](https://i.imgur.com/WBJcOsw.png)
    
     All you have to do is add the tag you previously created in the corresponding area.
    
     ![Untitled](https://i.imgur.com/OwZBRIN.png)
    
3. **Application configuration**:
     - Go to `Settings` then `Apps`.
     - Add your Radarr (and Radarr4K) and Sonarr (and Sonarr4K) instances as follows:
         - Example for Radarr:
             - **Prowlarr Server**: http://prowlarr:9696
             - **Radarr Server**: http://radarr:7878
             - **API Key**: Recoverable here https://radarr.votre_domaine.fr/settings/general
         - Example for Radarr4K:
             - **Prowlarr Server**: http://prowlarr:9696
             - **Radarr Server**: http://radarr4k:7878
             - **API Key**: Recoverable here https://radarr4k.votre_domaine.fr/settings/general
     - Then click `Sync App Indexers` to synchronize the indexers you added in step 2 across all your instances.
---

## Overseerr

Go to `oversearr.votre_domaine.fr` and log in with your Plex account.

- **Plex server configuration**:
     - Enter the following information:
         - **Hostname or IP Address**: plex
         - **Port**: 32400
     - Click on “Save Changes”.
- **Selection of libraries**:
     - Check all your Plex libraries.
     - Click “Continue”.
- **Addition of Radarr(4K) / Sonarr(4K) instances**:
     - For Radarr:
         - Check "Default Server".
         - Leave "4K Server" unchecked.
         - Fill in the following details:
             - **Server Name**: Radar
             - **Hostname or IP Address**: radarr
             - **Port**: 7878
             - **Use SSL**: unchecked
             - **API Key**: Recoverable here https://radarr.votre_domaine.fr/settings/general
                 - Once completed, click on the “Test” button to unlock the rest.
             - **Base URL**: empty
             - **Quality Profile**: according to your preference
             - **Root Folder**: the proposed choice
             - **Minimum Availability**: according to your preference
             - **Tags**: empty
             - **Enable Scan**: checked
             - **Enable Automatic Search**: checked
             - **Tag Requests**: unchecked
     - For Sonarr:
         - Check "Default Server".
         - Leave "4K Server" unchecked.
         - Fill in the following details:
             - **Server Name**: Sonarr
             - **Hostname or IP Address**: sonarr
             - **Port**: 8989
             - **Use SSL**: unchecked
             - **API Key**: Recoverable here https://sonarr.votre_domaine.fr/settings/general
                 - Once completed, click on the “Test” button to unlock the rest.
             - **Base URL**: empty
             - **Quality Profile**: according to your preference
             - **Root Folder**: the proposed choice
             - **Language Profile**: Deprecated
             - **Tags**: empty
             - **Anime Quality Profile**: according to your preference
             - **Anime Root Folder**: the proposed choice
             - **Season Folders**: checked
             - **Enable Scan**: checked
             - **Enable Automatic Search**: checked
             - **Tag Requests**: unchecked

### Configuration of Radarr(4K) / Sonarr(4K) instances

- **Added Radarr(4K) / Sonarr(4K) instances**
    
     If you have configured Radarr(4K) / Sonarr(4K) instances in your system, here is how to integrate them with Overseerr:
    
     - **Default Server**: Check the "Default Server" box for each Radarr(4K) / Sonarr(4K) instance to indicate that it is your main server.
     - **4K Server**: Also check the “4K Server” box to specify that these instances are dedicated to 4K content.
     - **Server Name**: For each instance, specify the server name as follows:
         - For Radarr4K: "Radarr 4K"
         - For Sonarr4K: "Sonarr 4K"
     - **Hostname or IP Address**: Use the following addresses depending on the instance you are configuring:
         - For Radarr4K: "radarr4k"
         - For Sonarr4K: "sonarr4k"
     - **API Key**: Retrieve the respective API key from the following links:
         - For Radarr4K: https://radarr4k.votre_domaine.fr/settings/general
         - For Sonarr4K: https://sonarr4k.votre_domaine.fr/settings/general

By following these steps, you will successfully configure your new Radarr4K/Sonarr4K instances in Overseerr, ensuring that the settings are tailored to each instance, including the specific API key. This will allow you to manage 4K content separately.

### Configuring Overseerr general settings

- **Configuration of general parameters**:
     - Go to `Settings`.
     - Under "Display Language", select "French".
     - Under "Discover Region", choose "France".
     - Under "Discover Language", select "all languages".
     - Click "Save changes".
- **Automatic validation of requests** (Optional):
     - If you want your users' requests to be automatically validated, go to `Users` and check "Validate automatically".
     - You can also check "Report problems" to enable the reporting functionality.
     - Click "Save".