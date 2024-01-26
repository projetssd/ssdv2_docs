# rdtclient configuration

Keep in mind that none of the torrents downloaded by qbitttorrent will physically be on your server, everything is stored on Realdebrid's servers. In short, you do not need any storage space other than that necessary to install the script and the applications.

Go to http://localhost:6500/ or https:[/](http://rdtclient:6500/)[/](http://rdtclient:6500/)[rdtclient.domain.com](http:/ /rdtclient.domain.com/), then register. Then go to settings:

Configure Rdtclient exactly as mentioned in the images below

![Capture](https://github.com/projetssd/ssdv2/assets/7422124/368ef533-5d3b-4b46-ad29-ae05be76b6b9)

1. Complete the `radarr, sonarr` categories (you can add more if you wish)
2. Increase the “parallel download” number to 100, as well as the maximum unpack process

![Capture1](https://github.com/projetssd/ssdv2/assets/7422124/60057ea0-69c1-4a98-a369-3ac51bb91a8e)

1. Choose Symlink Downloader under Download client
2. put `/data/downloads` as “download path”
3. put `/home/user/local` as “mapped path”

!!! note
    💡 IMPORTANT: The mapped folder corresponds to the local folder in which the symbolic links will be stored.


![Capture2](https://github.com/projetssd/ssdv2/assets/7422124/8b3e52be-ce2c-4941-b19c-219f47bdc6a3)

!!! note
    Specify the path of “Rclone mount path”, replacing “user” with your username


![Capture3](https://github.com/projetssd/ssdv2/assets/7422124/267c93a6-5a33-4ec3-9699-cca4365eb039)

![Capture4](https://github.com/projetssd/ssdv2/assets/7422124/63384b2a-3b7e-4790-9d35-42005eba208b)

