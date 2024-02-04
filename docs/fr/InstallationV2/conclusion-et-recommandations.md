# Conclusion et recommandations

Il semble que la configuration des applications soit terminée ! Il reste des pistes à explorer, tels que l'envoi de notifications pour différents événements, la personnalisation des formats dans Radarr et Sonarr, l'utilisation de listes pour ajouter automatiquement du contenu, etc. Il peut-être intéressant d'explorer ces options en fonction de vos besoins spécifiques.

En ce qui concerne les recommandations pour la suite, voici ce que vous pouvez envisager :

### Amélioration de la sécurité SSH

Pour améliorer la sécurité, envisagez de configurer SSH pour désactiver la connexion root et changer le port par défaut :

```bash
sudo nano /etc/ssh/sshd_config
```

- Changez `PermitRootLogin yes` en `PermitRootLogin no`.
- Modifiez le port par défaut en choisissant un numéro de port non standard.

N'oubliez pas de redémarrer le service SSH après vos modifications :

```bash
sudo systemctl restart sshd
```

## Sécurisation supplémentaires

1. **Protocole d'identification** : Si ce n'est pas déjà fait, envisagez de mettre en place un protocole d'identification sécurisé, tel que Google OAuth2 ou Authelia, pour renforcer la sécurité de votre système.
2. **Optimisation de Cloudflare** : Vous pouvez optimiser votre utilisation de Cloudflare en suivant le guide disponible à cette adresse : [Guide d'optimisation Cloudflare](https://projetssd.github.io/ssdv2_docs/Installation/optimisation-cloudflare/). Cela peut contribuer à améliorer les performances et la sécurité de votre système.
3. **Installation et configuration de UFW** : Vous pouvez installer et configurer Uncomplicated Firewall (UFW) en suivant le guide disponible ici : [Guide d'installation et de configuration de UFW](https://projetssd.github.io/ssdv2_docs/Installation/ufw-Installation-configuration/). Cela vous aidera à gérer les règles de pare-feu pour renforcer la sécurité.

## **Outils et guides recommandés**

**TRaSH-Guides** :

- Ces guides sont des ressources précieuses pour configurer et optimiser Sonarr, Radarr, et autres applications de gestion de médias. Ils offrent des conseils sur la configuration des qualités, des profils, et des indexeurs pour obtenir les meilleurs résultats possibles.

**Notifiarr** :

- Cet outil permet de synchroniser les configurations entre vos applications de gestion de médias et les guides TRaSH, en s'assurant que vos paramètres sont toujours optimisés selon les meilleures pratiques. Notifiarr peut également envoyer des notifications personnalisées pour divers événements sur votre serveur.

**Tautulli** :

- Application de suivi et de surveillance pour Plex Media Server. Elle vous permet de surveiller l'activité de votre serveur Plex, de générer des statistiques détaillées sur l'utilisation de vos médias, de recevoir des notifications sur les nouveaux ajouts et les activités des utilisateurs, et bien plus encore. C'est un outil essentiel pour les administrateurs de serveurs Plex.

**LunaSea** :

- Application mobile conviviale conçue pour gérer des applications telles que Radarr, Sonarr, Lidarr, et d'autres, directement depuis votre appareil. Elle offre une interface propre pour gérer et surveiller vos collections de films, de séries et de musique, ainsi que pour effectuer des recherches et des ajouts.

**nzb360** :

- nzb360 est une application mobile qui vous permet de gérer et de contrôler de manière intuitive vos applications de gestion de médias telles que Sonarr, Radarr, Sabnzbd, NZBGet, et plus, directement depuis votre smartphone. C'est un outil puissant pour garder un œil sur votre serveur Plex et les services associés, même lorsque vous êtes en déplacement.

## Applications complémentaires selon les besoins

**Organizr** :

- Portail web personnalisable qui agit comme une interface unifiée pour accéder à vos applications, services et sites web préférés. Vous pouvez regrouper et organiser tous vos liens et applications en un seul endroit, ce qui facilite la navigation et la gestion de vos ressources en ligne.

**Lidarr** :

- Si vous gérez également une collection de musique, Lidarr est à la musique ce que Sonarr est aux séries télé et Radarr aux films. Il peut automatiser le téléchargement de vos pistes musicales préférées.

**Bazarr** :

- Pour la gestion des sous-titres, Bazarr est une excellente addition. Il fonctionne bien avec Sonarr et Radarr pour télécharger automatiquement les sous-titres pour vos films et séries.

**Readdarr** :

- C'est un gestionnaire de livres et de bandes dessinées qui automatise le téléchargement de contenus basés sur des critères que vous définissez. Comme Sonarr et Radarr pour les séries et les films, Readdarr peut gérer vos besoins en matière de littérature et de comics, en gardant votre bibliothèque à jour avec les dernières sorties.

**Whisparr** :

- Se concentre sur la gestion de collections de films pour adultes, intégrant des fonctionnalités similaires de suivi et d'organisation automatique.

**Jackett** :

- Jackett sert de proxy entre vos applications de téléchargement de torrents et plus de 100 trackers de torrents, ce qui vous permet de chercher dans un large éventail de trackers directement depuis Sonarr, Radarr, etc. Bien que Prowlarr offre des fonctionnalités similaires, Jackett reste une alternative solide ou un complément, surtout si vous avez besoin de prendre en charge des trackers spécifiques non pris en charge par Prowlarr.

**Jellyfin** :

- Bien que vous utilisiez déjà Plex, Jellyfin peut servir d'alternative open-source ou complémentaire pour la diffusion de médias. C'est une solution de serveur média qui permet de gérer et de diffuser votre collection de médias numériques sans les restrictions liées aux licences.

**Mylar** :

- Pour les amateurs de bandes dessinées, Mylar automatise le téléchargement des comics, similaire à ce que Sonarr fait pour les séries télévisées.

**Calibre-Web** :

- Si vous gérez également une collection d'e-books, Calibre-Web peut être une excellente addition. Il permet de gérer et de lire vos livres électroniques dans un navigateur web.

**Requestrr** :

- C’est un outil de chatbot qui permet à vos amis et à votre famille de demander des films et des séries TV via Discord ou Telegram directement à votre serveur Sonarr ou Radarr. C'est un excellent moyen de simplifier le processus de demande sans avoir besoin d'accorder un accès direct à vos outils de gestion de médias. Requestrr peut automatiser le processus de demande et d'ajout de contenu à votre serveur Plex, rendant l'expérience plus interactive et conviviale pour les utilisateurs.

## Gestion et surveillance du serveur

**Uptime-Kuma** :

- Outil de surveillance de serveur qui vous permet de surveiller la disponibilité de vos services et sites web en temps réel. Il génère des rapports sur la disponibilité, la latence et les erreurs, vous permettant ainsi de détecter rapidement les problèmes et d'assurer une disponibilité maximale de vos services en ligne.

**Portainer** :

- Interface de gestion de conteneurs Docker qui simplifie la gestion et le déploiement de conteneurs Docker sur votre système. Il offre une interface utilisateur intuitive pour gérer vos conteneurs, surveiller leurs performances, effectuer des mises à jour et bien plus encore. C'est un outil puissant pour les utilisateurs de Docker.

**Grafana** ou **Prometheus** :

- Pour les utilisateurs avancés intéressés par la surveillance et la visualisation des performances de leur serveur. Ces outils peuvent vous aider à surveiller l'utilisation des ressources, les performances du réseau, et plus encore, avec des tableaux de bord personnalisables.

**Glances** :

- Un outil de surveillance de système cross-platform qui peut vous donner un aperçu rapide de l'utilisation des ressources sur votre serveur. Il est moins complexe que Grafana et Prometheus pour une configuration simple et rapide.

## Exploration de nouvelles fonctionnalités

**Nextcloud** :

- Une solution de stockage en cloud personnel qui peut être utilisée pour sauvegarder des configurations, des fichiers médias ou même pour partager des fichiers avec des amis et de la famille de manière sécurisée. Nextcloud peut compléter votre serveur Plex en offrant un stockage et un partage de fichiers flexibles.

**Home Assistant** :

- Pour ceux qui s'intéressent à l'automatisation de la maison, intégrer Home Assistant à votre réseau peut vous permettre de créer des automatisations intéressantes autour de votre expérience de visionnage Plex, comme ajuster l'éclairage ou le thermostat lorsque vous commencez à regarder un film.

Et bien d'autres que vous pourrez retrouver ici: https://github.com/Ravencentric/awesome-arr

## Félicitations pour avoir parcouru ce guide complet sur la mise en place de votre serveur avec SSDV2 ! **[🎉](https://emojipedia.org/fr/cotillons)**

Nous espérons que les instructions détaillées, les conseils pratiques, et les recommandations fournies vous ont équipé des connaissances nécessaires pour construire un serveur performant et sécurisé. Vous disposez maintenant d'un environnement robuste pour vos besoins en streaming et en gestion de fichiers multimédias. N'oubliez pas que le voyage ne s'arrête pas ici, continuez d'explorer, d'apprendre et d'adapter votre serveur pour qu'il réponde toujours mieux à vos besoins. Encore une fois, **bravo** et bonne continuation dans vos aventures numériques !