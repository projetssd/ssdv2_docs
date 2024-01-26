# Comment mettre à jour les formats personnalisés

Ici, je vais essayer d'expliquer comment vous pouvez mettre à jour manuellement les formats personnalisés pour Radarr v3+, avec toutes les modifications du guide ou les modifications qui vous sont fournies à partir d'autres sources, sans perdre la notation de votre profil de qualité.

!!! info "Gardez à l'esprit que les formats personnalisés sont conçus pour affiner votre profil de qualité.<br>En général, la qualité l'emporte sur tout"

## Comment copier/coller le JSON

La méthode manuelle est presque la même que la méthode d'importation au format personnalisé trouvée [ICI](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}

### Dans Radarr

`Paramètres` => `Formats personnalisés`

![cf-settings-cf](images/cf-settings-cf.png)

### Ouvrez le format personnalisé que vous souhaitez mettre à jour

![!Importer pour mettre à jour](images/cf-import-to-update.png)

### Collez le format personnalisé

Dans la zone vide "Format personnalisé JSON" (1), collez simplement le "JSON" que vous avez obtenu de la [Collection de formats personnalisés](/Radarr/Radarr-collection-of-custom-formats/){:target="_blank " rel="noopener noreferrer"} ou fourni à partir d'autres sources suivi du bouton `Importer` (2).

![cf-import-cf](images/cf-import-cf.png)

### Enregistrez le format personnalisé

Après avoir sélectionné le bouton « Importer », vous obtiendrez un écran contenant toutes les variables de format personnalisé correctement remplies. Il ne vous reste plus qu'à cliquer sur le bouton « Enregistrer » et vous avez terminé.

![cf-import-done](images/cf-import-done.png)

!!! avertissement "L'importation pour mettre à jour les formats personnalisés existants remplace le format personnalisé existant, donc toutes les modifications manuelles que vous y avez apportées seront perdues :avertissement:"

### Synchronisation TRaSH

Cela peut également être fait automatiquement avec l'une des applications TRaSH Sync,

plus d'informations peuvent être trouvées [Ici](/Guide-Sync/){:target="_blank" rel="noopener noreferrer"}

