# Rflood:

From the menu or with the `launch_service rflood` command  

## parameters to modify:  

<img width="828" alt="path" src="https://user-images.githubusercontent.com/64525827/149654327-93ebf2b6-de91-42a4-be70-5139719bd5b1.png">

## Important information:  

* Not compatible with radarr  
* No autotools to set a particular path at the end of the download  
* No ratio plugin, therefore no automatic management according to the ratio  


***

### You absolutely must modify the cloudplow config.json file in order to add the `rflood` folder in the exclusions  

* path => `home/${USER}/scripts/cloudplow/config.json`
take example from each already existing element (be careful it is written differently for each place)
***


