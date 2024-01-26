## Suggest a tutorial 

### Procedure 

#### Fork the 
git clone repository https://github.com/projetssd/ssdv2_docs.git 

#### Location of files to modify or create 
All files are stored in the docs folder, namely that the wiki is offered in bilingual, which means that you will have to place a file in French in the "fr" folder and another translated, using Google translate, in the "en" folder. 

The tutorials are written in markdown as on github. To enhance your presentation, do not hesitate to use admonitions. These are warning boxes which, when used correctly, bring clarity to the layout. 

???+ note 
    Example of box 

https://docs.framasoft.org/fr/grav/markdown.html 

#### Creating a link 
To do this, edit the mkdocs.yml file and follow, as an example, what is already present 

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

Latest step, once the two files have been developed (fr and en) you can propose a pull request. 

![Selection_801](https://github.com/projetssd/ssdv2/assets/7422124/0548afb6-77bc-40a1-83df-8bd17afa0be3)

![Selection_797](https://github.com/projetssd/ssdv2/assets/7422124/b474109f-4b22-475f-8ad0-b8bdeda8c624)