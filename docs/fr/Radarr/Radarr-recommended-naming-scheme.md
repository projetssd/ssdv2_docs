# Schéma de dénomination recommandé

Sur le [Radar Discord](https://radar.video/discord){:target="_blank" rel="noopener noreferrer"}, les gens demandent souvent : "Quelle est la meilleure façon de
nommez vos fichiers ?" Tout d'abord, c'est une préférence personnelle, mais il est souvent recommandé d'ajouter des informations non récupérables.

Pourquoi?

Si, pour une raison quelconque, vous devez effectuer une réinstallation ou une réimportation dans
les applications Starr ou Plex/Emby/Jellyfin, c'est bien d'avoir toutes ces informations dans le nom de fichier donc
il est importé correctement et ne correspond pas incorrectement à HDTV ou WEB-DL, etc.

Les jetons non disponibles dans la version ne seront pas utilisés/affichés.

------

## Préparation

Allez dans « Paramètres » => « Gestion des médias » et assurez-vous que « Afficher avancé » en haut est activé.

![Activer Avancé](images/radar-show-adavanced.png)

Une fois que vous avez cliqué sur le bouton, cela devrait ressembler à ceci et vous devriez voir toutes les options avancées.

![Afficher avancé](images/unhide-advanced.png)

## Format de film standard

Ce schéma de dénomination est conçu pour être compatible avec le [Nouvel Agent Plex](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517) {:target="_blank" rel="noopener noreferrer"} qui prend désormais en charge les ID IMDb et TMDb dans les noms de fichiers, si vous n'en avez pas besoin ou si vous le souhaitez, supprimez simplement `{imdb-{ImdbId}}`

!!! avertissement "À partir de la version 4.2.2.6489, Radarr prend désormais en charge les balises Plex Multiple Edition dans la dénomination."

    Si vous utilisez une version inférieure ou si vous n'en avez pas besoin, remplacez-la :

    `{edition-{Edition Tags}}` avec `{Edition Tags}`

    !!! danger "N'utilisez `{edition-{Edition Tags}}` que si vous êtes prêt à avoir des films séparés par édition<br>lorsque vous utilisez une bibliothèque Plex fusionnée - par exemple, vous conservez les versions 1080p et 2160p d'un film.<br> <br>Par exemple, si vous avez « Directors Cut » et « Extended Cut » pour un film, ceux-ci apparaîtront comme deux films distincts dans votre bibliothèque.<br><br>Notez que vous n'utilisez pas `{edition-{ Les balises d'édition}}` empêcheront Plex de reconnaître l'édition. "

###Plex

```bash
{{ radarr['naming']['radarr-naming']['file']['default'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre du film (2010) {imdb-tt0066921} {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`

#### Plex Anime

```bash
{{ radarr['naming']['radarr-naming']['file']['anime'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre du film (2010) {imdb-tt0066921} {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`

### Emby

```bash
{{ radarr['naming']['radarr-naming']['file']['emby'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre du film (2010) [imdbid-tt0066921] - {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`

#### Emby Anime

```bash
{{ radarr['naming']['radarr-naming']['file']['anime-emby'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre du film (2010) [imdbid-tt0066921] - {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`

### Gelée

```bash
{{ radarr['naming']['radarr-naming']['file']['jellyfin'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre du film (2010) [imdbid-tt0066921] - {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`

#### Jellyfin Anime

```bash
{{ radarr['naming']['radarr-naming']['file']['anime-jellyfin'] }}
```

??? résumé "RESULTATS : - [Cliquez pour afficher/masquer]"

    `Le titre du film (2010) [imdbid-tt0066921] - {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`

------

## Titre original vs nom de fichier original

### Titre original

Une autre option consiste à utiliser « {Titre original} » plutôt que le schéma de dénomination recommandé décrit ci-dessus. `{Titre original}` utilisera le titre de la version qui contiendra toutes les informations incluses dans la version elle-même. L'avantage de ce schéma de dénomination est d'éviter les boucles de téléchargement qui peuvent se produire lors de l'importation lorsqu'il y a une différence entre le titre de la version et le contenu du fichier lui-même (par exemple, si le titre de la version indique DTS-ES mais que le contenu est en réalité DTS). L'inconvénient est moins de flexibilité dans la façon dont les fichiers sont nommés.

Si vous utilisez ce schéma de dénomination alternatif, je suggère d'utiliser `{Titre original}` plutôt que `{Nom de fichier original}`

Pourquoi?

Le nom du fichier peut être masqué là où le nom de la version ne l'est pas, en particulier lorsque vous utilisez Usenet.

`{Titre original}` => `The.Movie.Title.2010.REMASTERED.1080p.BluRay.x264-GROUP`

`{Nom de fichier original}` => `group-karatekid-1080p` ou `lchd-tkk1080p` ou `t1i0p3s7i8yuti`

------

## Format du dossier de film

!!! danger ""

    **Veuillez noter que des noms de dossiers sont créés (dans la base de données) chaque fois que le film est ajouté à Radarr, et ils peuvent être manquants ou incorrects à ce moment-là et votre dossier aurait un identifiant vide !!!**

    Si vous l'ajoutez plutôt dans le nom du fichier, l'ID IMDb sera fraîchement extrait pour tout téléchargement ou mise à niveau.

    Un autre inconvénient potentiel de son utilisation dans le dossier est que les renommages de dossiers sont complexes, longs et potentiellement destructeurs dans Radarr par rapport aux renommages de fichiers.

### Minimum nécessaire et recommandé

```bash
{{ radarr['naming']['radarr-naming']['folder']['default'] }}
```

<small>RESULTAT :</small> `Le titre du film (2010)`

------

!!! note
    Gardez à l'esprit que l'ajout d'autre chose après l'année de sortie pourrait poser des problèmes lors d'une nouvelle importation dans Radarr, mais cela aide pour les films qui ont le même nom de sortie et la même année.

    ** Radarr prend en charge l'ID IMDb et l'ID TMDb dans le nom du dossier. **

    !!! citation "Citation d'un développeur"

        TMDb est généralement meilleur car il garantit une correspondance, IMDb n'est mis en correspondance que si l'entrée TMDb a la bonne association d'ID IMDb. Nous ne parlons pas réellement à IMDb.

#### Format de dossier de films en option

Ce schéma de dénomination est conçu pour être compatible avec le nouveau [Scanner Plex TV Series](https://forums.plex.tv/t/beta-new-plex-tv-series-scanner/696242){:target="_blank " rel="noopener noreferrer"} qui prend désormais en charge les ID IMDB et TVDB dans les noms de fichiers.

##### Plex en option

```bash
{{ radarr['naming']['radarr-naming']['folder']['plex'] }}
```

<small>RESULTAT :</small> `Le titre du film (2010) {imdb-tt1520211}`

##### Emby facultatif

```bash
{{ radarr['naming']['radarr-naming']['folder']['emby'] }}
```

<small>RESULTAT :</small> `Le titre du film (2010)`

##### Jellyfin en option

```bash
{{ radarr['naming']['radarr-naming']['folder']['jellyfin'] }}
```

<small>RESULTAT :</small> `Le titre du film (2010) [imdbid-tt1520211]`

!!! conseil
    Les identifiants IMDb seront très précis et changeront rarement, les identifiants TVDB/TMDB, en revanche, changent ou sont supprimés plus fréquemment.

------

Merci:

Un grand merci à [fryfrog](https://github.com/fryfrog) et [rg9400](https://github.com/rg9400) pour les suggestions.

