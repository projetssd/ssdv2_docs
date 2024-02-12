#wordpress

#### Point your domain name to Wordpress


By default your installation will be installed in subdomain: https://wordpres.ndd.tld

You may want/need to have your site pointing directly to your domain: https://ndd.tld

Just edit the **wordpress.yml** file and modify the two lines like in the black frame:

`nano /opt/seedbox/conf/wordpress.yml`

![](https://nextcloud.teamsyno.com/s/eDd89bxJWjTkpFf/preview)

`traefik.frontend.rule: 'Host:{{domain.stdout}}'`

`traefik.frontend.headers.SSLHost: '{{domain.stdout}}'`

Once finished, reset the container and as a precaution, clear your explorer cache.

You now have access to your site directly through the URL of your domain and not in a subdomain.





#### Increase upload size in Wordpress (very) easily

Basically, limiting the upload size can pose a problem.

Here's how to fix it:

* Start by editing the .htaccess: `nano /opt/seedbox/docker/TON_USER/wordpress/.htaccess`
* Add these lines:

`php_value upload_max_filesize 128M`

`php_value post_max_size 128M`

`php_value max_execution_time 300`

`php_value max_input_time 300`

It will look like this when finished:

![](https://nextcloud.teamsyno.com/s/Q3Y9dXe55bktf7z/preview)

As a precaution, always clear your browser cache and reload the page on your domain, namely https://ndd.tld.