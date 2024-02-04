# Configuration initiale

## Connexion SSH

### Étape 1 : Téléchargement de PuTTY

1. Rendez-vous sur le site officiel de PuTTY : [Télécharger PuTTY](https://www.putty.org/).
2. Sur la page de téléchargement, vous verrez différentes versions de PuTTY. Téléchargez la version qui correspond à votre système d'exploitation.
3. Une fois le téléchargement terminé, exécutez le fichier d'installation que vous avez téléchargé.

### Étape 2 : Utilisation de PuTTY pour une connexion SSH

1. Dans la fenêtre PuTTY, vous verrez plusieurs options. Sous "Host Name (or IP address)", saisissez l'adresse IP ou le nom d'hôte du serveur distant auquel vous souhaitez vous connecter.
2. Assurez-vous que le port est correct. Par défaut, le port SSH est généralement 22, mais il peut varier en fonction de la configuration du serveur.
3. Vérifiez que le protocole de connexion est bien sur SSH.
4. Vous pouvez donner un nom à votre session dans le champ "Saved Sessions" en bas de la fenêtre. Cela vous permettra de sauvegarder la configuration pour une utilisation future.
5. Cliquez sur le bouton "Open" en bas de la fenêtre pour démarrer la connexion SSH.
6. PuTTY vous avertira que la clé SSH du serveur est inconnue. Cliquez sur "Yes" pour accepter la clé et continuer.
7. Vous serez invité à vous connecter en entrant votre nom d'utilisateur et votre mot de passe sur le serveur distant.
8. Une fois connecté, vous aurez accès à la ligne de commande du serveur distant via PuTTY. Vous pouvez maintenant exécuter des commandes et interagir avec le serveur.

C'est tout ! Vous êtes maintenant connecté en SSH à un serveur distant à l'aide de PuTTY. Vous pouvez utiliser cette connexion pour gérer et administrer le serveur à l’aide de commande selon vos besoins.

### Création d'un utilisateur Non-Root

Remplacez `nom_utilisateur` par le nom d'utilisateur de votre choix.

Créez un utilisateur standard :

```bash
adduser nom_utilisateur
```

Ajouter le au groupe sudo :

```bash
usermod -aG sudo nom_utilisateur
```

### Mise à Jour des paquets

Mettez à jour le système pour obtenir les dernières versions des logiciels :

```bash
sudo apt update && sudo apt upgrade -y
```

### Installation de Git

Git est un système de contrôle de version indispensable pour cloner le script SSDV2 depuis GitHub. Installez-le en utilisant la commande suivante :

```bash
sudo apt install -y git
```

## Passage d'utilisateur Root à Non-Root dans Putty

Pour la suite du guide, il est impératif de ne plus utiliser le compte root.

Choisissez la méthode qui convient le mieux à vos besoins. Pour une transition rapide sans fermer Putty, la méthode 2 est pratique. Pour une séparation plus nette des sessions, la méthode 1 est recommandée.

### Méthode 1: Fermeture et reconnexion

Cette méthode implique la fermeture de la session Putty actuelle et la reconnexion avec un utilisateur non-root.

1. **Terminer la session Putty actuelle** :
    - Fermez la fenêtre Putty pour terminer la session en cours.
2. **Reconnexion avec un utilisateur Non-Root** :
    - Ouvrez Putty à nouveau.
    - Lors de la connexion, utilisez les informations de connexion de votre utilisateur non-root au lieu du compte root.

### Méthode 2: Changement d'utilisateur sans fermer Putty

Pour changer d'utilisateur dans Putty sans fermer la session actuelle, la méthode mise à jour est la suivante :

1. **Utilisation de la commande `su -l`** :
    - Dans la session Putty ouverte, saisissez `su -l nom_utilisateur` pour initier une session en tant que votre utilisateur non-root. Remplacez `nom_utilisateur` par le nom réel de l'utilisateur non-root que vous souhaitez utiliser.
    - Lorsqu'il vous sera demandé, entrez le mot de passe de l'utilisateur non-root.

Cette commande vous connecte en tant que l'utilisateur spécifié avec un environnement de shell qui simule une connexion directe pour cet utilisateur, en réinitialisant les variables d'environnement et le répertoire courant à ceux de l'utilisateur ciblé. Cela assure une transition sécurisée et propre vers le nouvel utilisateur, évitant les problèmes liés à l'environnement et aux permissions qui peuvent survenir avec une utilisation basique de `su`.

### Clonage du script SSDV2

Après avoir installé Git, clonez le script SSDV2.

```bash
sudo git clone https://github.com/projetssd/ssdv2.git /home/${USER}/seedbox-compose
```

### Appropriation des droits sur le dossier du script

Il est important que votre utilisateur possède les droits sur le dossier du script pour permettre une exécution sans erreur. Exécutez la commande suivante :

```bash
sudo chown -R ${USER}: /home/${USER}/seedbox-compose
```

### Félicitation la configuration initiale est terminée !