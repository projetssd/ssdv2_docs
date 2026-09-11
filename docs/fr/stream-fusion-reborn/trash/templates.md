# :material-layers: Templates de scoring

Un **template de scoring** est un profil JSON qui associe un **poids entier** à chaque Custom Format (CF). Quand un torrent est analysé, le moteur additionne les poids de tous les CFs qui matchent — le score final détermine le classement des résultats.

Quand un template est actif, il **remplace entièrement** les filtres globaux de l'application (langue, taille, qualité). Les filtres globaux ne servent de fallback que si aucun template n'est configuré.

---

## Structure JSON complète

```json
{
  "slug": "mon-template",
  "name": "Mon Template",
  "description": "Un template personnalisé pour mes préférences",
  "config": {
    "scores": {
      "vff": 500,
      "vfi": 450,
      "multi": 300,
      "1080p": 200,
      "remux-tier-01": 600,
      "lq": -8000,
      "cam": -10000
    },
    "constraints": {
      "relegate_below": -5000,
      "remove_below": null
    },
    "weights": {
      "rtn_base": 0.0,
      "cf_score": 1.0,
      "language_bonus": 0.8
    },
    "language_prefs": {
      "preferred_audio": ["fr", "multi"],
      "preferred_subs": ["fr", "none"],
      "must_have_french_audio": false
    },
    "size_rules": [
      { "source": "remux",  "resolution": null,    "min_gb": 20, "max_gb": 60,  "behavior": "remove" },
      { "source": "bluray", "resolution": null,    "min_gb": 10, "max_gb": 50,  "behavior": "remove" },
      { "source": "web-dl", "resolution": "2160p", "min_gb": 8,  "max_gb": 30,  "behavior": "remove" },
      { "source": "web-dl", "resolution": null,    "min_gb": 5,  "max_gb": 20,  "behavior": "remove" },
      { "source": "webrip", "resolution": null,    "min_gb": 2,  "max_gb": 15,  "behavior": "remove" },
      { "source": "default","resolution": null,    "min_gb": null,"max_gb": null,"behavior": "remove" }
    ]
  }
}
```

---

## Référence des champs

### `scores` *(obligatoire)*

Dictionnaire `{slug_ou_trash_id → poids}`. Chaque clé peut être :

1. **Un slug de CF** (recommandé) : `vff`, `2160p`, `remux-tier-01`
2. **Un `trash_id` brut** : `404c08fd0bd67f39b4d8e5709319094e`

Le moteur calcule un `cf_raw_score` = somme des poids des CFs qui matchent le torrent.

---

### `constraints`

| Champ | Type | Défaut | Description |
|-------|------|--------|-------------|
| `relegate_below` | `int` | `-10000` | Torrents avec `score < relegate_below` → **relégués en fin de liste** (visibles, mais après les autres) |
| `remove_below` | `int\|null` | `null` | Torrents avec `score < remove_below` → **retirés définitivement** de la liste. `null` = désactivé |

!!! tip "Reléguer vs Supprimer"
    - `relegate_below` : le torrent reste visible, en dernier. L'utilisateur peut le choisir manuellement.
    - `remove_below` : le torrent disparaît complètement. À utiliser pour les releases absolument indésirables (CAM, TS).

!!! note "Rétrocompatibilité"
    L'ancien champ `ban_below` (à la racine de `config` ou dans `constraints`) est toujours lu et mappé vers `relegate_below` automatiquement.

---

### `weights`

Multiplicateurs appliqués à chaque composante du score final :

```
score_final = rtn_base × rtn_score + cf_score × cf_raw + language_bonus × lang_score
```

| Champ | Type | Défaut | Composante |
|-------|------|--------|------------|
| `rtn_base` | `float` | `0.0` | `rtn_score` = `source_id × 100` (0–1000, qualité RTN : Remux=1000, BluRay=900…) |
| `cf_score` | `float` | `1.0` | `cf_raw` = somme des poids CF matchés |
| `language_bonus` | `float` | `0.0` | `lang_score` = bonus selon `preferred_audio` (voir ci-dessous) |

**Valeurs par défaut** (`rtn_base=0, cf_score=1, language_bonus=0`) → comportement identique à un template sans `weights` : seul le CF score compte.

