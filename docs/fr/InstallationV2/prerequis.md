# Prérequis pour suivre le guide

## Nom de domaine

L'accès à vos applications nécessite un nom de domaine. Notre script facilite l'ajout et la personnalisation du sous-domaine pour chaque application.

- **Exemple :** `https://rutorrent.mondomaine.com`

Notez que certains fournisseurs de noms de domaine gratuits, comme Freenom, ne sont pas compatibles avec Cloudflare.

**Fournisseurs de nom de domaine recommandés :**

- Gandi
- LWS
- OVH
- Ionos
- InternetBS
- Et bien d'autres...

---

## Configurer Cloudflare

### Présentation

Cloudflare offre plus que des services de CDN. Son réseau mondial est conçu pour améliorer la sécurité, la performance et la fiabilité de tout ce qui est connecté à Internet, avec une configuration facile pour tous.

### Étapes de Configuration

#### 1. Création ou Connexion à un Compte Cloudflare

- Rendez-vous sur [le site de Cloudflare](https://dash.cloudflare.com/sign-up).
- Entrez votre adresse email et un mot de passe.
- Cliquez sur "Créer un compte".
- Ajoutez votre site en cliquant sur le bouton bleu "Ajouter un site".

**Ajoutez votre domaine** en entrant le domaine racine, puis cliquez sur "Ajouter un site". Cloudflare identifiera vos enregistrements DNS.

- Choisissez l'offre gratuite et confirmez.
- Suivez les instructions pour modifier vos serveurs DNS à ceux fournis par Cloudflare.

#### 2. Changer les Serveurs DNS pour Cloudflare

- Accédez à la console d'administration de votre fournisseur de domaine, par exemple OVH.
- Modifiez les serveurs DNS pour ceux fournis par Cloudflare.
- Appliquez la configuration et attendez la propagation des DNS (jusqu'à 24h).

#### 3. Récupération de l'API Global Cloudflare

- Dans votre compte Cloudflare, cliquez sur "Aperçu", puis sur "Obtenir votre jeton d'API".
- Cliquez sur "Afficher" à côté de "Global API Key".
- Conservez votre jeton pour l'installation du script.

#### 4. Configuration du Mode de Chiffrement SSL/TLS

- Réglez le mode SSL/TLS sur "Complet".