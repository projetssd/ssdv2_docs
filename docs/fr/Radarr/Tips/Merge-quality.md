# Comment fusionner la qualité

La logique actuelle sur la façon dont les téléchargements sont comparés est la suivante : **La qualité l'emporte sur tout** :bangbang:

Dans certains cas, il peut être préférable de ne pas avoir Quality Trump All et de le laisser gérer via les mots préférés/formats personnalisés.

Pour y parvenir, vous devrez fusionner les qualités les unes avec les autres.

## Logique actuelle

Ici, vous verrez la logique actuelle afin de comprendre comment les téléchargements possibles sont comparés.

{! include-markdown "../../../includes/merge-quality/radarr-current-logic.md" !}
<!-- --8<-- "includes/merge-quality/radar-current-logic.md" -->

{! include-markdown "../../../includes/merge-quality/sonarr-current-logic.md" !}
<!-- --8<-- "includes/merge-quality/sonarr-current-logic.md" -->

## Fusionner les qualités

Accédez à votre profil de qualité préféré ou créez-en un nouveau.

`Paramètres` => `Profils`

Dans cet exemple, nous fusionnerons les qualités suivantes :

- Bluray-720p
- Bluray-1080p
- WEBDL/WEBRip-1080p

Pour les fusionner, vous devez cliquer sur Modifier les groupes.

![!Fusionner les qualités](images/merge.gif)

Une fois terminées, les mises à niveau de Sonarr/Radarr seront gérées via les mots préférés/formats personnalisés.

{! include-markdown "../../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->