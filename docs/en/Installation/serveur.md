# Choosing a server

## Get a remote server

* You will need a dedicated server, available for example from Hetzner, Kimsufi, OVH, Oneprovider, etc...

### The script is currently compatible with
*Ubuntu Server 18.014 and 20.04
* Debian 9 - 10 - 11

We advise you not to use a VPS server, you will not have sufficient performance to take full advantage of the script.

Your server must be blank, do not install any elements, the script will do it.

### Partitioning

If you have several hard drives on the server, we advise you to switch to RAID to use all the available space.
* The server must not have a separate "/home" when partitioning.
* The partition hosting the data must be at the root "/".
* A partition for the boot, with a recommended minimum size of 512MB.

### User

For the moment the installation must be done from a user who has sudo rights. No direct root connection! Likewise, you should not log in as root then do "su - <user>" but establish a connection directly with the correct user.