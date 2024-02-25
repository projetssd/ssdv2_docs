# Seed the symlinks downloaded by RDTClient

## Change made

It is now possible to seed the **symlink** of files downloaded by RDTClient.
This feature builds on the already existing “Copy added torrent files” setting which has been revisited.
If this feature is enabled (by specifying a path in the settings), RDTClient will transfer the original .torrent files to a dedicated seed client.
If disabled, RDTClient will function as if no changes had been made.

**Compatible with AMD64 and ARM64.**
Docker image: `systr0/rdt-client-2.0.39:latest`

The Docker images are provided for informational purposes, you have the possibility to automatically install this modified version as well as Rtorrentvpn directly via the script!

## Configuration

1. **Configuring the import path**:
    - In the RTTClient settings, specify the path where the .torrent files should be copied and imported.
![image](https://github.com/systr0/rdt-client-2.0.39/assets/158838664/e27f08ba-f8b7-44e3-950d-b6acc8f40de2)

2. **Installation of a torrent client for seed (e.g. Rtorrentvpn)**:
    - Install Rtorrentvpn (tested and compatible) or a torrent client with the same automatic import specifications.
Docker image: `binhex/arch-rtorrentvpn:latest`

3. **VPN configuration**:
    - Open the port for incoming connections from your torrent client **over the VPN**.

4. **Rtorrentvpn client configuration example**:
    - Enable AutoWatch in Settings under AutoTools.
    - Define the path to monitor, identical to that configured in RDTClient for copying .torrent files.
    - Make sure the “Start download automatically” option is enabled.
![image](https://github.com/systr0/rdt-client-2.0.39/assets/158838664/f10a5814-72af-4c18-b579-ad8d3e708997)


5. **Adaptation for other torrent clients**:
    - Repeat step 4 above, adapting according to the torrent client used, so as to reproduce the process of monitoring a folder, in order to import the .torrent files placed there.

## Explanation of operation

When a path is specified in the RDTClient settings for the "Copy added torrent files" option:
- **Creation of additional symbolic links**: At the end of the download by RDTClient, during the creation of symlinks for import by *arrs, creation of additional symlinks for the seed client in the path defined where must be copied the .torrent file.

- **Modified management of .torrent files**:
   - .torrent files are temporarily stored outside the path monitored by the seed client to avoid premature imports.
A folder is created where the Mapped path parameter is set in Download Client of RDTClient.
Example: `Mapped_path_Download_Client/tempTorrentsFiles`
   - Following the creation of the symbolic links, the .torrent file is moved to the path monitored by the seed client so that it can be imported.
   - Import then start checking files already present due to the symlink which points to Real-Debrid, then seed files.
  
- **In case of failure to create symlinks**: The .torrent file will not be moved from the temporary 'tempTorrentFiles' folder to prevent the seed client from importing and downloading (again if already downloaded by RDTClient because not in cache) files.