# Step by step installation

## we begin !!!
> You have followed the Prerequisites so we move on to installing the script which will install all the dependencies (including Docker).

### you need a NON-root user, who has sudo rights

On Debian, you have to start by installing sudo
```
apt-get update
apt install -y sudo
```

If you only have root:
```
adduser seed # change "seed" to the user you want, and answer the questions
usermod -aG sudo seed # change "seed" to the user you want
```
Once all this is done, log out of your root session, and reconnect with the user that has just been created

Afterwards

## Installing the script
### Package update:
```
sudo apt-get update && sudo apt upgrade -y
```
### Installing Git:
```
sudo apt install -y git
```
### Cloning the script:
```
sudo git clone https://github.com/projetssd/ssdv2.git /home/${USER}/seedbox-compose
```
### Change of rights
```
sudo chown -R ${USER}: /home/${USER}/seedbox-compose
```
To run the script:
```
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

### You will get this message:
```
IMPORTANT !
==================================================== =
Your user was not in the docker group
It has been added, but you must disconnect/reconnect for the rest of the process to work
```
So disconnect then reconnect and continue with the same command
```
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

### USER INFORMATION
just answer the questions  

### Installing cloudflare
* Do you want to use Cloudflare DNS? (y/n - default n): o
``yes`` recommendation in order to update subdomains automatically  

* Your Cloudflare Email: ``cloudflare account email``
* Your Cloudflare API: ``Global API``

### Google OAuth2 with Traefik – Secure SSO for Docker services
* Would you like to secure your Apps with Google OAuth2? (y/n - default n): n
* First answer ``n`` we will come back to this later

## Finish creating the account.yml file

When installing the script it will take time and stay on for a while.

```
TASK [Add Debian repositories] ******************************************** *******************
TASK [Install common packages] ******************************************** *******************
```
> Don't worry, let it happen because it will take more or less time depending on the power of your server and you will see the script restart after a while.


### Installing Traefik
* Would you like to personalize the subdomain? (y/n): ``n``
* Choice of Authentication for traefik [Enter] 1 => basic | 2 => oauth | 3 => authelia: ``1``
For the moment, you must choose ``basic`` later you can install Oauth Google or Authlia

### The components are now all installed/adjusted, continue with the installation
* Press enter to continue, or ctrl+c to exit

# You have successfully reached the home page of the ``BRAVO`` script

### Let’s start by installing an app (or two)
* Enter the number 1) Add/Remove Apps
* Added applications (navigate with arrows and tab)
* You can select multiple applications
> Selection of applications to install:  
Press the spacebar to select applications, then tab and type ENTER to `OK`  
* once all the apps have been selected, go to OK

### Customize subdomains: (y/N)? NOT
Firstly, I advise you to keep the default subdomains.

### Back to Home
* to get out of here, you have to CTRL c

### Now you can launch the menu by doing
```
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```
#END 👍