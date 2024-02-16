# Lancement du script et configuration 

### Soyez attentif aux instructions !

Le script vous guidera à travers plusieurs étapes de configuration, y compris le choix de la langue, la configuration des dossiers, et la gestion des permissions.

Des messages d'alerte peuvent apparaître pour vous informer sur des spécificités de l'installation, comme les restrictions liées à la restauration des données et l'ajout de votre utilisateur au groupe docker. Il est important de lire attentivement ces messages et de procéder selon les instructions.

Par exemple, lorsque votre utilisateur sera ajouté au groupe Docker, vous serez invité à vous déconnecter / reconnecter pour que les changements soient effectués.

### Lancement du script

Pour démarrer l'installation, naviguez vers le répertoire du script et exécutez-le :

```bash
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

### Choix de la langue

Vous serez invité à choisir la langue pour l'interface :

```bash
1. Anglais/English
2. Français/French
```

### Message relatif à une éventuelle restauration d’installation

Vous aurez ce message :

```bash
Actuellement, la restauration ne fonctionne que si le script a été installé depuis le même répertoire que celui qui a servi à faire la sauvegarde, et a été installé sur la même destination.
```

Vous pouvez appuyer sur ENTRÉE pour passer à la suite.

### Configuration des répertoires

Le script demandera le répertoire de stockage pour les réglages des containers. Utilisez le chemin par défaut ou spécifiez un nouveau chemin.

```bash
/home/VOTRE_USER/seedbox
```

Pensez à remplacer VOTRE_USER par le vôtre créé au préalable.

### Ajout de votre utilisateur au groupe Docker

Vous aurez ce message :

```bash
IMPORTANT !
===================================================
Votre utilisateur n'était pas dans le groupe docker
Il a été ajouté, mais vous devez vous déconnecter/reconnecter pour que la suite du process puisse fonctionner
```

Le script a automatiquement ajouté le nouvel utilisateur que vous avez créé et sur lequel vous devez être actuellement connecté au groupe Docker.
Pour que la modification prenne effet il est impératif de se déconnecter / reconnecter, en cas d’oubli voici comment faire: 

- Fermez la fenêtre Putty pour terminer la session en cours.
- Ouvrez Putty à nouveau.
- Lors de la connexion, pensez à utiliser les informations de connexion de votre utilisateur non-root.

### Relancer le script

Relancer la commande permettant de lancer le script :

```bash
cd /home/${USER}/seedbox-compose && ./seedbox.sh
```

Vous aurez ce message :

```bash
Certains composants doivent encore être installés/réglés
Cette opération va prendre plusieurs minutes selon votre système
```

Vous pouvez appuyer sur ENTRÉE pour passer à la suite.

### Configuration de l'authentification basique

Pour chaque message suivez l'indication :

```bash
↘️ Mot de passe | Appuyer sur [Enter] :
```

Entrer un mot de passe, puis confirmer avec entrée

```bash
↘️ Mail | Appuyer sur [Enter] :
```

Entrer votre adresse mail, puis confirmer avec entrée

```bash
↘️ Domaine | Appuyer sur [Enter] :
```

Entrer votre nom de domaine (sans le https://, exemple: domaine.fr), puis confirmer avec entrée

### Gestion des DNS avec Cloudflare

Si vous souhaitez utiliser Cloudflare pour la gestion des DNS, le script vous demandera votre adresse mail Cloudflare ainsi que votre clé API.

Vous aurez ce message:

```bash
Souhaitez vous utiliser les DNS Cloudflare ? (y/n)
```

Nous vous recommandons de les utiliser afin que le script s’occupe de leur gestion automatiquement.

Répondez “y”.

### Installation des composants

Dans cette section, vous serez guidé à travers l'installation des divers composants nécessaires pour votre serveur.

Lorsque vous exécutez le script, il peut prendre un certain temps et rester en pause sur les tâches suivantes :

```
TASK [Add Debian repositories] ***************************************************************
TASK [Install common packages] ***************************************************************
```

Ne vous inquiétez pas, laissez-le s'exécuter, car la durée dépend de la puissance de votre serveur. Vous verrez le script redémarrer après un certain temps.

Ensuite, vous passerez par les étapes suivantes :

```bash
Adresse par défault: https://traefik.cinecast.tv

Souhaitez-vous personnaliser le sous-domaine ? (y/n)
```

Répondez "n". Vous pourrez les personnaliser plus tard, pour un suivi plus simple du guide il n’est pas recommandé de le faire pour l’instant.

---

```bash
Choix de l'authentification pour Traefik [ Entrée ] : 1 => basique | 2 => oauth | 3 => authelia
```

Pour le moment, choisissez "basique" en tapant "1". Vous pourrez installer Oauth Google ou Authelia plus tard.

---

```bash
Les composants sont maintenants tous installés/réglés, poursuite de l'installation

 1) Installation zurg - rclone - RDTclient
 2) Installation Minimale sans zurg
 3) Restauration Seedbox

Votre choix :
```

Tapez "1" et confirmez pour sélectionner "1) Installation zurg - rclone - RDTclient".

---

```bash
Token API pour Zurg (https://real-debrid.com/apitoken) | Appuyez sur [Entrée]:
```

Fournissez votre clé API, disponible sur http://real-debrid.com/apitoken.

---

```bash
Personnaliser le sous-domaine pour rdtclient : (y/n) ?
```

Répondez "n".

---

```bash
Authentification rdtclient [ Entrée ] : 1 => basique (par défaut) | 2 => oauth | 3 => authelia | 4 => aucune
```

Répondez "1", pour l’instant comme vu plus haut.

---

```bash
Noms de dossiers à créer dans Medias (ex : Films, Series, Films d'animation, etc.) | Appuyez sur [Entrée] | Tapez "stop" une fois terminé.
```

La configuration classique : Films, Series, stop.
Pour un setup avec 4K : Films, Series, Films4K, Series4K, stop.
Vous devez entrer le nom, puis appuyer sur Entrée, et ainsi de suite, jusqu'à "stop". Pour ce guide, nous suivrons l'exemple avec 4K.

![creation_dossier_media.png](https://i.imgur.com/CNsarEa.png)

---

Après avoir terminé ces étapes, vous verrez le message suivant :

```
Pour bénéficier des changements, vous devez vous déconnecter/reconnecter.
L'installation est maintenant terminée.
Pour le configurer ou modifier les applications, vous pouvez le relancer :
cd /home/ubuntu/seedbox-compose
./seedbox.sh
```

Déconnectez-vous et reconnectez-vous pour appliquer les changements.

- Fermez la fenêtre Putty pour terminer la session en cours.
- Ouvrez Putty à nouveau.
- Lors de la connexion, pensez à utiliser les informations de connexion de votre utilisateur non-root.

### Vous avez réussi à accéder à l'accueil du script. Bravo. **[👍](https://emojipedia.org/thumbs-up)**