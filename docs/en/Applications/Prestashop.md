# Prestashop

To delete the install folder  
```
docker exec -ti prestashop bash
rm -rf install
mv admin toto
```  
  
To force SSL on all pages of the site  
```
docker exec -ti db-prestashop bash
mysql -u root -p
use prestashop
SELECT NAME, VALUE FROM ps_configuration WHERE NAME IN ('PS_SSL_ENABLED', 'PS_SSL_ENABLED_EVERYWHERE');
UPDATE ps_configuration SET VALUE = '1' WHERE NAME IN ('PS_SSL_ENABLED', 'PS_SSL_ENABLED_EVERYWHERE');
SELECT NAME, VALUE FROM ps_configuration WHERE NAME IN ('PS_SSL_ENABLED', 'PS_SSL_ENABLED_EVERYWHERE');
```