# Comment configurer les profils de qualité Anime

*alias Comment configurer les formats personnalisés (Anime)*<br><br>

!!! note
    Ce guide est créé et maintenu par [FonduemangVI](https://github.com/FonduemangVI) et [rg9400](https://github.com/rg9400)

Il est recommandé d'exécuter deux instances Radarr. Un pour les films d'animation et un pour les films normaux, ou vous pouvez utiliser des profils de qualité et obtenir différents formats personnalisés (CF) selon vos besoins.

L'objectif de ce guide est de sélectionner la meilleure version globale (selon [SeaDex](https://releases.moe/){:target="_blank" rel="noopener noreferrer"}) et pas nécessairement seulement le double audio.
La grande majorité des sorties peuvent être trouvées sur [Nyaa](https://nyaa.si/){:target="_blank" rel="noopener noreferrer"} ou [AB](https://animebytes.tv/). {:target="_blank" rel="noopener noreferrer"}

!!! Info ""
    Nyaa est un tracker public tandis qu'AB est un tracker sur invitation uniquement.

---

## Gestion des médias

### Schéma de dénomination recommandé

Pour la dénomination, veuillez vous référer au [Schéma de dénomination recommandé](/Radarr/Radarr-recommended-naming-scheme/){:target="_blank" rel="noopener noreferrer"}

---

## Paramètres de qualité

Pour les paramètres de qualité, veuillez vous référer aux [Définitions de qualité Radarr](/Radarr/Radarr-Quality-Settings-File-Size/#radar-quality-definitions){:target="_blank" rel="noopener noreferrer"}

---

## Profil de qualité

Nous devons créer un nouveau profil appelé « Remux-1080p - Anime » en raison de la façon dont l'anime peut être nommé, nous devrons fusionner quelques qualités, voir [ici](/Radarr/Tips/Merge-quality/){:target ="_blank" rel="noopener noreferrer"} pour un exemple.

Nous devons ajouter `Bluray-1080p Remux` et `Bluray-1080p` dans un groupe ensemble, `HDTV-1080p` dans le même groupe que `WEBDL-1080p` et `WEBRip-1080p`, et enfin `HDTV-720p` dans le même groupe que `WEBDL-720p` et `WEBRip-720p` afin que la notation fonctionne correctement.

Allez dans `Paramètres` => `Profils`

![!cf-settings-profiles](images/cfa-settings-profiles.png)

![!cfa-mergedqualities](images/cfa-mergedqualities.png)

Nous devons ensuite sélectionner et organiser les qualités comme ci-dessous.

![!cfa-qualityorder](images/cfa-qualityorder.png)

---

## Anime CF/Score

!!! note
    Nous allons utiliser les formats personnalisés ci-dessous. Consultez [Comment importer des formats personnalisés](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"} pour savoir comment les importer.

### Notation par défaut

La notation qui a été définie est la notation recommandée, cependant certains CF sont facultatifs selon ce que vous préférez.
« Anime Dual Audio », « Non censuré » et « 10 bits » peuvent recevoir des scores positifs si vous souhaitez préférer le contenu avec ces attributs.

« Anime Raws » et « Dubs Only » ont un score négatif, mais si vous préférez ces attributs, vous pouvez leur donner un score positif.

Une fois les formats personnalisés importés, vous pouvez définir les scores comme ci-dessus. Pour ce faire, allez dans `Paramètres` => `Profils` et sélectionnez le profil `Remux-1080p - Anime` qui a été configuré auparavant.

![!cf-settings-profiles](images/cfa-settings-profiles.png)

Dans le profil, entrez les scores selon le tableau ci-dessus dans cette section.

![!cfa-default-scoring](images/cfa-default-scoring.png)

Une fois que vous avez terminé, cela devrait ressembler à l’image ci-dessus.

### Double notation audio

Si vous préférez les versions « Dual Audio », vous disposez de quelques options en fonction de vos préférences.

Si vous souhaitez préférer « Dual Audio » au sein du même niveau, donnez au « CF » un score de « 10 », si vous souhaitez qu'il soit préféré à un niveau supérieur, donnez au « CF » un score de « 101 », et si vous Si vous voulez le préférer à n'importe quel niveau, donnez au « CF » un score de « 2000 ».

Si vous devez disposer de versions « Dual Audio », définissez le « Score de format personnalisé minimum » sur 2000 dans le profil « Remux-1080p - Anime » que vous avez configuré précédemment.

En utilisant cette notation, vous bénéficierez toujours des niveaux si un meilleur groupe de versions réalise une version « Dual Audio ».

Vous trouverez ci-dessous un exemple de notation définie pour préférer « Dual Audio » à n'importe quel niveau.

![!cfa-da-scoring](images/cfa-da-scoring.png)

### Notation non censurée

!!! note
    La plupart des BD ne sont pas censurées par défaut, donc la plupart des groupes ne l'incluent pas dans le nom.

Si vous préférez les versions « non censurées », vous disposez de quelques options en fonction de vos préférences.

Si vous souhaitez préférer « Non censuré » au sein du même niveau, donnez au « CF » un score de « 10 », si vous souhaitez qu'il soit préféré à un niveau supérieur, donnez au « CF » un score de « 101 ».

En utilisant cette notation, vous bénéficierez toujours des niveaux si un meilleur groupe de versions réalise une version « non censurée ».

Vous trouverez ci-dessous un exemple de notation définie pour préférer « Non censuré » à un niveau supérieur.

![!cfa-uncensored-scoring](images/cfa-uncensored-scoring.png)

### Finir

Une fois que vous avez défini votre score préféré, vous devrez apporter deux modifications supplémentaires à votre profil « Remux-1080p - Anime ».

Assurez-vous que « Mises à niveau autorisées » est cochée, puis définissez la section « Mise à niveau jusqu'à » sur « Remux-1080p » et la « Mise à niveau jusqu'au score de format personnalisé » sur « 10000 » et définissez « Langue » sur « Original ».

Une fois cela fait, votre profil devrait ressembler à celui ci-dessous. Ceci est un exemple de configuration de la notation par défaut.

![!cfa-complete](images/cfa-complete.png)

### Remerciements

La plupart de mes informations et connaissances proviennent de :

- rg9400 (Création des formats personnalisés, conseils sur les groupes d'anime et partage de connaissances générales.)

- V01 de SeaDex (Conseils sur les groupes d'anime et partage de connaissances générales.)

- Drazzilb (Conseils sur les groupes d'anime, tests et partage de connaissances générales.)

- [TRaSH](https://trash-guides.info/) (Pour m'avoir permis d'utiliser son site Web pour notre guide et notre partage de connaissances générales.)
