# Sécurisation de l'accès au serveur

Sécuriser l'accès à votre serveur est une étape cruciale pour protéger vos données et vos applications. Vous avez le choix entre plusieurs méthodes d'authentification :

- Basique
- Google Auth
- Authelia
- Aucune

Il est recommandé de configurer l'authentification avant d'installer les applications nécessitant une protection. Dans ce guide, nous allons illustrer la procédure en utilisant Google Auth.

En intégrant Google Auth, vous simplifiez non seulement le processus de connexion pour les utilisateurs mais assurez également une couche de sécurité supplémentaire pour votre infrastructure.

## Configuration de Google Auth

1. **Préparation** : Commencez par consulter le [guide d'installation et de configuration pour Google Auth](https://projetssd.github.io/ssdv2_docs/Installation/oauth/). Ce guide vous fournira les étapes détaillées pour obtenir vos informations d'identification Google OAuth.
2. **Lancement du script** : Désormais vous pouvez utiliser un alias pour lancer le script, tapez simplement :
    
    ```bash
    seedbox
    ```
    
3. **Sélection dans le menu** : Choisissez l'option de gestion (2) suivie par la sécurisation du système (1), puis sécurisez Traefik avec Google OAuth2 (1).
4. **Configuration OAuth** : Remplissez les informations demandées : `Oauth_client`, `Oauth_secret`, et les comptes Gmail autorisés. (Vous pourrez en rajouter plus tard)
5. Refusez la personnalisation des sous-domaines et désormais choisissez Google Auth (2) lorsque le choix d'authentification vous est présenté.

Cette configuration permettra la mise à jour de Traefik pour utiliser Google Auth et l'installation de Watchtower pour la mise à jour automatique des containers Docker.

### Message de confirmation

Vous aurez ce message:

```bash
---------------------------------------------------------------
MISE A JOUR DU SERVEUR EFFECTUEE AVEC SUCCES
---------------------------------------------------------------

---------------------------------------------------------------
 IMPORTANT: Avant la 1ere connexion
 - Nettoyer l'historique de votre navigateur
 - déconnection de tout compte google
---------------------------------------------------------------
```

Après la mise à jour, il est conseillé de nettoyer l'historique de votre navigateur et de vous déconnecter de tous les comptes Google avant votre première connexion.

Vous pouvez appuyer sur ENTRÉE et nous pourrons continuer.

### Réinitialisation de RDTClient pour Google Auth

Il est nécessaire de le réinitialiser pour qu'il utilise correctement Google Auth :

```bash
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

Sélectionnez `1` pour l'ajout/suppression/sauvegarde, puis `3` pour réinitialiser une application. Utilisez les flèches pour sélectionner RDTClient et confirmez avec ENTRÉE.
Refusez la personnalisation du sous-domaine et comme vu plus haut, désormais choisissez Google Auth (2) lorsque le choix d'authentification vous est présenté.

### Fin de la configuration de Google Auth