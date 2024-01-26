# Comment configurer FlareSolverr 

[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr){:target="_blank" rel="noopener noreferrer"} est un serveur proxy pour contourner la protection Cloudflare et DDoS-GUARD. 

!!! info 

    - Un proxy FlareSolverr ne sera utilisé pour les requêtes que si et seulement si Cloudflare est détecté par Prowlarr 
    - Un proxy FlareSolverr ne sera utilisé pour les requêtes que si et seulement si le proxy et l'indexeur ont des balises correspondantes 
    - Un proxy Flaresolverr configuré sans aucune balise ou n'a pas d'indexeurs avec des balises correspondantes, il sera désactivé. 

## Installer FlareSolverr 

Veuillez suivre les instructions d'installation de [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr#installation){:target="_blank" rel="noopener noreferrer"} 

## Ajouter FlareSolverr aux 

`Paramètres de Prowlarr ` => `indexers` 

![Paramètres => images](images/settings-indexers.png) 

Cliquez sur le signe + et sélectionnez `FlareSolverr` 

![Ajouter des indexeurs](images/add-indexer-proxy-flaresolverr.png) 

Ajoutez les informations suivantes 

![Ajouter Proxy FlareSolverr](images/add-proxy-flaresolverr.png) 

1. Nom du proxy dans Prowlarr. 
1. Les balises de ce proxy. 
1. Le chemin complet de l'hôte (inclut http et le port) vers votre instance FlareSolverr. 
1. La [valeur maxTimeout de la requête FlareSolver](https://github.com/FlareSolverr/FlareSolverr#-requestget){:target="_blank" rel="noopener noreferrer"} Prowlarr doit utiliser pour les requêtes FlareSolverr. Doit être compris entre « 1 » seconde et « 180 » secondes (par défaut : « 60 » secondes). 
1. Testez si votre connexion fonctionne. 
1. Si cela fonctionne, cliquez sur « Enregistrer ». 

## Ajoutez FlareSolverr à votre indexeur 

Sélectionnez l'indexeur que vous souhaitez utiliser avec FlareSolverr 

![Sélectionnez l'indexeur](images/select-indexer.png) 

Faites défiler vers le bas et ajoutez la balise que vous avez configurée plus tôt à l'étape 2. 

![Ajouter une balise à l'indexeur](images/add-tag-to-indexer-flaresolverr.png) 

Cliquez sur `Test` et `Enregistrer`. 

L'indexeur devrait maintenant utiliser FlareSolverr. 

--8<-- "includes/support.md"