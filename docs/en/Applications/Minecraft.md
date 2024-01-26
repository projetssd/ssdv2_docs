# Minecraft

![](https://nextcloud.teamsyno.com/s/2jzfHCLjTdB2WTF/preview)

#### Login and password for McMyAdmin

Login: `admin`

Password: `pass123`

**This must be changed immediately after your first connection for security reasons!**

Do not neglect this recommendation, this option is offered directly after the first connection, but do not skip this step.

#### Switch from Java 11 to Java 8

For many (good) Mods you will need Minecraft version 1.12.2, but this version **runs under Java 8**.

However, McMyAdmin is installed with Java 11 by default, which will result in your server never launching.

To remedy this, follow these steps:

`docker exec -ti minecraft bash`

`apt update`

`echo "deb http://ftp.us.debian.org/debian sid main" >> /etc/apt/sources.list`

`apt update`

`apt install openjdk-8-jdk`

`update-alternatives --config java`

Choose Java 8 version.

And finally, a little `exit`, we validate... it's over.

Good fun :)