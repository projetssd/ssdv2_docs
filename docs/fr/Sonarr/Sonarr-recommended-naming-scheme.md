# Schéma de dénomination recommandé

Sur le [Sonarr Discord](https://discord.gg/M6BvZn5){:target="_blank" rel="noopener noreferrer"}, les gens demandent souvent : "Quelle est la meilleure façon de
nommez vos fichiers ?" Tout d'abord, c'est une préférence personnelle, mais il est souvent recommandé d'ajouter des informations non récupérables.

Pourquoi?

Si, pour une raison quelconque, vous devez effectuer une réinstallation ou une réimportation dans
les applications Starr ou Plex/Emby/Jellyfin, c'est bien d'avoir toutes ces informations dans le nom de fichier donc
il est importé correctement et ne correspond pas incorrectement à HDTV ou WEB-DL, etc.

!!! info "Les jetons non disponibles dans la version ne seront pas utilisés/affichés."

------

## Préparation

Allez dans « Paramètres » => « Gestion des médias » et assurez-vous que « Afficher avancé » en haut est activé.

![Activer Avancé](images/sonarr-show-adavanced.png)

Une fois que vous avez cliqué sur le bouton, cela devrait ressembler à ceci et vous devriez voir toutes les options avancées.

![Afficher avancé](images/unhide-advanced.png)

## Format d'épisode standard

```bash
{{ sonarr['naming']['sonarr-naming']['episodes']['standard']['default:4'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    Épisode unique :

    `Le titre de la série ! (2010) - S01E01 - Titre de l'épisode 1 [AMZN WEBDL-1080p Proper][DV HDR10][DTS 5.1][x264]-RlsGrp`

    Épisode multiple :

    `Le titre de la série ! (2010) - S01E01-E03 - Titre de l'épisode [AMZN WEBDL-1080p Proper][DV HDR10][DTS 5.1][x264]-RlsGrp`

------

## Format des épisodes quotidiens

```bash
{{ sonarr['naming']['sonarr-naming']['episodes']['daily']['default:4'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre de la série ! (2010) - 30/10/2013 - Titre de l'épisode 1 [AMZN WEBDL-1080p Proper][DV HDR10][DTS 5.1][x264]-RlsGrp`

------

## Format des épisodes d'anime

```bash
{{ sonarr['naming']['sonarr-naming']['episodes']['anime']['default:4'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    Épisode unique :

    `Le titre de la série ! (2010) - S01E01 - 001 - Titre de l'épisode 1 [iNTERNAL HDTV-720p v2][HDR10][10bit][x264][DTS 5.1][JA]-RlsGrp`

    Épisode multiple :

    `Le titre de la série ! (2010) - S01E01-E03 - 001-003 - Titre de l'épisode [iNTERNAL HDTV-720p v2][HDR10][10bit][x264][DTS 5.1][JA]-RlsGrp`

------

Format de dossier de la série ###

```bash
{{ sonarr['naming']['sonarr-naming']['series']['default'] }}
```

<small>RESULTAT :</small> `Le titre de la série ! (2010)

#### Format de dossier de série facultatif

Ce schéma de dénomination est conçu pour être compatible avec le nouveau [Scanner Plex TV Series](https://forums.plex.tv/t/beta-new-plex-tv-series-scanner/696242){:target="_blank " rel="noopener noreferrer"} qui prend désormais en charge les ID IMDB et TVDB dans les noms de fichiers.

##### Plex en option

```bash
{{ sonarr['naming']['sonarr-naming']['series']['plex'] }}
```

<small>RESULTAT :</small> `Le titre de la série ! (2010) {imdb-tt1520211}`

##### Emby facultatif

```bash
{{ sonarr['naming']['sonarr-naming']['series']['emby'] }}
```

<small>RESULTAT :</small> `Le titre de la série ! (2010)

##### Jellyfin en option

```bash
{{ sonarr['naming']['sonarr-naming']['series']['jellyfin'] }}
```

<small>RESULTAT :</small> `Le titre de la série ! (2010) [tvdbid-tt1520211]`

!!! conseil
    Les identifiants IMDb seront très précis et changeront rarement, les identifiants TVDB/TMDB, en revanche, changent ou sont supprimés plus fréquemment.

------

### Format du dossier de saison

Pour cela, il n’y a qu’une seule véritable option à utiliser à mon avis.

```bash
Saison {saison:00}
```

RÉSULTAT : `Saison 01`

------

### Style multi-épisodes

```bash
Plage préfixée
```

RÉSULTATS:

![résultats](images/results.png)

------

## Titre original vs nom de fichier original

### Titre original

Une autre option consiste à utiliser « {Titre original} » plutôt que le schéma de dénomination recommandé décrit ci-dessus. `{Titre original}` utilisera le titre de la version qui contiendra toutes les informations incluses dans la version elle-même. L'avantage de ce schéma de dénomination est d'éviter les boucles de téléchargement qui peuvent se produire lors de l'importation lorsqu'il y a une différence entre le titre de la version et le contenu du fichier lui-même (par exemple, si le titre de la version indique DTS-ES mais que le contenu est en réalité DTS). L'inconvénient est moins de flexibilité dans la façon dont les fichiers sont nommés.

Si vous utilisez ce schéma de dénomination alternatif, je suggère d'utiliser `{Titre original}` plutôt que `{Nom de fichier original}`

Pourquoi?

Le nom du fichier peut être masqué là où le nom de la version ne l'est pas, en particulier lorsque vous utilisez Usenet.

`{Titre original}` => `The.Series.Title.S01E01.Episode.Title.1080p.AMZN.WEB-DL.DDP5.1.H.264-RlsGrp`

`{Nom de fichier original}` => `afficher l'épisode 1-1080p` ou `lchd-tkk1080p` ou `t1i0p3s7i8yuti`

------

Merci:

Un grand merci à [fryfrog](https://github.com/fryfrog), [rg9400](https://github.com/rg9400) et [bakerboy448](https://github.com/bakerboy448) pour le suggestions.

