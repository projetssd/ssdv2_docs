# Paramètres de qualité (taille du fichier)

On me pose souvent la question : « Quels sont les meilleurs paramètres de qualité à utiliser ? »
Eh bien, c'est en fait une préférence personnelle, je vais donc vous montrer mes recommandations.

Mais avant de continuer à lire, comme pour tous mes guides :

!!! danger ""
    **Si vous ne vous souciez pas de la qualité, arrêtez de lire et voyez si les autres tutoriels vous sont utiles.**

Ces paramètres de qualité ont été créés et testés avec des informations obtenues auprès d'autres personnes et publient des comparaisons provenant de différentes sources.

Je fais moi-même du WEB-DL uniquement pour les émissions de télévision car, à mon avis, le WEB-DL est le juste milieu entre la qualité et la taille et de toute façon, on ne voit souvent pas de grandes différences pour les émissions de télévision. (Sauf pour les émissions comme GOT, Vikings, etc.)

??? question "FAQ"

    ## FAQ

    **Q : Pourquoi diffusez-vous uniquement à partir de HDTV720p ?**

    R : Avec les grands écrans de nos jours, tout ce qui est inférieur ne semble pas regardable.

    **Q : Pourquoi avez-vous défini certaines tailles si haut ?**

    R : Vous n'avez probablement pas lu le texte en gras ci-dessus, je dois également garder à l'esprit les versions Usenet qui sont souvent plus volumineuses que les versions torrent.

    **Q : Vous avez remarqué que certains épisodes ne sont pas capturés à cause de ces paramètres.**

    R : Si vous remarquez que certains épisodes ne seront pas récupérés à cause de ces paramètres de taille, vous pouvez m'en fournir une preuve avec une capture d'écran et l'erreur qu'elle vous montre lorsque vous effectuez une recherche interactive (non expurgée sauf l'indexeur/tracker si vous le souhaitez). à).

    - Je n'accepterai que les modifications qui sont des versions internationales. Pas de versions multilingues ou doublées.
    - Je n'accepterai pas de versions sources mal étiquetées comme celles de MeGusta, etc. (Ils devraient d'abord apprendre à nommer correctement leurs contenus)
    - Je n'accepterai pas de modifications pour les versions de taille micro.
    - Les documentaires et les dessins animés sont souvent beaucoup plus petits donc je ne les monterai probablement pas non plus.

------

## Sonarr Quality Definitions

| Quality                                                            | Minimum (Megabytes Per Minute)                                 | Maximum (Megabytes Per Minute)                                 |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------- |
| {{ sonarr['quality-size']['series']['qualities'][0]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][0]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][0]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][1]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][1]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][1]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][2]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][2]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][2]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][3]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][3]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][3]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][4]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][4]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][4]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][5]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][5]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][5]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][6]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][6]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][6]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][7]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][7]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][7]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][8]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][8]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][8]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][9]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][9]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][9]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][10]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][10]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][10]['max'] }} |
| {{ sonarr['quality-size']['series']['qualities'][11]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][11]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][11]['max'] }} |
| {{ sonarr['quality-size']['series']['qualities'][12]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][12]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][12]['max'] }} |
| {{ sonarr['quality-size']['series']['qualities'][13]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][13]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][13]['max'] }} |

------

### Sonarr Quality Definitions - Anime

| Quality                                                           | Minimum (Megabytes Per Minute)                                | Maximum (Megabytes Per Minute)                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| {{ sonarr['quality-size']['anime']['qualities'][0]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][0]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][0]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][1]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][1]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][1]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][2]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][2]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][2]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][3]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][3]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][3]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][4]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][4]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][4]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][5]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][5]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][5]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][6]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][6]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][6]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][7]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][7]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][7]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][8]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][8]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][8]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][9]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][9]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][9]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][10]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][10]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][10]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][11]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][11]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][11]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][12]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][12]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][12]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][13]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][13]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][13]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][14]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][14]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][14]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][15]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][15]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][15]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][16]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][16]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][16]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][17]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][17]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][17]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][18]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][18]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][18]['max'] }} |

!!! note
    La raison pour laquelle vous ne voyez pas le score « Préféré » dans le tableau ci-dessus est que nous voulons de toute façon une qualité maximale. Alors réglez-le le plus haut possible.

    La qualité préférée la plus élevée que vous pouvez saisir manuellement est inférieure de 1 à la qualité maximale. Si vous utilisez le curseur, la qualité préférée peut être jusqu'à 5 inférieure à la qualité maximale.

    Assurez-vous d'avoir activé « Afficher avancé » dans Sonarr, si vous ne voyez pas de disposition pour saisir les scores, sous les paramètres de qualité.

