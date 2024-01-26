## Proposer un tutoriel

### Marche à suivre 

#### Forker le repos
git clone https://github.com/projetssd/ssdv2_docs.git

#### Localisation des fichiers à modifier ou créer
Tous les fichiers sont stockés dans le dossier docs, à savoir que le wiki est proposé en bilingue, ce qui signifie que vous devrez déposer un fichier en francais dans le dossier "fr" et un autre traduit, grâce à google translate, dans le dossier "en".

La rédaction des tutos est faite en markdown comme sur le github. Pour agrémenter votre présentation ne pas hésiter à utiliser des admonitions. Ce sont des boites d'avertissement qui bien utilisées permettent d'apporter de la clareté dans la mise en page. 

???+ note
    Exemple de boite

https://docs.framasoft.org/fr/grav/markdown.html

#### Création d'un lien
Pour ce faire, éditer le fichier mkdocs.yml et suivre, en exemple, ce qui est déjà présent

```
  - Radarr:
    - Radarr/radarr-setup-quality-profiles-french-fr.md
    - Radarr/radarr-setup-quality-profiles-anime.md
    - Radarr/radarr-setup-quality-profiles.md
    - Radarr/Radarr-remote-path-mapping.md
    - Radarr/Radarr-recommended-naming-scheme.md
    - Radarr/Radarr-Quality-Settings-File-Size.md
    - Radarr/Radarr-import-custom-formats.md
    - Radarr/Radarr-how-to-update-custom-formats.md
    - Tips:
      - Radarr/Tips/Merge-quality.md
      - Radarr/Tips/Sync-2-radarr-sonarr.md
      - Radarr/Tips/How-to-setup-language-custom-formats.md
  - Sonarr:
    - Sonarr/sonarr-setup-quality-profiles-french-en.md
    - Sonarr/sonarr-setup-quality-profiles-anime.md
    - Sonarr/sonarr-setup-quality-profiles.md
    - Sonarr/Sonarr-remote-path-mapping.md
    - Sonarr/Sonarr-Release-Profile-RegEx-Anime.md .....
```


#### Pull request

Dernière étape, une fois les deux fichiers élaborés (fr et en) vous pouvez proposer un pull request.

![Selection_801](https://github.com/projetssd/ssdv2/assets/7422124/0548afb6-77bc-40a1-83df-8bd17afa0be3)

![Selection_797](https://github.com/projetssd/ssdv2/assets/7422124/b474109f-4b22-475f-8ad0-b8bdeda8c624)


