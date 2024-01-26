# UFW installation and configuration

UFW, or Uncomplicated Firewall, is an interface to iptables that is designed to simplify the process of setting up a firewall.

#### 1 - Installation :

To activate it you must go to the menu 3) Management, 2) Utilities, 8) Block non-vital ports with UFW.

By default, it will be installed with the following open ports:

	- http (80)
    - https (443)
    - plex  (32400)
    - ssh (22 if you left the default)

![mobaxterm-kfkusnrm4l](https://user-images.githubusercontent.com/64525827/105354525-f70c7700-5bf0-11eb-83ae-27aec32d5a72.png)


#### 2 - Important advice:

Once the installation is complete, do not close your terminal. Open a second one and try to connect via SSH.

#### 3 - Useful UFW commands:

attached is a non-exhaustive list of commands for UFW

To know the list of ports and the status on your server

	ufw status verbose
    


	Status: active 
	To                         Action      From
	-- ------ ----
	8398                       ALLOW       Anywhere
	Anywhere                   ALLOW       176.189.55.227
	Anywhere                   ALLOW       172.16.0.0/12
	Anywhere                   ALLOW       127.0.0.1
	80                         ALLOW       Anywhere
	443                        ALLOW       Anywhere
	8080                       ALLOW       Anywhere
	45000                      ALLOW       Anywhere
	plexmediaserver-all        ALLOW       Anywhere
	Anywhere                   ALLOW       182.122.87.111
	8398 (v6)                  ALLOW       Anywhere (v6)
	80 (v6)                    ALLOW       Anywhere (v6)
	443 (v6)                   ALLOW       Anywhere (v6)
	8080 (v6)                  ALLOW       Anywhere (v6)
	45000 (v6)                 ALLOW       Anywhere (v6)
	plexmediaserver-all (v6)   ALLOW       Anywhere (v6)
    
    
#### 4 - Adding ports and/or IP

If you need to add a particular port and/or IP address that will not be affected by UFW filtering, you must edit the following file: /opt/seedbox/conf/ufw.yml
and add additional lines. You should not modify existing lines.

	hosts: localhost
 	gather_facts: true
  	whose:
     opened_ports:
      - 80
      - 443
      - 8080
      - 45000
      # Add the necessary ports here:
      # - 25 # smtp
     allow_ips:
      - 172.17.0.1/12 # docker network, do not delete!
      - 127.0.0.1
      - 188.13.87.111
      # add additional ips or ranges here
      # - 123,456,789,123
      # - fe20:abcd::