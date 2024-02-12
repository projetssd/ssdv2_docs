# Organize

#### What is Organizr?

Organizr allows you to configure “tabs” that will all load into a single web page.
You can then work on your server with ease and switch from one service to another very easily!
This is also what we call a dashboard.

#### A brief aside on authentication

Organizr has its own authentication page, you can very well deactivate Auth (the window where you must enter your user and password created during the script) if you have user accounts so as not to reveal your administrator account. Here are the steps to follow:

`nano /opt/seedbox/conf/organizr.yml`





We comment on these 4 lines by adding a # in front of the lines in question:

`#traefik.frontend.auth.basic: '{{ passwd.stdout if (not oauth_client.stat.exists) | default(false) else omit }}'`

`#traefik.frontend.auth.forward.address: 'http://oauth:4181'`

`#traefik.frontend.auth.forward.authResponseHeaders: 'X-Forwarded-User'`

`#traefik.frontend.auth.forward.trustForwardHeader: 'true'`





Once this is done, you must reset the container as follows to validate all the changes made:

`cd /opt/seedbox-compose/`

`./seedbox.sh`

Choose option 2 (Add/Remove Apps)

Choose option 3 (Reset Container)

Choose Organizr and confirm with OK





#### What might Organizr look like once configured and installed?

Everything obviously depends on how you are going to configure your dashboard, here is an example:

