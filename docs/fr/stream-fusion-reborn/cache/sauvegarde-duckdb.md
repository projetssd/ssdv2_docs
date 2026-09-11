# Sauvegarde DuckDB

DuckDB est la base de données analytique qui alimente le **matching IMDB** de Stream Fusion. Sa sauvegarde est critique : une corruption signifie une reconstruction complète de ~8 heures.

---

## Pourquoi sauvegarder DuckDB ?

<div class="grid cards" markdown>

-   :material-clock-fast: **Temps de reconstruction**

    La construction initiale de la base DuckDB prend **6 à 8 heures** : téléchargement des datasets IMDB (~1.5 GB compressés), parsing TSV, normalisation des titres, insertion dans DuckDB.
    
    Une sauvegarde se restaure en **quelques secondes**.

-   :material-alert-circle: **Données critiques**

    Sans DuckDB, le matching IMDB est inopérant. Les torrents ne reçoivent plus d'ID IMDB/TMDB, ce qui dégrade fortement la qualité des résultats de recherche.

-   :material-file-alert: **Corruption possible**

    Un arrêt brutal du conteneur, un espace disque plein, ou une corruption du système de fichiers peut endommager le fichier `imdb.duckdb`.

</div>

---

## Méthode correcte : CHECKPOINT + copie fichier

La méthode de dump fiable et bit-perfect pour DuckDB est :

```
1. CHECKPOINT       → vide le WAL sur disque
2. Copie fichier    → copie imdb.duckdb
3. Archive tar.gz   → compression + SHA-256
```

```bash
# Équivalent manuel de ce que fait la tâche db_dump_create
# 1. Connexion DuckDB et CHECKPOINT
python3 -c "
import duckdb
con = duckdb.connect('/data/imdb_db/imdb.duckdb')
con.execute('CHECKPOINT')
con.close()
"

# 2. Archivage
tar czf /data/backups/duckdb/$(date +%Y-%m-%d_%H-%M).tar.gz \
  -C /data/imdb_db imdb.duckdb

# 3. Vérification
sha256sum /data/backups/duckdb/$(date +%Y-%m-%d_%H-%M).tar.gz
```

!!! success "Pourquoi ça marche"
    - DuckDB est conçu pour la **portabilité** : le fichier `.duckdb` est auto-contenu et compatible entre plateformes (Linux ARM64/AMD64, macOS)
    - Le `CHECKPOINT` garantit que le WAL est vidé : le fichier est dans un état cohérent
    - La copie est **bit-perfect** : aucune transformation, aucune perte

---

## Méthode incorrecte : EXPORT / IMPORT DATABASE

!!! danger "Ne JAMAIS utiliser EXPORT DATABASE / IMPORT DATABASE"

DuckDB propose deux commandes qui semblent pratiques pour la sauvegarde :

```sql
-- DANGEREUX : ne pas utiliser
EXPORT DATABASE '/tmp/duckdb_export';
IMPORT DATABASE '/tmp/duckdb_export';
```

Ce round-trip CSV est **cassé** sur les données IMDB réelles pour plusieurs raisons :

### 1. Apostrophes et guillemets dans les titres

Les titres IMDB contiennent fréquemment des caractères problématiques pour le CSV :

| Titre | Caractère problématique |
|---|---|
| `L'Affaire Farewell` | Apostrophe |
| `L'Immortel` | Apostrophe |
| `Today's Special` | Apostrophe |
| `"Les Misérables"` | Guillemets |

Le parsing CSV de DuckDB utilise des règles d'échappement strictes. Un titre contenant une apostrophe non échappée selon les conventions CSV sera tronqué ou corrompu.

### 2. Origine des données

Les données IMDB entrent dans DuckDB via `executemany()` Python, pas via parsing CSV :

```python
# Les données sont insérées par executemany() — pas de CSV
con.executemany(
    "INSERT INTO imdb_akas VALUES (?, ?, ?, ?, ?, ?, ?)",
    rows  # Liste de tuples Python
)
```

Le chemin de données est : `TSV original` -> `parsing Python` -> `executemany()` -> `DuckDB`.  
Le parsing TSV de Python et le parsing CSV de DuckDB ont des règles d'échappement **différentes**.

### 3. Résultat

Le round-trip CSV peut causer :
- **Perte silencieuse de lignes** contenant des caractères spéciaux
- **Corruption de titres** (apostrophes transformées, guillemets mal échappés)
- **Base inutilisable** pour le matching (titres normalisés incorrects)

