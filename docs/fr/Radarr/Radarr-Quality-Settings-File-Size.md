# Paramètres de qualité (taille du fichier)

On me pose souvent la question : « Quels sont les meilleurs paramètres de qualité à utiliser ? »
Eh bien, c'est en fait une préférence personnelle, je vais donc vous montrer mes recommandations.

Mais avant de continuer à lire, comme pour tous mes guides :

!!! danger ""
    **Si vous ne vous souciez pas de la qualité, arrêtez de lire et voyez si les autres tutoriels vous sont utiles.**

Ces paramètres de qualité ont été créés et testés avec des informations obtenues auprès d'autres personnes et publient des comparaisons provenant de différentes sources.

??? question "FAQ - [Cliquez pour afficher/masquer]"

    ## FAQ

    **Q : Pourquoi diffusez-vous uniquement à partir de HDTV720p ?**

    R : Avec les grands écrans de nos jours, tout ce qui est inférieur ne semble pas regardable.

    **Q : Pourquoi certaines tailles sont-elles définies au maximum ?**

    R : Vous n'avez probablement pas lu le texte en gras ci-dessus

    **Q : Lorsque je règle Bluray sur la taille MAX, j'obtiens souvent la structure des dossiers ISO/Bluray.**

    R : Vous avez probablement mal configuré vos profils de qualité et activé BR-DISK et vous n'avez pas ajouté le profil personnalisé recommandé pour aider Radarr à le bloquer/l'ignorer. [BR-DISK](/Radarr/Radarr-collection-of-custom-formats/#br-disk){:target="_blank" rel="noopener noreferrer"}

    **Q : Certains films ne seront pas capturés à cause de ces paramètres.**

    R : Si vous remarquez que certains films ne seront pas récupérés à cause de ces paramètres de taille, vous pouvez m'en fournir la preuve avec une capture d'écran et l'erreur qu'elle vous montre lorsque vous effectuez une recherche interactive (non expurgée sauf l'indexeur/tracker si vous le souhaitez). à).

    - Je n'accepterai que les modifications qui sont des versions internationales. Pas de versions multilingues ou doublées.
    - Je n'accepterai pas de versions sources mal étiquetées comme celles de MeGusta, etc. (Ils devraient d'abord apprendre à nommer correctement leurs contenus)
    - Je n'accepterai pas de modifications pour les versions de taille micro.
    - Les documentaires et les dessins animés sont souvent beaucoup plus petits donc je ne les monterai probablement pas non plus.

------

## Radarr Quality Definitions

- Note that `400` is the displayed value for Unlimited

| Quality                                                           | Minimum (Megabytes Per Minute)                                | Maximum (Megabytes Per Minute)                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| {{ radarr['quality-size']['movie']['qualities'][0]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][0]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][0]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][1]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][1]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][1]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][2]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][2]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][2]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][3]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][3]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][3]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][4]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][4]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][4]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][5]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][5]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][5]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][6]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][6]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][6]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][7]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][7]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][7]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][8]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][8]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][8]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][9]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][9]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][9]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][10]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][10]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][10]['max'] }} |
| {{ radarr['quality-size']['movie']['qualities'][11]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][11]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][11]['max'] }} |
| {{ radarr['quality-size']['movie']['qualities'][12]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][12]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][12]['max'] }} |
| {{ radarr['quality-size']['movie']['qualities'][13]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][13]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][13]['max'] }} |

!!! note
    La raison pour laquelle vous ne voyez pas le score « Préféré » dans le tableau ci-dessus est que nous voulons de toute façon une qualité maximale. Alors réglez-le le plus haut possible.

    La qualité préférée la plus élevée que vous pouvez saisir manuellement est inférieure de 1 à la qualité maximale. Si vous utilisez le curseur, la qualité préférée peut être jusqu'à 5 inférieure à la qualité maximale.

    Assurez-vous d'avoir activé « Afficher avancé » dans Radarr, si vous ne voyez pas de disposition permettant de saisir les scores, sous les paramètres de qualité.
