# Securing access to the server

Securing access to your server is a crucial step in protecting your data and applications. You have the choice between several authentication methods:

- Basic
-GoogleAuth
-Authelia
- None

It is recommended to configure authentication before installing applications that require protection. In this guide, we will demonstrate the procedure using Google Auth.

By integrating Google Auth, you not only simplify the login process for users but also provide an additional layer of security for your infrastructure.

## Setting up Google Auth

1. **Preparation**: Start by consulting the [installation and configuration guide for Google Auth](https://projetssd.github.io/ssdv2_docs/Installation/oauth/). This guide will provide you with detailed steps to obtain your Google OAuth credentials.
2. **Launching the script**: Now you can use an alias to launch the script, simply type:
    
    ```bash
    seedbox
    ```
    
3. **Selection from the menu**: Choose the management option (2) followed by securing the system (1), then secure Traefik with Google OAuth2 (1).
4. **OAuth configuration**: Fill in the requested information: `Oauth_client`, `Oauth_secret`, and authorized Gmail accounts. (You can add more later)
5. Refuse subdomain customization and now choose Google Auth (2) when the authentication choice is presented to you.

This configuration will allow the update of Traefik to use Google Auth and the installation of Watchtower for automatic updating of Docker containers.

### Confirmation message

You will get this message:

```bash
-------------------------------------------------- -------------
SERVER UPDATE SUCCESSFULLY COMPLETED
-------------------------------------------------- -------------

-------------------------------------------------- -------------
  IMPORTANT: Before the first connection
  - Clean your browser history
  - disconnection from any google account
-------------------------------------------------- -------------
```

After updating, it is advisable to clean your browser history and log out of all Google accounts before your first login.

You can press ENTER and we can continue.

### Resetting RTTClient for Google Auth

It is necessary to reset it for it to use Google Auth correctly:

```bash
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

Select `1` for add/remove/backup, then `3` to reset an application. Use the arrows to select RDTClient and confirm with ENTER.
Refuse the customization of the subdomain and as seen above, now choose Google Auth (2) when the authentication choice is presented to you.

### Google Auth setup Complete !