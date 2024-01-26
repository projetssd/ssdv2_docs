# Manual manipulations

For any operation, make sure you are not root.

Load environment:
```
cd /opt/seedbox-compose
source profile.sh
```

After that, you should see (venv) in front of the command prompt.


# Show all the contents of account.yml in the shell
```
get_from_account_yml
```

# Handle the account.yml

The keys are separated by periods. For example
```
user
  domain: mydomain.net
```

The key will be user.domain, and its value will be mydomain.net

## Write a key
This will create the key if it doesn't exist, or overwrite it if it does.

```
manage_account_yml key value
```
For example
```
manage_account_yml user.domain mydomain.com
```

## Delete a key
This will erase the key as well as all associated subkeys.

```
manage_account_yml key " "
```
For example
```
manage_account_yml user.domain " "
```

## Get the value of a key

```
get_from_account_yml key
```
For example
```
get_from_account_yml user.domain
```
will return
```
mydomain.com
```
If the value is not found, it returns "notfound"

You can also return a key and all its subkeys:
```
get_from_account_yml user
```
will return
```
domain: mydomain.com group: null groupid: 1001 htpwd: seed:xxxxxxxxxxxxxx mail: me@mydomain.com name: seed pass: xxxxxxxxxxxxxx userid: 1001
```

# Install/Launch an application without going through the menu

```
launch_service servicename
```
# Uninstall an application without going through the menu
```
delete_app service name
```
# Exit the manipulation environment

Run the command
```
deactivate
```