!!! tip "La copie de fichier est aussi plus rapide"
    `EXPORT DATABASE` écrit chaque table en CSV puis `IMPORT DATABASE` les relit. Pour une base de ~8-10 GB, cela prend beaucoup plus de temps qu'une simple copie binaire du fichier.

---

## Dumps automatisés

La tâche Taskiq `db_dump_create` (type `duckdb`) automatise le processus :

- **CHECKPOINT** : vidage du WAL
- **Copie fichier** : `imdb.duckdb` -> `tar.gz`
- **SHA-256** : vérification d'intégrité
- **Manifest** : enregistrement dans `manifest.json`
- **Rétention** : nettoyage des anciens dumps

### Configuration

```env
DB_DUMP_SCHEDULE_ENABLED=True   # Active les dumps automatiques
DB_DUMP_CRON=0 4 * * 0          # Dimanche 4h (défaut)
DB_DUMP_RETENTION=3             # Garder 3 dumps (défaut)
```

!!! note "Planification par défaut"
    Par défaut, les dumps DuckDB sont planifiés le **dimanche à 4h du matin**, en même temps que les dumps Meilisearch. La rétention par défaut est de 3 dumps.

### Déclenchement manuel

Depuis le panneau d'administration (`/admin/maintenance/`), vous pouvez déclencher un dump DuckDB à tout moment via le bouton **Créer un dump**.

---

## Restauration manuelle

### Depuis un dump local

```bash
# 1. Arrêter l'application
docker compose stop app

# 2. Extraire l'archive
tar xzf /data/backups/duckdb/2025-01-01_04-00.tar.gz -C /tmp/

# 3. Remplacer le fichier
cp /tmp/imdb.duckdb /data/imdb_db/imdb.duckdb

# 4. Redémarrer
docker compose start app
```

### Depuis un pair (pull distant)

Utilisez le panneau d'administration :

1. Allez dans `/admin/maintenance/`
2. Sélectionnez un pair dans la liste déroulante (avec aperçu des stats : nombre de lignes, taille)
3. Choisissez un dump
4. Cliquez sur **Pull**
5. La progression s'affiche en temps réel
6. La vérification SHA-256 est automatique

Ou déclenchez manuellement :

```bash
# via l'API admin
curl -X POST http://localhost:8080/admin/meta/peer-pull/start \
  -H "Content-Type: application/json" \
  -H "X-API-Key: votre-secret-api-key" \
  -d '{"db_type": "duckdb", "peer_id": "id-du-peer", "dump_id": "2025-01-01_04-00"}'
```

!!! warning "Les dumps DuckDB sont priorisés"
    Parmi les trois types de dumps, DuckDB est le plus critique. Une base DuckDB corrompue signifie que le matching IMDB est inopérant jusqu'à reconstruction complète (~8h). Activez toujours les dumps automatiques DuckDB en production.

---

## Dépannage

### Vérifier l'intégrité d'un dump

```bash
# Vérifier le SHA-256
sha256sum /data/backups/duckdb/2025-01-01_04-00.tar.gz

# Comparer avec le manifest.json
cat /data/backups/duckdb/manifest.json | jq '.dumps[] | select(.id=="2025-01-01_04-00") | .sha256'
```

### Vérifier la validité d'une base DuckDB

```bash
python3 -c "
import duckdb
con = duckdb.connect('/data/imdb_db/imdb.duckdb', read_only=True)
tables = con.execute(\"SELECT name FROM sqlite_master WHERE type='table'\").fetchall()
print('Tables:', [t[0] for t in tables])
for t in tables:
    count = con.execute(f'SELECT COUNT(*) FROM {t[0]}').fetchone()[0]
    print(f'  {t[0]}: {count} rows')
con.close()
"
```

Une base saine doit contenir au minimum plusieurs millions de lignes dans `imdb_akas` et plusieurs centaines de milliers dans `imdb_basics`.

---

## Voir aussi

<div class="grid cards" markdown>

-   :material-database: **[Dumps et restauration](../configuration/dump-restore.md)**

    Système complet de sauvegarde (DuckDB, Meilisearch, PostgreSQL), transfert entre pairs, configuration

-   :material-movie-search: **[Matching IMDB](details-imdb.md)**

    Schéma des tables DuckDB, algorithme de matching en 4 passes

-   :material-rocket-launch: **[Population initiale](population-initiale.md)**

    Tutoriel de peuplement des caches sur une nouvelle instance

</div>
