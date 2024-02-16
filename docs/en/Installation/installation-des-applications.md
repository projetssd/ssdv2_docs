# Installing apps

After configuring your authentication type, it's time to install the key applications that will be at the heart of your server.

## Starting the installation script

Normally you are still in the script, otherwise you can type:

```bash
seedbox
```

### Selecting applications to install

1. **Access to the installation menu**: Answer `1` to access the addition, removal, or backup of applications.
2. **Installing applications**: Choose `1` to install an application.
3. **Choice of Seedbox applications**: Select `1` for applications dedicated to the Seedbox.

### Application selection

From the selection menu, choose the following applications to install them on your server:

- Overseerr
- Plex
- Prowlarr
- Radarr (and Radarr4K if you have a 4K setup)
- Sonarr (and Sonarr4K if you have a 4K setup)

Confirm your selection and follow the instructions for each application, including setting up subdomains and authentication.
Regarding subdomain customization, answer: n.
For authentication, it depends on the choice you made, if you follow the guide with Google Auth: 2.

### Plex specific configuration

When installing Plex, you will need to provide your Plex email or ID, as well as your password, to automatically link your Plex server to your account.
In the event of an error in the identifiers, it will be necessary to delete and then reinstall Plex.