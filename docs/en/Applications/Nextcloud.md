#Nextcloud

## How to install & configure Nextcloud

#### About mariadb and the database

⚠️ TON_USER = YOUR user, in lower case ⚠️

⚠️ ndd.tld = YOUR domain, in lowercase ⚠️

⚠️ Commenting means adding a # at the start of the line so that the config file does not take it into account ⚠️



In order to avoid future errors and optimize your installation, it is better to opt for an installation with Mariadb and not SQLite!

Here is the information needed for an installation with Mariadb:

![505-828-max](https://user-images.githubusercontent.com/64525827/105355834-f2e15900-5bf2-11eb-9d55-19d4eb658830.jpg)

* Login: choose yours and leave toto alone :0)
* Password: choose a **strong** password!
* Data directories: `/data `
* Database user: `nextcloud`
* Database password: `nextcloud`
* Database name: `nextcloud`
* Database host: `db-nextcloud`

Click on **Install**, you are free to leave the recommended applications checked. It is always possible to install them afterwards.

#### Remember to update your Nextcloud before any other operation!!
#### This tutorial is valid for the latest version: 20.0.4


### Set security alerts

After installing Nextcloud it is necessary to adjust the security alerts present in:

Settings / Overview / Security warnings & configuration

https://nextcloud.ndd.tld/settings/admin/overview