![](https://user-images.githubusercontent.com/16184466/53615856-35cc5a80-3b9d-11e9-8428-1f2ae05da2c9.png)

This is a classic Organizr presentation. It is possible to include Grafana on the homepage. This is [the subject of this tutorial](Varken-Grafana-Influxdb).

You will then obtain a mixture of Organizr & Grafana:

![](https://nextcloud.teamsyno.com/s/HrTfHFBnpJWQnZk/preview)





#### Configure Organizr: Part 1

You arrive on this page (https://organizr.ndd.tld), and you must choose your installation type.

There are two types of installations:

![](https://nextcloud.teamsyno.com/s/yDJqT7QNJsznRzP/preview)

**Personal** or **Professional**

**Staff** hides nothing — no restrictions

**Professional** caches media items [Plex, Emby, etc.]

Choose what suits you and your needs.

Click on **next**.






**Administrator info.**

![](https://nextcloud.teamsyno.com/s/KRFBgmDxw8YJFJ7/preview)

Indicate your **username**: here: **Marcel**

Indicate your **email**: In this regard, it is advisable to use the one linked to your Emby or Plex account.

Indicate **your password**: Preferably a strong password. [You can create one here!](https://www.motdepasse.xyz/)

Click on **Next**.






**Administrator creation**

![](https://nextcloud.teamsyno.com/s/nCzafGiRXweDWQn/preview)

**Hash key**: between 2 and 30 characters. Let's put 30 characters, precisely. The frame should be green, if you exceed 30 characters, it will be red, you will need to delete the excess characters.

**Registration password**: re-enter the same password created in the previous step.

**API key**: it's already filled out, you can move on to the next step.

Click on **Next**






**Creating the administrator, second part**

![](https://nextcloud.teamsyno.com/s/RX6GdQ4Bsr2wwyF/preview)

**Database name**: choose a database name.

**Database location**: as shown in the screenshot, you must place the database outside the root of the web folder. You can copy/paste the first example `/config/www/db`.

Click on **Test/Create Path**, you should get the message announcing **Path is good to go**.

We go to the next page by clicking on **Next**.





**Administrator creation, part three**

![](https://nextcloud.teamsyno.com/s/XSEKKtxqPpBnStx/preview)

Now you can click **Finish**!






You are now on the Organizr authentication page, depending on whether you have deactivated Auth or not, you will first need to enter your credentials created during the script if it is not deactivated.

![](https://nextcloud.teamsyno.com/s/9nwXYdtyyzzGJCn/preview)

Once you have entered your login and password, click on **Connection**.





You arrive on the general page of **Organizr Settings**. This is where it really begins.

![](https://nextcloud.teamsyno.com/s/8GdZereG9m8RnzT/preview)





#### Configure Organizr: Part 2

Given the many possibilities that Organizr offers, we will go through the basics so that you have a good functional dashboard and we invite you to join us on [Discord](https://discord.gg/v5dZHB5) if you have other questions that will not necessarily be addressed here.

On the other hand, following these steps will familiarize you with the interface which is not very complicated and you will quickly get the hang of it :)





#### Create tabs

Definitely one of the most important settings in Organizr!

It is thanks to the tabs that you will be able to display the icons of the corresponding services.

**I invite you to activate Homepage before anything else** :)

![](https://nextcloud.teamsyno.com/s/ojcDJYa8JaPjpym/preview)





In the **Tab Editors** section, click on ![](https://nextcloud.teamsyno.com/s/jztJFy2dmXrzKwt/preview)

![](https://nextcloud.teamsyno.com/s/CJjtSsz8qa7MYHY/preview)





We will add the ruTorrent tab for example.

![](https://nextcloud.teamsyno.com/s/rxA3SmmEc9p65yN/preview)

**Tab name**: **ruTorrent** or whatever you like

**Tab URL**: indicate the URL of your ruTorrent in the form https://rutorrent.ndd.tld

**Choose image**: either type in rutorrent search or paste this directly into **Tab image**:

 `plugins/images/tabs/rutorrent.png`

Validate with **Add a tab**.





Reload your page by pressing **F5**, you can see the appearance of your first ruTorrent tab on the left side of your Organizr. Good game!

![](https://nextcloud.teamsyno.com/s/icPzxfcMX9YMkTm/preview)




Now let's add Plex!

We will add the Plex tab in the same way as ruTorrent.

In the **Tab Editors** section, click on ![](https://nextcloud.teamsyno.com/s/jztJFy2dmXrzKwt/preview)

![](https://nextcloud.teamsyno.com/s/xep3rL4pNCpzTbp/preview)

**Tab Name**: **Plex** or whatever you like

**Tab URL**: indicate the Plex URL in the form https://plex.ndd.tld

**Choose image**: either type in **Plex** search or paste this directly into **Tab image**:

`plugins/images/tabs/plex.png`

Validate with **Add a tab**.

Reload your page by pressing F5, you can see the appearance of your second **Plex** tab on the left side of your Organizr. Yeah!

You can now add tabs as you wish, the principle is still the same.


#### Organize tabs



It is possible to organize the order of your tabs.

![](https://nextcloud.teamsyno.com/s/dP2Rg4TbptMkKoi/preview)

By hovering your mouse over the icon, you will see three small lines![](https://nextcloud.teamsyno.com/s/mcATj2MCsM8yrsY/preview), enter the tab by holding down the left click of your mouse, move your tab up or down.




#### Personalization

Like any good self-respecting dashboard, there is a way to personalize the interface.

Here is the customization part:

![](https://nextcloud.teamsyno.com/s/E8ey8x3J3xsJaPE/preview)

**Top Bar**

This category allows you to modify 3 elements.

* **Logo**: allows you to change the Organizr logo OR leave the ORGANIZR V2 title (which you can modify of course, that's the next step).

To use a logo instead of the title, simply check **Use logo instead of title**.

* **Title**: by default ORGANIZR V2, adapt according to your needs.
* **Meta Description**: the description of this part informs that: Used to set the description for SEO meta tags.

To make it simpler:

> Search engine optimization, also called SEO (from English Search Engine Optimization) is a set of techniques aimed at promoting understanding of the theme and content of one or all of the pages of a website by search engines.




In this example, we will personalize the dashboard with a small **Seedbox Docker Script** logo.

In the **Logo** section, paste the URL of the desired image, check **Use the logo instead of the title** and validate with **Save**:

![](https://nextcloud.teamsyno.com/s/2NGJ9RBB4MWem6r/preview)

Be sure to refresh the page to see the logo appear in the upper left corner.



If you want to change the background of the login page, still in **Personalize**, **LoginPage** part:

![](https://nextcloud.teamsyno.com/s/qzby3ePFnwBPwDD/preview)



You paste your image URL into the **Connection Background** part. When it's done, you log out of your Organizr session and admire the result.

![](https://nextcloud.teamsyno.com/s/Q2bJBWYHnWJtgND/preview)




View Ombi queries on the Organizr Homepage:

![](https://nextcloud.teamsyno.com/s/aBEfJkPCP8kFDzA/preview)





Go to Ombi: https://ombi.ndd.tld/Settings/Ombi

We recover the **Api Key**:

![](https://nextcloud.teamsyno.com/s/Q7CR72Qny32jpam/preview)




We return to Organizr: **Settings**, **Tab editors**, **Home page elements**, we click on Ombi.

![](https://nextcloud.teamsyno.com/s/fiJ5FYYBbi2ie2D/preview)

We start by checking **Activate** in the first tab.





In **Connection** you put the URL of your Ombi and paste the previously copied API KEY.

![](https://nextcloud.teamsyno.com/s/rsgscHqgjkXR4s2/preview)





Now go to the Default Filter section and check according to your needs:

![](https://nextcloud.teamsyno.com/s/gJW72o7AaJz8dHd/preview)



All that remains is to save everything and go to the last tab, **Test Connection**, to check that everything is working properly.

Your Homepage now displays Ombi queries:

![](https://nextcloud.teamsyno.com/s/NBAwHcQjaGGWPKm/preview)


***
> ### To go even further with Oganizr, follow this tutorial [Varken-Grafana-Influxdb](Varken-Grafana-Influxdb)

***