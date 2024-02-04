# Initial setting

## SSH connection

### Step 1: Downloading PuTTY

1. Go to the official PuTTY website: [Download PuTTY](https://www.putty.org/).
2. On the download page, you will see different versions of PuTTY. Download the version that matches your operating system.
3. Once the download is complete, run the installer file you downloaded.

### Step 2: Using PuTTY for an SSH connection

1. In the PuTTY window, you will see several options. Under "Host Name (or IP address)", enter the IP address or host name of the remote server you want to connect to.
2. Make sure the port is correct. By default, the SSH port is usually 22, but it may vary depending on the server configuration.
3. Verify that the connection protocol is SSH.
4. You can give your session a name in the "Saved Sessions" field at the bottom of the window. This will allow you to save the configuration for future use.
5. Click the "Open" button at the bottom of the window to start the SSH connection.
6. PuTTY will warn you that the server's SSH key is unknown. Click "Yes" to accept the key and continue.
7. You will be prompted to log in by entering your username and password on the remote server.
8. Once connected, you will have access to the remote server command line via PuTTY. You can now run commands and interact with the server.

That's all ! You are now connected by SSH to a remote server using PuTTY. You can use this connection to manage and administer the server using commands as needed.

### Creating a Non-Root User

Replace `username` with the username of your choice.

Create a standard user:

```bash
adduser username
```

Add it to the sudo group:

```bash
usermod -aG sudo username
```

### Package Update

Update the system to get the latest software versions:

```bash
sudo apt update && sudo apt upgrade -y
```

### Installing Git

Git is an essential version control system for cloning SSDV2 script from GitHub. Install it using the following command:

```bash
sudo apt install -y git
```

## Switching from Root to Non-Root user in Putty

For the remainder of the guide, it is imperative to no longer use the root account.

Choose the method that best suits your needs. For a quick transition without closing Putty, method 2 is convenient. For a cleaner separation of sessions, method 1 is recommended.

### Method 1: Closing and reconnecting

This method involves closing the current Putty session and reconnecting with a non-root user.

1. **End current Putty session**:
     - Close the Putty window to end the current session.
2. **Reconnect with a Non-Root user**:
     - Open Putty again.
     - When logging in, use your non-root user's login credentials instead of the root account.

### Method 2: Switch User Without Closing Putty

To change users in Putty without closing the current session, the updated method is:

1. **Using the `su -l`** command:
     - In the open Putty session, type `su -l username` to initiate a session as your non-root user. Replace `username` with the actual name of the non-root user you want to use.
     - When prompted, enter the password of the non-root user.

This command logs you in as the specified user with a shell environment that simulates a direct login for that user, resetting the environment variables and current directory to those of the targeted user. This ensures a secure and clean transition to the new user, avoiding environment and permissions issues that can arise with basic use of `su`.

### Cloning the SSDV2 script

After installing Git, clone the SSDV2 script.

```bash
sudo git clone https://github.com/projetssd/ssdv2.git /home/${USER}/seedbox-compose
```

### Appropriation of rights to the script folder

It is important that your user has rights to the script folder to allow error-free execution. Run the following command:

```bash
sudo chown -R ${USER}: /home/${USER}/seedbox-compose
```

### Congratulations, initial setup is complete!