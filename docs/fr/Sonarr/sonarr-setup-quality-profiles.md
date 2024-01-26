# Comment configurer des profils de qualité

*alias Comment configurer des formats personnalisés*<br><br>
Alors, quelle est la meilleure façon de configurer les formats personnalisés et lesquels utiliser avec quels scores pour configurer vos profils de qualité ?

Il n’existe pas de « meilleure » configuration, cela dépend de votre configuration multimédia (périphériques matériels) et de vos préférences personnelles.

Certains préfèrent un son de haute qualité (HD Audio), d’autres une vidéo de haute qualité. Beaucoup préfèrent les deux.

Ici, je vais essayer de vous expliquer comment tirer le meilleur parti des formats personnalisés pour vous aider à configurer vos profils de qualité en fonction de vos besoins personnels.

J'ai créé un [organigramme] (#quel-profil-de-qualité-devriez-vous-choisir) pour faciliter votre/vos décision/choix.

------

## Bases

Après avoir ajouté les formats personnalisés, comme expliqué dans [Comment importer des formats personnalisés](/Sonarr/sonarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
Vous devrez le configurer dans le profil de qualité que vous souhaitez utiliser/préférez utiliser les formats personnalisés.

`Paramètres` => `Profils`

![!cf-settings-profiles](images/cf-settings-profiles.png)

!!! info "Les formats personnalisés Sonarr peuvent être définis par profil et ne sont pas globaux"
Sélectionnez le profil que vous souhaitez utiliser/préférer.

![!cf-quality-profiles](images/cf-quality-profiles.png)

![!cf-profile-selected](images/cf-profile-selected.png)

1. Nom du profil.
1. Autorisez les mises à niveau. Sonarr arrêtera d’améliorer la qualité une fois que (3) sera satisfait.
1. Mettez à niveau jusqu'à la qualité sélectionnée.
1. Le « score minimum au format personnalisé » dont le téléchargement est autorisé. [Plus d'informations](#minimum-custom-format-score)
1. Continuez à mettre à niveau le format personnalisé jusqu'à ce que ce score soit atteint. (le définir sur « 0 » signifie qu'aucune mise à niveau n'aura lieu en fonction des formats personnalisés)

En bas, dans le profil que vous avez choisi, vous verrez les formats personnalisés ajoutés où vous pourrez commencer à configurer les scores.

??? succès "Exemple de capture d'écran - [Cliquez pour afficher/masquer]"
    ![!cf-quality-profile-cf](images/cf-quality-profile-cf.png)

    !!! avertissement
        Ces captures d'écran ne sont que des exemples pour vous montrer à quoi cela devrait ressembler et où vous devez placer les données que vous devez ajouter. Elles ne reflètent pas toujours à 100 % les données réelles et ne sont pas toujours à jour à 100 % avec les données réelles. données que vous devez ajouter.

        - Suivez toujours les données décrites dans le guide.
        - Si vous avez des questions ou n'êtes pas sûr, cliquez simplement sur le badge de discussion pour rejoindre la chaîne Discord où vous pourrez poser vos questions directement.

!!! info "Gardez à l'esprit que les formats personnalisés sont conçus pour affiner votre profil de qualité.<br>En général, la qualité l'emporte sur tout"

    Les formats personnalisés sont contrôlés par les profils de qualité.

    - Le score Upgrade Until empêche la mise à niveau une fois qu'une version avec ce score souhaité a été téléchargée.
    - Un score de 0 signifie que le format personnalisé est uniquement informatif.
    - Le score minimum exige que les versions atteignent ce seuil sinon elles seront rejetées.
    - Les formats personnalisés qui correspondent à des attributs indésirables doivent recevoir un score négatif pour réduire leur attrait.
    - Les rejets purs et simples devraient recevoir une note négative suffisamment faible pour que même si tous les autres formats avec des notes positives étaient ajoutés, la note resterait toujours en dessous du minimum.

------

{! include-markdown "../../includes/merge-quality/sonarrv4-current-logic.md" !}

------

## Quel profil de qualité choisir

??? résumé "Quel profil de qualité devriez-vous choisir - [Cliquez pour afficher/masquer]"

    ![Organigramme](/Sonarr/images/flowchart-quality-profiles-sonarr.png)

    Si vous n'êtes pas sûr ou si vous avez des questions, n'hésitez pas à demander de l'aide sur Discord

    [![Chat Discord](https://img.shields.io/discord/492590071455940612?style=for-the-badge&color=4051B5&logo=discord){ .off-glb }](https://trash-guides.info /discord){:target="_blank" rel="noopener noreferrer"}

------

## Profils de qualité TRaSH

Les profils de qualité suivants peuvent être combinés en un seul profil de qualité si vous souhaitez, par exemple, pouvoir passer de 1080p à 4K/2160p.

### WEB-1080p

Si vous préférez WEBDL 720p/1080p (WEB-1080p)

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

{! include-markdown "../../includes/cf/sonarr-optional.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-streaming-services.md" !}

{! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}

J'ai décidé de ne pas ajouter de formats personnalisés « Audio Advanced » au profil WEB. Vous trouverez difficilement de l'audio HD avec WEB-DL (la plupart des WEBDL les plus récents auront Atmos). Si vous voulez des formats audio HD, je vous suggère d'opter pour des Remux.

Utilisez les paramètres principaux suivants dans votre profil.

![!cf-profile-web1080](images/cf-profile-web1080.png)

!!! Info ""

    Pour certaines émissions plus anciennes, vous souhaiterez peut-être activer le « WEB 720p », ou même le « HDTV 1080p ».

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? résumé "Workflow Logic - [Cliquez pour afficher/masquer]"

    - Il téléchargera WEB-DL 1080p. (Si vous avez également activé « WEB 720p » et/ou « HDTV 1080p », la mise à niveau sera effectuée jusqu'à « Mise à niveau jusqu'à »)
    - Les médias téléchargés seront mis à niveau vers l'un des formats personnalisés ajoutés jusqu'à un score de 10 000.

    Alors pourquoi une « Mise à niveau jusqu'à la personnalisation » aussi ridiculement élevée et pas un score de « 100 » ?

    Parce que je suis trop paresseux pour calculer le maximum pour chaque profil de qualité que j'utilise, et je veux de toute façon qu'il passe au score le plus élevé possible.

------

### WEB-2160p

Si vous préférez WEBDL 2160p (WEB-2160p)

Le seul problème avec le 2160p est lorsque la version inclut le DV/HDR. Le 2160p sans DV/HDR présente un avantage minime.

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

{! include-markdown "../../includes/cf/sonarr-optional.md" !}

{! include-markdown "../../includes/cf/sonarr-optional-uhd.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-uhd-streaming-services.md" !}

{! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}

J'ai décidé de ne pas ajouter de formats personnalisés « Audio Advanced » au profil WEB. Vous trouverez difficilement de l'audio HD avec WEB-DL (la plupart des WEBDL les plus récents auront Atmos). Si vous souhaitez également des formats audio HD, je vous suggère d'opter pour les Remux.

Utilisez les paramètres principaux suivants dans votre profil.

![!cf-profile-web2160](images/cf-profile-web2160.png)

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? résumé "Workflow Logic - [Cliquez pour afficher/masquer]"

    - Cela téléchargera WEB-2160p avec HDR/DV.
    - Les médias téléchargés seront mis à niveau vers l'un des formats personnalisés ajoutés jusqu'à un score de 10 000.

    Alors pourquoi une « Mise à niveau jusqu'à la personnalisation » aussi ridiculement élevée et pas un score de « 100 » ?

    Parce que je suis trop paresseux pour calculer le maximum pour chaque profil de qualité que j'utilise, et je veux de toute façon qu'il passe au score le plus élevé possible.

------

## Groupes de formats personnalisés

Les groupes de formats personnalisés suivants doivent être combinés avec les profils de qualité ci-dessus. Les utilisateurs devront choisir les options et les formats personnalisés qu'ils préfèrent.

###Formats HDR

- Vous disposez d'un téléviseur 4K et d'un lecteur multimédia matériel (tel que Roku, AppleTV, Shield, SmartTV App, etc.) prenant en charge plusieurs formats HDR (tels que Dolby Vision, HDR10, HDR10+, etc.).

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

------

## FAQ et informations

### Pourquoi seulement WEB-DL

??? question "Pourquoi avez-vous uniquement un profil de version pour WEB-DL - [Cliquez pour afficher/masquer]"

    Je fais moi-même du WEB-DL uniquement pour les émissions de télévision. À mon avis, le WEB-DL est le juste milieu entre qualité et taille (de toute façon, on ne voit souvent pas de grandes différences pour les émissions de télévision) à l'exception des émissions comme GOT, Vikings, etc.

### Pourquoi préférer les groupes P2P

??? question "Pourquoi préférez-vous les groupes P2P aux groupes de scènes - [Cliquez pour afficher/masquer]"

    Les groupes de scène sont toujours pressés de sortir les sorties le plus rapidement possible.

    J'ai souvent remarqué que je recevais des Repacks/Propers de leur part, ou de différents groupes et qualités. Les groupes de versions P2P sont un peu plus intelligents et travaillent en quelque sorte ensemble, en ne faisant pas les mêmes versions. De plus, j'ai remarqué qu'avec certaines versions de scène, l'audio 5.1 était supprimé ou converti en audio AAC.

    À mon avis, les versions P2P sont de meilleure qualité. Cependant, il existe un groupe de scènes qui produit des versions de qualité `-deflate`/`-inflate`.

### Pourquoi tant de reconditionnements/propriétés

??? question "Pourquoi est-ce que je vois autant de repacks/propriétés d'Amazon WEB-DL ces derniers temps - [Cliquez pour afficher/masquer]"

    Une grande partie des WEB-DL d'Amazon au cours des dernières semaines n'avaient que 192 Kbps DD+5.1 (car c'est tout ce qu'Amazon avait initialement mis à disposition). L’audio DD+5.1 à 640 Kbit/s approprié peut apparaître quelques heures, voire quelques mois, plus tard. La version de qualité inférieure sera REMPACKÉE lorsque la qualité audio de meilleure qualité sera disponible.

### Propre et reconditionné

??? Astuce "Proper and Repacks - [Cliquez pour afficher/masquer]"

    Je vous suggère également de modifier les paramètres Propers et Repacks dans Radarr

    `Media Management` => `File Management` sur `Ne pas préférer` et utilisez le format personnalisé [Repack/Proper](/Sonarr/sonarr-collection-of-custom-formats/#repackproper).

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    De cette façon, vous vous assurez que les préférences de format personnalisé seront utilisées à la place.

### Formats personnalisés pour éviter certaines versions

??? question "Comment utiliser un format personnalisé pour éviter certaines versions ? - [Cliquez pour afficher/masquer]"

    Pour les formats personnalisés que vous voulez vraiment éviter, définissez-le sur quelque chose de très bas comme « -10000 » et non sur quelque chose comme « -10 ».
    Lorsque vous ajoutez votre format personnalisé préféré et que vous le définissez sur quelque chose comme `+10`, il est possible que, par exemple, le `BR-DISK` soit téléchargé - (-10)+(+10)=0 - si votre ` Le score minimum de format personnalisé est défini sur « 0 ».

### Versions à éviter

À mon avis, c'est un incontournable pour chaque profil de qualité que vous utilisez. Tous ces formats personnalisés garantissent que vous n'obtiendrez pas de versions de mauvaise qualité.

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

### Formats personnalisés avec un score de 0

??? question "Que font les formats personnalisés avec un score de 0 ? - [Cliquez pour afficher/masquer]"

    Tous les formats personnalisés avec un score de 0 sont purement informatifs et ne font rien.

### Score minimum du format personnalisé

??? info "Score minimum de format personnalisé - [Cliquez pour afficher/masquer]"

    Certaines personnes suggèrent de ne pas utiliser de scores négatifs pour vos formats personnalisés et de définir cette option sur un score supérieur à 0.

    La raison pour laquelle je ne préfère/n'utilise pas cela est parce que vous pourriez vous limiter lorsque de nouveaux groupes ou quoi que ce soit seront publiés.

    En outre, cela montre beaucoup plus clairement ce que vous préférez et ce que vous voulez éviter.

### Canaux audio

??? info "Canaux audio - [Cliquez pour afficher/masquer]"

    Ailleurs dans le guide, vous trouverez un groupe distinct de formats personnalisés appelés « Canaux audio ». Ceux-ci correspondront au nombre de canaux audio dans une version, par exemple 2.0 (stéréo) ou 5.1/7.1 (son surround). Personnellement, je n'ajouterais pas les formats personnalisés des canaux audio, car vous pourriez vous limiter dans le nombre de versions que vous pouvez obtenir. Utilisez-les uniquement si vous en avez un besoin spécifique.

    L'utiliser avec n'importe quel type de profil de qualité Remux est inutile, à mon avis, étant donné que 99% de tous les Remux sont de toute façon multi-audio. Vous pouvez obtenir de meilleurs scores simplement en utilisant les formats personnalisés « Audio Advanced ».

### Évitez d'utiliser le format personnalisé x264/x265

??? Astuce "Évitez d'utiliser le format personnalisé x264/x265 - [Cliquez pour afficher/masquer]"

    Évitez d'utiliser le format personnalisé x264/x265 avec une partition si possible, il est plus intelligent d'utiliser le [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection -of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} Format personnalisé.

    Quelque chose comme 95 % des fichiers vidéo sont au format x264 et offrent une bien meilleure prise en charge de la lecture directe. Si vous avez plus de quelques utilisateurs, vous remarquerez beaucoup plus de transcodage.

    Utilisez x265 uniquement pour les versions 4K et le [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd ){:target="_blank" rel="noopener noreferrer"} s'assure que vous disposez toujours des versions x265.

### Pourquoi est-ce que j'obtiens des couleurs violettes ou vertes

{! include-markdown "../../includes/cf/dv-info-green-purple.md" !}

### Profils Dolby Vision

{! include-markdown "../../includes/cf/dv-info-profiles.md" !}

## Merci

Un merci spécial à tous ceux qui ont contribué aux tests et à la création de ces formats personnalisés.