![1582-500-max](https://user-images.githubusercontent.com/64525827/105355836-f379ef80-5bf2-11eb-95a0-1a166d368729.jpg)



For the alert:
“The “Strict-Transport-Security” HTTP header is not configured for at least “15552000” seconds. To enhance security, we recommend enabling HSTS as described in our security tips ↗. »

`nano /opt/seedbox/docker/TON_USER/nextcloud/conf/nginx/site-confs/default`

Add this line:
`add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";`

Like this (for example):

![769-132-max](https://user-images.githubusercontent.com/64525827/105355840-f4128600-5bf2-11eb-8e64-a454f0ac9b9c.jpg)

Save the edited file.

We relaunch Nextcloud and its database by doing:

`docker restart nextcloud db-nextcloud`



For the alert: The database has some missing indexes. Adding indexes to large tables can take some time. They are therefore not added automatically.

`docker exec -ti nextcloud bash`

`occ db:add-missing-indices`



For the alert: Some columns in the database have not been converted to big int. Changing the column type in large tables can take a long time, so they were not converted automatically.

`docker exec -ti nextcloud bash`

`occ db:convert-filecache-bigint` Validate

Following columns will be updated:

* federated_reshares.share_id
* share_external.id
* share_external.parent

This can take up to hours, depending on the number of files in your instance!
Continue with the conversion (y/n)? Choose y, of course!

You get your sacred green **V** again ;)

![1575-187-max](https://user-images.githubusercontent.com/64525827/105355841-f4128600-5bf2-11eb-97c6-80a48fb09b02.jpg)

For the alert:
> Your installation does not have a default region prefix. This is necessary to validate phone numbers in profile settings without a country code. To allow numbers without a country code, please add "default_phone_region" with the respective ISO 3166-1 code of the region in your configuration file.

You must modify the config.php file:
```
nano /opt/seedbox/docker/TON_USER/nextcloud/conf/www/nextcloud/config/config.php
```
add to last line
```
'default_phoneregion' => 'FR',
```
example:
```
  'dbhost' => 'XXX',
  'dbport' => '',
  'dbtableprefix' => 'oc',
  'mysql.utf8mb4' => true,
  'dbuser' => 'XXX',
  'dbpassword' => 'XXX',
  'installed' => true,
  'default_phone_region' => 'FR',
```
Save the edited file.

We relaunch Nextcloud and its database by doing:

```
docker restart nextcloud db-nextcloud
```

### Add dark mode to Nextcloud


Probably the most followed and coolest app for a dark theme.

https://apps.nextcloud.com/apps/breezedark


It works like any other app in the Nextcloud store.

Here's a preview:

![screenshot](https://user-images.githubusercontent.com/64525827/105355843-f4ab1c80-5bf2-11eb-9c2c-f94ab3a3221c.png)

In the application part of Nextcloud, you just need to enter **dark** as a keyword and install it.

Clear the cache and reload the page to see the effects!




### Mount home in Nextcloud

https://mondedie.fr/d/10779-docker-monter-le-home-dans-nextcloud

### Mount the home in Nextcloud without modifying files

It's very simple, just go to the **Applications** part of your Nextcloud installation.
Search for the **External storage support** application and install it.

Once installed, go to **Settings** then in the left column in **External storage**:

Now fill in the requested parameters:

* A folder name: at your convenience
* In external storage: choose... local :)
* Authentication: none
* Configuration: here you will need to enter the path that leads to your home.

_For those who use Gdrive: /home/**TON_USER**/Medias/_

_For those who **NOT** use Gdrive: /home/**TON_USER**/local/_
* Available for: it's up to you, otherwise leave it by default if there are no restrictions

So that you can share your files and/or folders, make sure to click on the **...** as shown in the screenshot and click on **Allow sharing**

Check that a green **V** is present as in the screenshot, you're done!





### Double authentication | 2fa

Increase the security of your account with double authentication (two-factor authentication or 2fa)!

![](https://raw.githubusercontent.com/nextcloud/twofactor_totp/dd1e48deec73a250886f35f3924186f5357f4c5f/screenshots/enter_challenge.png)

Go to the Applications section of your Nextcloud.

Find and install: **Two-Factor TOTP Provider**
Go to **Settings**
Choose **Security** at the top left (https://ndd.tld/settings/user/security)

At this step, all you need to do is launch your favorite application for double authentication and scan the QR Code.
In this case we will use Google Authenticator, available here: https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=fr

Now that the application is launched, you should see this:

Click on **Get started**
Select **Scan a barcode**

Your account is added!

Don't forget to enter the code returned by Google Authenticator in Nextcloud to **verify** everything:


***
# Nextcloud with Talk
***


We start by updating the script:

`cd /opt/seedbox-compose/`

`git pull`


We install Nextcloud:

`cd /opt/seedbox-compose/`

`./seedbox.sh`

Choose option 2, then option 1. Select Nextcloud in the list of applications with the **Space** bar, using the TAB(ulation) key on your keyboard, select **OK** and validate.


Go to Nextcloud and download **Talk** in the applications section:

https://nextcloud.ndd.tld/settings/apps and type in search “**Talk**”.


Once installed you must go to this address, which corresponds to **Parameters** / **Discussion** (bottom left):

https://nextcloud.ndd.tld/settings/admin/talk

Fill in the information as shown in the screenshot:

* **STUN servers**: the IP of your server followed by the port: 3478
* **TURN servers**: the IP of your server followed by the port: 3478
* **Secret**: indicate the code after **static-auth-secret** in your turnserver.conf file:

`nano /opt/seedbox/docker/YOUR_USER/coturn/turnserver.conf`  

**Important**  
Consider opening port 3478 in iptables  

It's finished, Talk is now functional.


***
# Nextcloud with Collabora
***

![](https://nextcloud.teamsyno.com/s/xmkMexGHMoxJkop/preview)

## You already have Nextcloud installed with the script (without data loss)

We start by updating the script:

`cd /opt/seedbox-compose/`

`git pull`





Now we will copy the nextcloud.yml file:

`cp /opt/seedbox-compose/includes/dockerapps/nextcloud.yml /opt/seedbox/conf`






We reset Nextcloud:

`cd /opt/seedbox-compose/`

`./seedbox.sh`

Choose option 2, then option 3. Select Nextcloud in the list of applications with the **Space** bar, using the TAB(ulation) key on your keyboard, select **OK** and validate.






Go to Nextcloud and download **Collabora** in the applications section:

https://nextcloud.ndd.tld/settings/apps

Once installed, go to the configuration section of **Collabora**:

https://nextcloud.ndd.tld/settings/admin/richdocuments

![](https://nextcloud.teamsyno.com/s/QeD2qzCBm5xXrM4/preview)

Indicate your subdomain as shown in the screenshot: https://collabora.ndd.tld and validate with **Apply**.

## You do not yet have Nextcloud installed



We start by updating the script:

```cd /opt/seedbox-compose/ && git pull```


We install Nextcloud:

```cd /opt/seedbox-compose/ && ./seedbox.sh```


Choose option 2, then option 1. Select Nextcloud in the list of applications with the **Space** bar, using the TAB key on your keyboard, select **OK** and validate.


Go to Nextcloud and download **Collabora** in the applications section:

https://nextcloud.ndd.tld/settings/apps

Once installed, go to the configuration section of **Collabora**:

https://nextcloud.ndd.tld/settings/admin/richdocuments

Indicate your subdomain as shown in the screenshot: https://collabora.ndd.tld and validate with **Apply**.


### Unauthorized WOPI host

You may one day get an error like this: "Unauthorized WOPI host".

To fix this, follow this procedure:

* Output the file: `docker cp collabora:/etc/loolwsd/loolwsd.xml /opt/loolwsd.xml`
* Then edit the loolwsd.xml file: `nano /opt/loolwsd.xml`

Update the **storage** tag by adding two lines, one for the IP of your server, the other for the domain of your Nextcloud instance:

```<host desc="Regex pattern of hostname to allow or deny." allow="true">1\.2\.3\.4</host>```

```<host desc="Regex pattern of hostname to allow or deny." allow="true">nextcloud.yourdomain.tld</host>```

* Reinject the loolwsd.xl file: ```docker cp /opt/loolwsd.xml collabora:/etc/loolwsd/loolwsd.xml```

It's finished and functional :)