**Exemple — donner un bonus langue de ~800 pts :**
```json
"weights": { "rtn_base": 0.0, "cf_score": 1.0, "language_bonus": 0.8 }
```
Avec `language_bonus=0.8`, un torrent dont l'audio correspond à `preferred_audio[0]` reçoit `0.8 × 1000 = +800` pts.

---

### `language_prefs`

Préférences de langue utilisées pour calculer le `lang_score` et filtrer les torrents.

| Champ | Type | Description |
|-------|------|-------------|
| `preferred_audio` | `list[str]` | Langues audio par ordre de préférence. Premier match = score plein, deuxième = moitié, etc. |
| `preferred_subs` | `list[str]` | Langues de sous-titres préférées (informatif, non encore scoré) |
| `must_have_french_audio` | `bool` | Si `true` : les torrents sans langue `fr` sont **retirés** de la liste |

**Calcul du `lang_score` :**

| Match | Score |
|-------|-------|
| `preferred_audio[0]` | +1000 |
| `preferred_audio[1]` | +500 |
| `preferred_audio[2]` | +250 |
| Aucun match | 0 |

!!! info "Remplacement du filtre langue global"
    Quand un template est actif, `language_prefs` remplace le filtre de langue global de l'application. Si `language_prefs` n'est pas défini dans le template, aucun filtrage de langue n'est appliqué (le template gère la langue via les scores CF).

---

### `size_rules`

Liste de règles de taille par source et résolution, évaluées **dans l'ordre** (première règle qui matche gagne).

```json
"size_rules": [
  { "source": "remux",  "resolution": null,    "min_gb": 20, "max_gb": 60,  "behavior": "remove" },
  { "source": "web-dl", "resolution": "2160p", "min_gb": 8,  "max_gb": 30,  "behavior": "remove" },
  { "source": "web-dl", "resolution": null,    "min_gb": 5,  "max_gb": 20,  "behavior": "remove" },
  { "source": "default","resolution": null,    "min_gb": null,"max_gb": null,"behavior": "remove" }
]
```

| Champ | Valeurs | Description |
|-------|---------|-------------|
| `source` | `remux`, `bluray`, `web-dl`, `webrip`, `hdtv`, `dvd`, `cam`, `default` | Source qualité RTN. `default` = fallback si aucune autre règle ne matche |
| `resolution` | `"2160p"`, `"1080p"`, `"720p"`, `"480p"`, `null` | Résolution ciblée. `null` = toute résolution |
| `min_gb` | `float\|null` | Taille minimum en Go. `null` = pas de borne basse |
| `max_gb` | `float\|null` | Taille maximum en Go. `null` = pas de borne haute |
| `behavior` | `"remove"`, `"relegate"` | `remove` = torrent retiré de la liste ; `relegate` = torrent relégué en fin de liste |

**Sources disponibles (Radarr IDs) :**

| `source` | Source ID | Qualité reconnue |
|----------|-----------|-----------------|
| `remux` | 10 | Remux, REMUX, BluRay REMUX |
| `bluray` | 9 | BluRay, Blu-ray, BDRip, BRRip |
| `web-dl` | 7 | WEB-DL, WebDL, WEB |
| `webrip` | 8 | WEBRip, WebRip |
| `hdtv` | 6 | HDTV |
| `dvd` | 5 | DVD, DVDRip |
| `cam` | 1–4 | CAM, TS, TC, Telecine |

!!! info "Remplacement du filtre taille global"
    Quand un template est actif, `size_rules` remplace le filtre de taille global. Si aucune `size_rules` n'est définie, aucun filtrage de taille n'est appliqué par le template.

---

## Ordering des résultats (CF actif)

Quand un template est actif, l'ordre final des résultats Stremio suit cette hiérarchie :

1. **Non-relégué + Instant** (debrid cached) — score le plus élevé en tête
2. **Relégué + Instant** (debrid cached, mais sous `relegate_below`)
3. **Non-relégué + DL** (à envoyer au debrid)
4. **Relégué + DL**

Le contenu disponible instantanément est toujours prioritaire sur le contenu à télécharger, quel que soit son statut de relégation.

---

## Les clés `scores` — slugs et alias

Chaque clé du dictionnaire `scores` peut être :

1. **Un slug de CF** (recommandé) : `vff`, `2160p`, `remux-tier-01`
2. **Un `trash_id` brut** : `404c08fd0bd67f39b4d8e5709319094e`
3. **Un alias interne** : `bluray-tier-01` → résolu vers `uhd-bluray-tier-01`

