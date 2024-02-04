# Installation des applications

Après avoir configuré votre type d'authentification, il est temps d'installer les applications clés qui seront au cœur de votre serveur.

## Démarrage du script d'installation

Lancez le script d'installation pour accéder au menu des applications :

```bash
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

### Sélection des applications à installer

1. **Accès au menu d'installation** : Répondez `1` pour accéder à l'ajout, la suppression, ou la sauvegarde d'applications.
2. **Installation d'applications** : Choisissez `1` pour installer une application.
3. **Choix des applications Seedbox** : Sélectionnez `1` pour les applications dédiées à la Seedbox.

### Sélection des applications

À partir du menu de sélection, choisissez les applications suivantes pour les installer sur votre serveur :

- Overseerr
- Plex
- Prowlarr
- Radarr (et Radarr4K si vous avez un setup en 4K)
- Sonarr (et Sonarr4K si vous avez un setup en 4K)

Confirmez votre sélection et suivez les instructions pour chaque application, notamment pour la configuration des sous-domaines et l'authentification.
Concernant la personnalisation des sous-domaines, répondez : n.
Pour l'authentification, cela dépend du choix que vous avez fait, si vous suivez le guide avec la Google Auth: 2.

### Configuration spécifique de Plex

Lors de l'installation de Plex, vous devrez fournir votre e-mail ou identifiant Plex, ainsi que votre mot de passe, pour lier automatiquement votre serveur Plex à votre compte.
En cas d'erreur dans les identifiants il sera nécessaire de supprimer puis réinstaller Plex.