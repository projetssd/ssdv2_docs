# Google OAuth2 implementation

Google OAuth2 allows you to use your Google account to sign in to your services.

Using Google OAuth with Traefik whitelists accounts, implements Google's 2FA standard, and provides single sign-on (SSO) to your services.  

This not only offers the advantage of not having frequent connection requests, but also improves security.


## Google OAuth2 Service configuration

> #### Note  
> For those who use Cloudflare, the creation of the CNAME is automated by the script, for others remember to create it with your Registrar.  
![01-clouldflare-dns-records-for-traefik-google-oauth-740x265](https://user-images.githubusercontent.com/64525827/105626357-56f06100-5e2f-11eb-815d-684ea953c4c8.png)


### We will create a project again this time for traefik Google oAuth

* Go to the following address and log in with your Gsuite account:  
[Google Apps Script API](https://href.li/?https://console.cloud.google.com/cloud-resource-manager)

> WARNING: You must be sure and certain that you are connecting to the correct Google account.
If you have several, then connect in private browsing window!

* ### Click Create Project
![create_a_project](https://user-images.githubusercontent.com/64525827/119948392-14839000-bf99-11eb-96a0-c7509bde74e9.png)  
<br><br>
* ### Enter the project name ``oauth`` then click on Create  
![creation_projet](https://user-images.githubusercontent.com/64525827/119948566-3f6de400-bf99-11eb-8ddf-ce61d54a76b4.png)  
<br><br>
* ### In the notification at the top right, click on "select a project"  
![notification](https://user-images.githubusercontent.com/64525827/119949044-c28f3a00-bf99-11eb-8c9f-3342f6c0649e.png)  

### After installation click on “credentials”  
![username](https://user-images.githubusercontent.com/64525827/119950352-0a629100-bf9b-11eb-923c-fd49240cc6e0.png)
<br><br>
In the new window, click on “Create identifiers” then on “OAuth client ID”
![creation_identifiant](https://user-images.githubusercontent.com/64525827/119950515-33832180-bf9b-11eb-9e12-14995ab54f3c.png)  
<br><br>
There is an intermediate step, click on "Configure authorization screen"  
![configure oauth](https://user-images.githubusercontent.com/64525827/119950915-af7d6980-bf9b-11eb-9d4a-f51a90294427.png)  
<br><br>
then select "external" and Create  
![external](https://user-images.githubusercontent.com/64525827/119951092-dc318100-bf9b-11eb-8fb2-79b59052fecf.png)
<br><br>
In the new window, fill in the fields:
* Application name => ``same as project name``
* User support email address => ``select that of the google account``
* Developer contact details (email address) => ``Enter your email``  

### On each step, click at the bottom on save  
![steps](https://user-images.githubusercontent.com/64525827/119951704-8a3d2b00-bf9c-11eb-9632-8c3698a45e5d.png)
<br><br>
Once finished, click again on “Credentials” on the left of the screen  
Then :
* Create logins
*OAuth client ID
* Application type => ``Web application``
* Name => ``same as project name``
* URI => ``https://oauth.example.com/_oauth``  
![oauth](https://user-images.githubusercontent.com/64525827/119953309-2451a300-bf9e-11eb-9a85-fb8414e3c667.png)   
<br><br>

### You will then need these identifiers to create your Rclone.  
![identifians_ok](https://user-images.githubusercontent.com/64525827/119952283-236c4180-bf9d-11eb-9937-86ca1d319f1c.png)
<br><br>


* ### Copy the CLIENT ID and SECRET CUSTOMER onto a notepad  
![google-apps-script-api-client-id-et-secret](https://user-images.githubusercontent.com/64525827/105181463-1ee5d700-5b2c-11eb-85b1-55a14668ea34.jpeg)

### You will need these identifiers later.  


If you closed the window with your identifiers, you can find them in the drive project identifier section. [Dashboard API](https://href.li/?https://console.developers.google.com).  

![google-projects-api-ids](https://user-images.githubusercontent.com/64525827/105181488-2907d580-5b2c-11eb-9b8b-cc39e3e2ed04.jpg)


***
> ## BONUS
***
#### Google OAuth and NZB360, LunaSea etc...  
The idea is to use specific rules for example, if the request header contains the sabnzbd API, radarr, sonarr etc.. we bypass the authentication.  

As a result, it is an amalgamation of middleware with and without authentication which, more generally, triggers Google Oauth authentication via the web while allowing access to NZB360 and preserving access security.   

The procedure is very simple, you just need to change the traefik labels in the sabnzbd, lidarr, sonarr, radarr, rutorrent apps.  

#### Sabnzbd  

Before

```
traefik.enable: 'true'
## HTTP Routers
traefik.http.routers.sabnzbd-rtr.entrypoints: 'https'
traefik.http.routers.sabnzbd-rtr.rule: 'Host(`sabnzbd.domain`)'
traefik.http.routers.sabnzbd-rtr.tls: 'true'
## Middleware
traefik.http.routers.sabnzbd-rtr.middlewares: "{{ 'chain-oauth@file' if oauth_enabled | default(false) else 'chain-basic-auth@file' }}"
## HTTP Services
traefik.http.routers.sabnzbd-rtr.service: 'sabnzbd-svc'
traefik.http.services.sabnzbd-svc.loadbalancer.server.port: '8080'
```
After  
```
traefik.enable: 'true'
traefik.http.routers.sabnzbd-rtr-bypass.entrypoints: 'https'
traefik.http.routers.sabnzbd-rtr-bypass.rule: 'Query(`apikey`, `api_de_sabnzbd`)'
traefik.http.routers.sabnzbd-rtr-bypass.priority: '100'
traefik.http.routers.sabnzbd-rtr-bypass.tls: 'true'
## HTTP Routers Auth
traefik.http.routers.sabnzbd-rtr.entrypoints: 'https'
traefik.http.routers.sabnzbd-rtr.rule: 'Host(`sabnzbd.domain`)
traefik.http.routers.sabnzbd-rtr.priority: '99'
traefik.http.routers.sabnzbd-rtr.tls: 'true'
## Middleware
traefik.http.routers.sabnzbd-rtr-bypass.middlewares: 'chain-no-auth@file'
traefik.http.routers.sabnzbd-rtr.middlewares: 'chain-oauth@file'
## HTTP Services
traefik.http.routers.sabnzbd-rtr.service: 'sabnzbd-svc'
traefik.http.routers.sabnzbd-rtr-bypass.service: 'sabnzbd-svc'
traefik.http.services.sabnzbd-svc.loadbalancer.server.port: '8080'
```
Don't forget to put the API key in place of api_de_sabnzbd. Then reset with the script

#### sonarr, radarr, lidarr  
Same procedure as for sabnzbd except a label which we will modify.
```
traefik.http.routers.sonarr-rtr-bypass.rule: 'Headers(`X-Api-Key`, `api_sonarr`)'
```  
#### rutorrent
Replace your middleware with the following:
```
traefik.enable: 'true'
traefik.http.routers.rutorrent-rtr-bypass.entrypoints: 'https'
traefik.http.routers.rutorrent-rtr-bypass.rule: 'Path(`/RPC2`)'
traefik.http.routers.rutorrent-rtr-bypass.priority: '100'
traefik.http.routers.rutorrent-rtr-bypass.tls: 'true'
## HTTP Routers Auth
traefik.http.routers.rutorrent-rtr.entrypoints: 'https'
traefik.http.routers.rutorrent-rtr.rule: 'Host(`rutorrent.domain`)'
traefik.http.routers.rutorrent-rtr.priority: '99'
traefik.http.routers.rutorrent-rtr.tls: 'true'
## Middleware
traefik.http.routers.rutorrent-rtr-bypass.middlewares: 'chain-basic-auth@file'
traefik.http.routers.rutorrent-rtr.middlewares: 'chain-oauth@file'
## HTTP Services
traefik.http.routers.rutorrent-rtr.service: 'rutorrent-svc'
traefik.http.routers.rutorrent-rtr-bypass.service: 'rutorrent-svc'
traefik.http.services.rutorrent-svc.loadbalancer.server.port: '8080'
```
As a security measure, we add a basic authentication layer for access to nzb360  
So to make sonarr, radarr, lidarr work on both NZb360 and LunaSea you modify the label in this way

```
traefik.http.routers.sonarr-rtr-bypass.rule: 'Headers(`X-Api-Key`, `b12d1732186a4376b80bdb3875a0f39d`) || Query(`apikey`, `b12d1732186a4376b80bdb3875a0f39d`)'
```