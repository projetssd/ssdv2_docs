#Authelia

First of all, Authelia is an open-source tool that acts as a portal where the user is asked to authenticate.

Once connected, Authelia allows you to manage whether or not a user can access given resources with a fairly fine granularity on the URL. For example, you can allow the user to connect to a domain name, while preventing them from accessing a specific folder (/admin).

This tool manages up to two authentication factors and allows the use of single sign-on (SSO) across all applications configured through it.

Finally, Authelia easily integrates with reverse proxy tools such as Traefik, NGINX or even HAProxy as you can see in the architecture below:

![authelia-architecture](https://user-images.githubusercontent.com/64525827/105358641-b9125180-5bf6-11eb-929c-4eb7131d5a84.png)


Important: Create an application password by following this procedure  

[Create and use app passwords](https://support.google.com/mail/answer/185833?hl=en)

Finally example of connection parameter with gmail

smtp: smtp.gmail.com
port 587
application password: the one created previously by following the link