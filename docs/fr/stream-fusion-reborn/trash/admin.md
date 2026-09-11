# :material-monitor-dashboard: Administration TRaSH

Le panneau d'administration TRaSH (`/admin/quality/`) permet de gérer le système de scoring en temps réel : synchronisation, monitoring, création de templates, test des Custom Formats, et maintenance.

---

## Dashboard

Accès : `/admin/quality/dashboard.html`

Le dashboard présente une vue d'ensemble du système TRaSH en 4 cartes de statistiques :

| Stat | Description |
|---|---|
| **CFs Radarr** | Nombre de CFs disponibles pour les films (`source = radarr` ou `both`) |
| **CFs Sonarr** | Nombre de CFs disponibles pour les séries (`source = sonarr` ou `both`) |
| **CFs créés par admin** | CFs personnalisés créés manuellement (`source = user`) |
| **Templates actifs** | Nombre total de templates en base (système + utilisateur) |

### Cartes de statut

- **Scoring** : indique si `TRASH_SCORING_ENABLED` est actif et quel template est défini par défaut
- **Sync auto** : indique si `TRASH_SYNC_ENABLED` est actif et affiche le cron configuré
- **Dernier sync** : date de la dernière synchronisation réussie + version du miroir

!!! tip "Hot-reload"
    Le statut **Scoring** est modifiable à chaud depuis l'admin (`Paramètres → TRaSH → Scoring activé`). Aucun redémarrage n'est nécessaire.

---

## Synchronisation

Accès : `/admin/quality/sync.html`

### Lancer une sync manuelle

Cliquez sur **Lancer la sync** pour déclencher immédiatement une synchronisation avec le dépôt miroir. La sync s'exécute en arrière-plan via Taskiq.

**Phases d'exécution** :

1. `git_clone` — clone du miroir (`depth=1`)
2. `upsert_cf` — import des CFs radarr + sonarr, merge par `trash_id`
3. `cache_redis` — écriture des clés `cf:data:*`, `cf:slug_index`, `cf:metadata`
4. `upsert_templates` — import des templates système, résolution des slugs
5. `invalidate_caches` — suppression des anciens caches `tmpl:data:*`

### Monitoring temps réel

La page affiche un **flux de logs** en direct pendant la sync :

- :material-check: **Vert** = succès
- :material-alert: **Orange** = warning (slug non résolu, JSON invalide…)
- :material-close: **Rouge** = erreur

### Historique des syncs

Un tableau des 7 dernières exécutions affiche :

| Colonne | Description |
|---|---|
| Date | Horodatage de fin |
| Statut | `ok` / `error` / `skipped` |
| Durée | Temps d'exécution en ms |

### Gestion des verrous

| Action | Description |
|---|---|
| **Verrou actif** | Badge jaune indiquant qu'une sync est en cours (TTL 30 min) |
| **Libérer le verrou** | Force la suppression de la clé Redis `trash_sync:lock` si une tâche précédente est bloquée |

!!! danger "Libération manuelle"
    Ne libérez le verrou que si vous êtes certain qu'aucune sync n'est réellement en cours. Une double sync simultanée peut corrompre les données en base.

### Purge

| Bouton | Cible | Impact |
|---|---|---|
| **Purger la DB** | Supprime tous les CFs et templates **système** de PostgreSQL | Les CFs/utilisateurs et templates clonés sont préservés |
| **Purger Redis** | Supprime `cf:data:*`, `tmpl:data:*`, `cf:slug_index`, `cf:metadata` | Le scoring rechargera depuis PostgreSQL au prochain hit |

!!! warning "Purge irréversible"
    La purge DB nécessite une re-sync pour récupérer les CFs système. Assurez-vous que le miroir est accessible avant de purger.

---

## Templates

Accès : `/admin/quality/templates.html`

### Liste des templates

Chaque ligne affiche :

- **Nom + Slug**
- **Source** : `système` (importé du miroir) ou `utilisateur` (créé/cloné manuellement)
- **Défaut** : étoile jaune si c'est le template par défaut
- **Scores** : nombre de CFs configurés dans le template
- **Actions** : Éditer / Cloner / Exporter / Définir par défaut / Supprimer

