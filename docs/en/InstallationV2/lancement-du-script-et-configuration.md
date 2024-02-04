# Script launch and configuration

### Pay attention to the instructions!

The script will guide you through several configuration steps, including choosing the language, setting up folders, and managing permissions.

Alert messages may appear to inform you about specifics of the installation, such as restrictions related to restoring data and adding your user to the Docker group. It is important to read these messages carefully and proceed as instructed.

For example, when your user is added to the Docker group, you will be prompted to logout/login again for the changes to be made.

### Launching the script

To start the installation, navigate to the script directory and run it:

```bash
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

### Choice of language

You will be prompted to choose the language for the interface:

```bash
1. English/English
2. French/French
```

### Message relating to a possible installation restoration

You will get this message:

```bash
Currently, the restoration only works if the script was installed from the same directory as the one used to make the backup, and was installed on the same destination.
```

You can press ENTER to move on.

### Configuring directories

The script will request the storage directory for the container settings. Use the default path or specify a new path.

```bash
/home/YOUR_USER/seedbox
```

Remember to replace YOUR_USER with yours created beforehand.

### Adding your user to the Docker group

You will get this message:

```bash
IMPORTANT !
==================================================== =
Your user was not in the docker group
It has been added, but you must disconnect/reconnect for the rest of the process to work
```

The script automatically added the new user you created that you should currently be logged in to the Docker group.
For the modification to take effect, it is imperative to disconnect/reconnect, if you forget, here is how to do it:

- Close the Putty window to end the current session.
- Open Putty again.
- When logging in, remember to use your non-root user's login information.

### Information message

You will get this message:

```bash
Some components still need to be installed/adjusted
This operation will take several minutes depending on your system.
```

You can press ENTER to move on.

### Configuring Basic Authentication

For each message follow the indication:

```bash
↘️ Password | Press [Enter]:
```

Enter a password, then confirm with enter

```bash
↘️ Email | Press [Enter]:
```

Enter your email address, then confirm with enter

```bash
↘️ Domain | Press [Enter]:
```

Enter your domain name (without https://, example: domaine.fr), then confirm with enter

### DNS management with Cloudflare

If you want to use Cloudflare for DNS management, the script will ask you for your Cloudflare email address and your API key.

You will get this message:

```bash
Do you want to use Cloudflare DNS? (y/n)
```

We recommend that you use them so that the script takes care of their management automatically.

Answer “y”.

### Installing components

In this section, you will be guided through the installation of the various components needed for your server.

When you run the script, it may take a while and pause on the following tasks:

```
TASK [Add Debian repositories] ******************************************** *******************
TASK [Install common packages] ******************************************** *******************
```

Don't worry, just let it run, because the duration depends on the power of your server. You will see the script restart after a while.

Then you will go through the following steps:

```bash
Default address: https://traefik.cinecast.tv

Would you like to customize the subdomain? (y/n)
```

Answer "n". You can personalize them later, for easier follow-up of the guide it is not recommended to do so at this time.

---

```bash
Choice of authentication for Traefik [Enter]: 1 => basic | 2 => oauth | 3 => authelia
```

For now, choose "basic" by typing "1". You can install Oauth Google or Authelia later.

---

```bash
The components are now all installed/adjusted, continue with the installation

  1) Installation zurg - rclone - RDTclient
  2) Minimal installation without zurg
  3) Seedbox Restoration

Your choice :
```

Type "1" and confirm to select "1) Installation zurg - rclone - RDTclient".

---

```bash
API token for Zurg (https://real-debrid.com/apitoken) | Press [Enter]:
```

Provide your API key, available at http://real-debrid.com/api.

---

```bash
Customize subdomain for rdtclient: (y/n)?
```

Answer "n".

---

```bash
rdtclient authentication [Enter]: 1 => basic (default) | 2 => oauth | 3 => authelia | 4 => none
```

Answer "1", for now as seen above.

---

```bash
Folder names to create in Media (eg: Films, Series, Animated films, etc.) | Press [Enter] | Type “stop” when finished.
```

The classic configuration: Films, Series, stop.
For a setup with 4K: Films, Series, Films4K, Series4K, stop.
You must enter the name, then press Enter, and so on, until "stop". For this guide, we'll follow the example with 4K.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f38ef6a5-1048-4500-ae56-c1ae91aae0bc/b68c72dc-0f6c-45f6-b025-c7a8198df7d1/ Untitled.png)

---

After completing these steps, you will see the following message:

```
To benefit from the changes, you must disconnect/reconnect.
The installation is now complete.
To configure it or modify the applications, you can restart it:
cd /home/ubuntu/seedbox-compose
./seedbox.sh
```

Log out and log back in to apply the changes.

- Close the Putty window to end the current session.
- Open Putty again.
- When logging in, remember to use your non-root user's login information.

### You have successfully accessed the script home page. Well done. **[👍](https://emojipedia.org/thumbs-up)**