!!! tip "Slugs vs trash_ids"
    Utilisez **toujours les slugs** dans vos templates personnalisés. Ils sont lisibles, stables, et le sync les résout automatiquement.

### Alias de slugs

| Alias écrit | Résolu vers |
|---|---|
| `fr-scene-groups` | `french-scene` |
| `french-lq-groups` | `french-lq` |
| `low-quality-groups` | `lq` |
| `hq-release-groups` | `mainframe` |
| `hq-audio` | `dts-hd-ma` |
| `hdr10` | `hdr` |
| `hdr10plus` | `hdr10plus-boost` |
| `dolby-vision` | `dv-boost` |
| `atmos` | `truehd-atmos` |
| `bluray-tier-01` | `uhd-bluray-tier-01` |
| `bluray-tier-02` | `uhd-bluray-tier-02` |

---

## Templates système

Les templates système sont importés depuis le [dépôt miroir](https://github.com/LimeHubs/streamfusion-trash-mirror/tree/main/templates). Ils sont **protégés** et mis à jour automatiquement à chaque sync.

| Slug | Nom | Langue | Résolution |
|---|---|---|---|
| `vff-vfi-hd` | VFF/VFI HD | VFF/VFI | 1080p |
| `vff-vfi-uhd` | VFF/VFI UHD | VFF/VFI | 2160p |
| `vff-vfi-web` | VFF/VFI WEB Compact | VFF/VFI | 1080p WEB |
| `vff-vfi-uhd-web` | VFF/VFI UHD WEB | VFF/VFI | 2160p WEB |
| `multi-hd` | MULTi HD | MULTi | 1080p |
| `multi-uhd` | MULTi UHD | MULTi | 2160p HDR |
| `vostfr-hd` | VOSTFR HD | VOSTFR | 1080p |
| `remux-cinephile` | Remux Cinéphile | Toutes | Remux |
| `anime-vf` | Animé VF | VFF/VFI/VOSTFR | Variable |
| `anime-multi` | Animé MULTi | MULTi/Dual | Variable |

!!! tip "Cloner pour personnaliser"
    Les templates système sont en **lecture seule**. Pour les modifier : **TRaSH → Templates → Cloner**.

---

## Guide : créer un template personnalisé

### Étape 1 — Cloner un template de base

1. Allez dans l'admin : `/admin/quality/templates`
2. Trouvez le template le plus proche de vos besoins
3. Cliquez **Cloner** — cela crée une copie `source = user` jamais écrasée par la sync

### Étape 2 — Configurer les scores et contraintes

```json
{
  "scores": {
    "vff": 500, "vfi": 450, "multi": 300, "vostfr": 100,
    "1080p": 200, "2160p": 300,
    "remux-tier-01": 600, "web-tier-01": 400,
    "lq": -8000, "cam": -10000
  },
  "constraints": {
    "relegate_below": -5000,
    "remove_below": null
  }
}
```

### Étape 3 — Ajouter langue et taille (optionnel)

```json
{
  "weights": { "rtn_base": 0.0, "cf_score": 1.0, "language_bonus": 0.8 },
  "language_prefs": {
    "preferred_audio": ["fr", "multi"],
    "must_have_french_audio": false
  },
  "size_rules": [
    { "source": "remux",  "resolution": null, "min_gb": 20, "max_gb": 60, "behavior": "remove" },
    { "source": "web-dl", "resolution": null, "min_gb": 5,  "max_gb": 25, "behavior": "remove" }
  ]
}
```

### Étape 4 — Tester

Utilisez le [Testeur de CF](admin.md#testeur-de-custom-formats) pour vérifier le classement sur des titres réels.

---

## Export et import

- **Exporter** : bouton **Exporter JSON** dans l'admin → fichier `.json` au format du miroir
- **Importer** : coller le JSON dans un nouveau template dans l'admin
- **Partager** : proposez une PR dans le dossier `templates/` du [dépôt miroir](https://github.com/LimeHubs/streamfusion-trash-mirror)

---

## Contribution au miroir

1. Exportez votre template au format JSON
2. Proposez une PR sur [github.com/LimeHubs/streamfusion-trash-mirror](https://github.com/LimeHubs/streamfusion-trash-mirror)
3. Placez le fichier dans `templates/`

Les templates communautaires sont reviewés avant intégration.
