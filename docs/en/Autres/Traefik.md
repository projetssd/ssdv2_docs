# Traefik

#### Add a 2nd Domain to traefik  
Considering you are using cloudflare, which in my opinion is the best choice. Firstly, we delete the traefik container  

```
docker rm -f traefik
rm -rf /opt/seedbox/docker/traefik
```  
Back up the rules folder if you have created specific rules  
Configure cloudflare for the new domain concerned (the 2 domains must belong to the same cloudflare account)  
Then modify the following file:  

```/opt/seedbox-compose/includes/dockerapps/traefik.yml```

```
    - name: label traefik with cloudflare
      set_fact:
        labels:
          traefik.enable: 'true'
          ## HTTP-to-HTTPS Redirect
          traefik.http.routers.http-catchall.entrypoints: 'http'
          traefik.http.routers.http-catchall.rule: 'HostRegexp(`{host:.+}`)'
          traefik.http.routers.http-catchall.middlewares: 'redirect-to-https'
          traefik.http.middlewares.redirect-to-https.redirectscheme.scheme: 'https'
          ## HTTP Routers
          traefik.http.routers.traefik-rtr.entrypoints: 'https'
          traefik.http.routers.traefik-rtr.rule: 'Host(`traefik.{{user.domain}}`)'
          traefik.http.routers.traefik-rtr.tls: 'true'
          traefik.http.routers.traefik-rtr.tls.certresolver: 'letsencrypt'
          traefik.http.routers.traefik-rtr.tls.domains[0].main: '{{user.domain}}'
          traefik.http.routers.traefik-rtr.tls.domains[0].without: '*.{{user.domain}}'
          traefik.http.routers.traefik-rtr.tls.domains[1].main: 'second-domain.com'
          traefik.http.routers.traefik-rtr.tls.domains[1].without: '*.second-domain.com'
          ....
```
Reinstall Traefik  
```
ansible-playbook /opt/seedbox-compose/includes/dockerapps/traefik.yml
```
Verification:  
```cat /opt/seedbox/docker/traefik/acme/acme.json```  
```
{
  "letsencrypt": {
    “Account”: {
      "Email": "xxxxxxx@gmail.com",
      "Registration": {
        "body": {
          "status": "valid",
          "contact": [
            "mailto:xxxxxx@gmail.com"
          ]
        },
        "uri": "https://acme-staging-v02.api.letsencrypt.org/acme/acct/16387697"
      },
      "PrivateKey": "MIIJKAI............Nz9NTZXRDc=",
      “KeyType”: “4096”
    },
    "Certificates": [
      {
        "domain": {
          "main": "PremierDomaine.com",
          "without": [
            "*.PremierDomaine.com"
          ]
        },
        "certificate": "t.............LS0K",
        "Store": "default"
      },
      {
        "domain": {
          "main": "SecondDomaine.fr",
          "without": [
            "*.SecondDomaine.fr"
          ]
        },
        "certificate": "S0.............K",
        "key": "0K.........",
        "Store": "default"
      }
    ]
  }
}
```
Modify the traefik labels of apps this way (/opt/seedbox/conf)    

```
        pg_labels:
          traefik.enable: 'true'
          ## HTTP Routers
          traefik.http.routers.lidarr-rtr.entrypoints: 'https'
          traefik.http.routers.lidarr-rtr.rule: 'Host(`lidarr.{{user.domain}}`) || Host(`lidarr.secondDomaine.com`)'
          traefik.http.routers.lidarr-rtr.tls: 'true'
          ## Middleware
          ##traefik.http.routers.lidarr-rtr.middlewares: "{{ 'chain-oauth@file' if oauth_enabled | default(false) else 'chain-basic-auth@file' }}"
          ## HTTP Services
          traefik.http.routers.lidarr-rtr.service: 'lidarr-svc'
          traefik.http.services.lidarr-svc.loadbalancer.server.port: '8686'
```
Finally reset via script