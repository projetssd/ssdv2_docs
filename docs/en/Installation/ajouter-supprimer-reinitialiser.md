# Differences between add, delete and reset

## 1) Add application

- Allows you to do a complete application installation
- Allows you to apply modifications made to the local .yml file (start by deleting the `docker rm -f appli` container)

## 2) Application removal

- Allows you to delete the local .yml as well as the data under `opt/seedbox/docker/${USER}` and the information
authentication and subdomains in the account file

## 3) Container reset

- Allows you to restore the original .yml file and apply changes
no deletion of user data or data contained in the account file

## 4) Container restart

- Allows you to stop/restart a container without deleting custom settings. Use if you have modified the original .yml of the application.
no deletion of user data or data contained in the account file

## Tips

It is possible to use quick commands provided you are in the Friday

``suppression_appli app``: delete the container, the information in account and the local yml  
``suppression_appli app 1``: delete the container, the information in account, the local yml as well as the data under opt  
``launch_service app``: installation of the application requested  