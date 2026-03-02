# 🛠️ Installation SSDv2 (Automatique)

> L’installation de SSDv2 est **automatique** lors du **premier lancement** de Seedbox.  
> Dans la majorité des cas, tu n’as **rien à faire** : lance Seedbox, laisse le bootstrap dérouler, puis utilise la WebUI.

---

## ✅ TL;DR

- 1️⃣ **Premier lancement Seedbox** → l’installation SSDv2 se fait **toute seule**
- 🔁 Pour relancer l’installation : `webui reinstall`
- 🧰 En cas de problème : relancer le bootstrap “manuel”
  - `cd $HOME/seedbox-compose/includes/config/ssd-bootstrap`
  - `make setup-all`
- 🆘 Si ça bloque : **copie/colle les logs** dans le Discord → section **"remonté de bug"**

---

## 1) Installation automatique (recommandée)

### Ce qui se passe
Lors de la **première exécution de Seedbox**, SSDv2 :
- initialise la configuration
- prépare les dépendances nécessaires
- déploie les composants et la WebUI
- applique les réglages par défaut

✅ Résultat attendu : après le premier lancement, tout est prêt.

---

## 2) Relancer l’installation via la WebUI / CLI

Si tu veux **forcer une réinstallation** (réparation, mise à jour, état incohérent) :

```bash
webui reinstall
```

> [!TIP]
> Utilise cette option en premier : c’est la méthode la plus simple pour remettre l’installation d’aplomb.

---

## 3) Dépannage — relancer l’installation “manuellement”

Si `webui reinstall` ne suffit pas ou si l’installation automatique a échoué, relance le bootstrap directement :

```bash
cd $HOME/seedbox-compose/includes/config/ssd-bootstrap
make setup-all
```

> [!WARNING]
> Cette méthode est à utiliser **en cas de souci** : elle relance le processus de setup complet via le bootstrap SSD.

---

## 4) En cas d’erreur : remonter le bug correctement

Si le problème persiste :

1. Relance l’installation via la méthode de dépannage (section 3)
2. Récupère les logs affichés (ou la sortie complète)
3. Colle-les dans le Discord, section :

✅ **"remonté de bug"**

> [!TIP]
> Plus tu donnes de contexte, plus le diagnostic est rapide :
> - ce que tu as lancé (auto / `webui reinstall` / `make setup-all`)
> - à quelle étape ça bloque
> - message d’erreur exact
> - ton environnement (OS, VPS/NAS, etc.)

---

## ✅ Résumé

- Installation **automatique** au premier lancement Seedbox ✅  
- Réinstallation simple : `webui reinstall` 🔁  
- En cas de problème : relance bootstrap avec `make setup-all` 🧰  
- Si ça coince : **logs → Discord / "remonté de bug"** 🆘