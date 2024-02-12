# Trakt.tv-et-Kitana

Warning: first writing.

## You want to synchronize your readings with your Trakt.tv account, you are at the right address.

### prerequisites:
* a “free” trakt.tv account
* a “free” plex account

as you have understood, there is no need to be VIP, we will not use webhooks

> Advantage of this solution (there is another but I won't talk about it) you will be able to synchronize each user of your plex server with their own Trakt.tv account

## we begin :

### Installing the trakt plugin (Plex-Trakt-Scrobbler)

Download the latest release of the Trakt.tv plugin:
````
wget https://github.com/trakt/Plex-Trakt-Scrobbler/archive/master.zip -O Plex-Trakt-Scrobbler.zip
````
Extract the downloaded ZIP archive:
````
unzip Plex-Trakt-Scrobbler.zip
````

Move: (replace USER your your user)
````
cp -r Plex-Trakt-Scrobbler-*/Trakttv.bundle "/opt/seedbox/docker/USER/plex/config/Library/Application Support/Plex Media Server/Plug-ins"
````

Change of rights:
````
cd "/opt/seedbox/docker/USER/plex/config/Library/Application Support/Plex Media Server/Plug-ins/"
````
````
chown -R 1000:1000 Trakttv.bundle && chmod -R 775 Trakttv.bundle
````

Restart Plex Media Server:
````
docker restart plex
````

### Installing Kitana:

Go to the script menu to add the “kitana” application


### Solution configuration:

Go to the following address [trakt-scrobbler](http://trakt-for-plex.github.io/configuration/#/login)

Connection to your plex account:

![login](https://user-images.githubusercontent.com/64525827/119456089-94f88580-bd3a-11eb-946a-e2f2eb956c94.png)

then select your server in the “connect” window

![configuration](https://user-images.githubusercontent.com/64525827/119456303-d7ba5d80-bd3a-11eb-90a2-0eb725f0cf9f.png)  
click on Rules and reproduce this  
![rules](https://user-images.githubusercontent.com/64525827/119456424-f28cd200-bd3a-11eb-8d3a-ffcb8caafc57.png)  

In "Accounts" you must add the different accounts that you wish to synchronize with Trakt.tv

> IMPORTANT: you must follow the following instructions exactly  

For Plex:
Click on the link https://plex.tv/pin to enter the code on the screen, wait for it to be taken into account then SAVE with the blue button at the top right.  

For Trakt:
Click on “Get PIN” connect to your Trakt account to see the generated code, then paste it in the config and click on “Sign in” then SAVE with the blue button

Expected result :

![authentication](https://user-images.githubusercontent.com/64525827/119457702-43e99100-bd3c-11eb-9b8b-5c64ecafe6b9.png)  

## Continuation of the installation with Kitana

Go to the address of your kitana (example: https://kitana.votrendd.fr)

log in with your PLEX account  
![kitana connect](https://user-images.githubusercontent.com/64525827/119457858-6c718b00-bd3c-11eb-86d7-a7e0982448bc.png)  

Click on the local IP address “172.18.0.xx” then on the trakt plugin  

In the "sync" tab you have several possibilities, I present two of them:

This choice allows you to retrieve the view history from Trakt in order to mark as seen in Plex everything that is marked as seen in Trakt  
![Pull](https://user-images.githubusercontent.com/64525827/119458238-d12ce580-bd3c-11eb-9196-237f146ed463.png)  


This choice allows you to send to Trakt all content marked as seen in your Plex  
![Push](https://user-images.githubusercontent.com/64525827/119458428-089b9200-bd3d-11eb-8543-2d9b1dd0cfea.png)


> To check that it is working correctly, simply start a playback and go to trakt.tv, you should see this  
![Screenshot 2021-05-25 at 09 41 58](https://user-images.githubusercontent.com/64525827/119458868-79db4500-bd3d-11eb-8450-9df1430724e6.png)

End 👍🏻