### Actions disponibles

| Action | Système | Utilisateur | Description |
|---|---|---|---|
| **Éditer** | ✅ Vue seule | ✅ Édition JSON | Modifie le JSON du template |
| **Cloner** | ✅ | ✅ | Crée une copie `source = user` |
| **Exporter** | ✅ | ✅ | Télécharge le fichier `.json` |
| **Définir défaut** | ✅ | ✅ | Template pré-sélectionné pour les nouveaux users |
| **Supprimer** | ❌ | ✅ | Supprime définitivement |

### Créer un template

1. Cliquez **Nouveau template**
2. Remplissez `slug`, `name`, `description`
3. Éditez le JSON `config` (voir [Templates de scoring](templates.md#structure-json-complete))
4. Sauvegardez

---

## Custom Formats

Accès : `/admin/quality/formats.html`

### Liste des CFs

Les CFs sont présentés par catégorie avec :

- **Nom + trash_id**
- **Source** : `radarr` / `sonarr` / `both` / `user`
- **Specs** : nombre de règles de détection
- **Statut** : toggle actif/inactif

### Activer / Désactiver un CF

Cliquez sur le **toggle** à droite de chaque CF pour l'activer ou le désactiver. Les CFs désactivés ne participent plus au scoring.

!!! info "Désactivation persistante"
    La désactivation d'un CF système est conservée même après une re-sync. Seul le contenu JSON est écrasé par la sync, pas le statut actif/inactif.

### Créer un CF personnalisé

1. Cliquez **Nouveau CF**
2. Remplissez `name`, `category`
3. Ajoutez des [specifications](custom-formats.md#structure-json-dune-spec) au format JSON
4. Sauvegardez

Le CF est immédiatement utilisable dans vos templates personnalisés. Il est marqué `source = user` et ne sera jamais touché par la sync.

---

## Testeur de Custom Formats

Accès : `/admin/quality/tester.html`

Le testeur est l'outil le plus utile pour comprendre et déboguer le scoring. Il simule l'évaluation d'un titre de torrent contre les CFs de votre choix.

### Comment utiliser le testeur

1. **Collez un titre** dans le champ "Titre du torrent"
2. **Sélectionnez les CFs** à tester (barre de recherche + cases à cocher)
3. **Cliquez sur Évaluer**

### Résultats affichés

| Section | Contenu |
|---|---|
| **Métadonnées parsées** | Résolution, source, codec, audio, groupe, HDR, langues… extraits par RTN |
| **Score total** | Grande valeur affichée en haut à droite |
| **Détail par CF** | Liste des CFs testés avec ✅ (match) ou ❌ (no match) |
| **Breakdown** | Tableau des CFs matchés avec leur poids individuel |

!!! tip "Astuce de débogage"
    Si un CF ne matche pas alors que vous pensez qu'il devrait :
    
    1. Vérifiez les **métadonnées parsées** — RTN a-t-il bien extrait la résolution / la source ?
    2. Vérifiez que la spec utilise le bon `implementation` (ex: `ReleaseTitleSpecification` pour une regex sur le titre brut)
    3. Testez vos regex sur le titre brut avec un outil externe (regex101.com)

---

## Paramètres TRaSH

Accès : `/admin/settings.html` (section TRaSH)

| Paramètre | Type | Description |
|---|---|---|
| `TRASH_SCORING_ENABLED` | `bool` | Master switch du scoring (hot-reloadable) |
| `TRASH_SYNC_ENABLED` | `bool` | Active la sync planifiée |
| `TRASH_SYNC_CRON` | `str` | Expression cron de la sync |
| `TRASH_MIRROR_REPO_URL` | `str` | URL du dépôt miroir Git |
| `TRASH_MIRROR_BRANCH` | `str` | Branche à cloner |
| `TRASH_DEFAULT_TEMPLATE_SLUG` | `str` | Template par défaut si aucun n'est marqué en DB |

!!! note "Priorité des paramètres"
    Les valeurs modifiées dans l'admin écrasent les variables d'environnement. Si vous voulez revenir aux valeurs par défaut du `.env`, utilisez le bouton **Réinitialiser** dans l'admin.
