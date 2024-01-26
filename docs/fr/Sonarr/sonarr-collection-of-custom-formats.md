# Collection de formats personnalisés

Vous trouverez ci-dessous une collection de ce que nous considérons comme les formats personnalisés les plus nécessaires et les plus couramment utilisés.
Ces CF ont été collectés à partir de discussions sur Discord ou créés avec l'aide d'autres personnes.

Un merci spécial à tous ceux qui ont aidé à la création et aux tests de ces formats personnalisés, à mon équipe des guides TRaSH et à la communauté.

Sonarr V4+ introduit les formats personnalisés. Ceux-ci sont beaucoup plus avancés/puissants que les profils de version, bien que cela signifie également qu'un format personnalisé peut nécessiter plus de connaissances pour être configuré ou créé.
Nous avons réalisé 3 guides liés à cela.

- [Comment importer des formats personnalisés](/Sonarr/sonarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"} - Explique comment importer les formats personnalisés.
- [Comment mettre à niveau les formats personnalisés](/Sonarr/sonarr-how-to-update-custom-formats){:target="_blank" rel="noopener noreferrer"} - Explique comment mettre à niveau vos formats personnalisés existants.
- [Comment configurer les profils de qualité](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explique comment tirer le meilleur parti des formats personnalisés et montre quelques détails de ma configuration. Vous pouvez utiliser ces exemples pour avoir une idée de la façon de configurer vos préférences.

!!! conseil

    Il est également recommandé de modifier les paramètres Propers et Repacks dans les « Paramètres » de Sonarr.

    `Media Management` => `File Management` sur `Ne pas préférer` et utilisez le format personnalisé [Repack/Proper](#repackproper).

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    De cette façon, vous vous assurez que la notation et les préférences du format personnalisé seront pleinement utilisées.

--8<-- "includes/support.md"

------

## INDEX

------

| Audio Advanced #1                     | Audio Advanced #2         | Audio Channels               | HDR Formats                       |
| ------------------------------------- | ------------------------- | ---------------------------- | --------------------------------- |
| [TrueHD ATMOS](#truehd-atmos)         | [FLAC](#flac)             | [1.0 Mono](#10-mono)         | [DV HDR10+](#dv-hdr10plus)        |
| [DTS X](#dts-x)                       | [PCM](#pcm)               | [2.0 Stereo](#20-stereo)     | [DV HDR10](#dv-hdr10)             |
| [ATMOS (undefined)](#atmos-undefined) | [DTS-HD HRA](#dts-hd-hra) | [3.0 Sound](#30-sound)       | [DV](#dv)                         |
| [DD+ ATMOS](#ddplus-atmos)            | [AAC](#aac)               | [4.0 Sound](#40-sound)       | [DV HLG](#dv-hlg)                 |
| [TrueHD](#truehd)                     | [DD](#dd)                 | [5.1 Surround](#51-surround) | [DV SDR](#dv-sdr)                 |
| [DTS-HD MA](#dts-hd-ma)               | [MP3](#mp3)               | [6.1 Surround](#61-surround) | [HDR10+](#hdr10plus)              |
| [DD+](#ddplus)                        | [Opus](#opus)             | [7.1 Surround](#71-surround) | [HDR10](#hdr10)                   |
| [DTS-ES](#dts-es)                     |                           | [9.1 Surround](#91-surround) | [HDR](#hdr)                       |
| [DTS](#dts)                           |                           |                              | [HDR (undefined)](#hdr-undefined) |
|                                       |                           |                              | [PQ](#pq)                         |
|                                       |                           |                              | [HLG](#hlg)                       |

------

| Series Versions       | Unwanted                                | HQ Source Groups                        | Streaming Services                          |
| --------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------------- |
| [Hybrid](#hybrid)     | [BR-DISK](#br-disk)                     | [Remux Tier 01](#remux-tier-01)         | [4OD](#4od)                                 |
| [Remaster](#remaster) | [Extras](#extras)                       | [Remux Tier 02](#remux-tier-02)         | [ALL4](#all4)                               |
|                       | [LQ](#lq)                               | [HD Bluray Tier 01](#hd-bluray-tier-01) | [Amazon](#amzn)                             |
|                       | [LQ (Release Title)](#lq-release-title) | [HD Bluray Tier 02](#hd-bluray-tier-02) | [Apple TV+](#atvp)                          |
|                       | [Upscaled](#upscaled)                   | [WEB Tier 01](#web-tier-01)             | [BBC iPlayer (iP)](#ip)                     |
|                       | [x265 (HD)](#x265-hd)                   | [WEB Tier 02](#web-tier-02)             | [CANAL+](#canalplus)                        |
|                       |                                         | [WEB Tier 03](#web-tier-03)             | [Comedy Central](#cc)                       |
|                       |                                         | [WEB Scene](#web-scene)                 | [Crave](#crav)                              |
|                       |                                         |                                         | [DC Universe](#dcu)                         |
|                       |                                         |                                         | [Disney+](#dsnp)                            |
|                       |                                         |                                         | [FOD](#fod)                                 |
|                       |                                         |                                         | [HBO](#hbo)                                 |
|                       |                                         |                                         | [HBO Max](#hmax)                            |
|                       |                                         |                                         | [Hulu](#hulu)                               |
|                       |                                         |                                         | [iTunes](#it)                               |
|                       |                                         |                                         | [Max](#max)                                 |
|                       |                                         |                                         | [NLZiet](#nlz)                              |
|                       |                                         |                                         | [Netflix](#nf)                              |
|                       |                                         |                                         | [OViD](#ovid)                               |
|                       |                                         |                                         | [Paramount+](#pmtp)                         |
|                       |                                         |                                         | [Peacock TV](#pcok)                         |
|                       |                                         |                                         | [Quibi](#qibi)                              |
|                       |                                         |                                         | [RTBF](#rtbf)                               |
|                       |                                         |                                         | [SALTO](#salto)                             |
|                       |                                         |                                         | [SHOWTIME](#sho)                            |
|                       |                                         |                                         | [Stan](#stan)                               |
|                       |                                         |                                         | [TVer](#tver)                               |
|                       |                                         |                                         | [U-NEXT](#u-next)                           |
|                       |                                         |                                         | [Videoland](#vdl)                           |
|                       |                                         |                                         | [YouTube Red](#red)                         |
|                       |                                         |                                         | [UHD Streaming Boost](#uhd-streaming-boost) |
|                       |                                         |                                         | [UHD Streaming Cut](#uhd-streaming-cut)     |

------

| Misc                           | Optional                               | French Audio Version          | French Source Groups                          |
| ------------------------------ | -------------------------------------- | ----------------------------- | --------------------------------------------- |
| [MPEG2](#mpeg2)                | [AV1](#av1)                            | [Multi-French](#multi-french) | [FR Remux Tier 01](#fr-remux-tier-01)         |
| [Multi](#multi)                | [Bad Dual Groups](#bad-dual-groups)    | [Multi-Audio](#multi-audio)   | [FR HD Bluray Tier 01](#fr-hd-bluray-tier-01) |
| [Repack v2](#repack-v2)        | [DV (Disk)](#dv-disk)                  | [French Audio](#french-audio) | [FR WEB Tier 01](#fr-web-tier-01)             |
| [Repack v3](#repack-v3)        | [DV (WEBDL)](#dv-webdl)                | [VFF](#vff)                   | [FR WEB Tier 02](#fr-web-tier-02)             |
| [Repack/Proper](#repackproper) | [DV HDR10+ Boost](#dv-hdr10plus-boost) | [VOF](#vof)                   | [FR WEB Tier 03](#fr-web-tier-03)             |
| [x264](#x264)                  | [HDR10+ Boost](#hdr10plus-boost)       | [VFI](#vfi)                   | [FR Anime Tier 01](#fr-anime-tier-01)         |
| [x265](#x265)                  | [HFR](#hfr)                            | [VF2](#vf2)                   | [FR Anime Tier 02](#fr-anime-tier-02)         |
|                                | [Internal](#internal)                  | [VFQ](#vfq)                   | [FR Anime Tier 03](#fr-anime-tier-03)         |
|                                | [No-RlsGroup](#no-rlsgroup)            | [VOQ](#voq)                   | [FR Anime FanSub](#fr-anime-fansub)           |
|                                | [Obfuscated](#obfuscated)              | [VQ](#vq)                     | [FR Scene Groups](#fr-scene-groups)           |
|                                | [Retags](#retags)                      | [VFB](#vfb)                   | [FR LQ](#fr-lq)                               |
|                                | [Scene](#scene)                        | [VOSTFR](#vostfr)             |                                               |
|                                | [SDR (no WEBDL)](#sdr-no-webdl)        | [FanSUB](#fansub)             |                                               |
|                                | [SDR](#sdr)                            | [FastSUB](#fastsub)           |                                               |
|                                | [Season Packs](#season-pack)           |                               |                                               |
|                                | [VP9](#vp9)                            |                               |                                               |
|                                | [x265 (no HDR/DV)](#x265-no-hdrdv)     |                               |                                               |

------

| Anime Source Groups                                                         | Anime Source Groups                                                   | Anime Misc/Streaming Services | Anime Optional                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------- | ------------------------------------- |
| [Anime BD Tier 01 (Top SeaDex Muxers)](#anime-bd-tier-01-top-seadex-muxers) | [Anime Web Tier 01 (Muxers)](#anime-web-tier-01-muxers)               | [v0](#v0)                     | [Uncensored](#uncensored)             |
| [Anime BD Tier 02 (SeaDex Muxers)](#anime-bd-tier-02-seadex-muxers)         | [Anime Web Tier 02 (Top FanSubs)](#anime-web-tier-02-top-fansubs)     | [v1](#v1)                     | [10bit](#10bit)                       |
| [Anime BD Tier 03 (SeaDex Muxers)](#anime-bd-tier-03-seadex-muxers)         | [Anime Web Tier 03 (Official Subs)](#anime-web-tier-03-official-subs) | [v2](#v2)                     | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 04 (SeaDex Muxers)](#anime-bd-tier-04-seadex-muxers)         | [Anime Web Tier 04 (Official Subs)](#anime-web-tier-04-official-subs) | [v3](#v3)                     | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 05 (Remuxes)](#anime-bd-tier-05-remuxes)                     | [Anime Web Tier 05 (FanSubs)](#anime-web-tier-05-fansubs)             | [v4](#v4)                     |                                       |
| [Anime BD Tier 06 (FanSubs)](#anime-bd-tier-06-fansubs)                     | [Anime Web Tier 06 (FanSubs)](#anime-web-tier-06-fansubs)             | [B-Global](#b-global)         |                                       |
| [Anime BD Tier 07 (P2P/Scene)](#anime-bd-tier-07-p2pscene)                  | [Anime Raws](#anime-raws)                                             | [Bilibili](#bilibili)         |                                       |
| [Anime BD Tier 08 (Mini Encodes)](#anime-bd-tier-08-mini-encodes)           | [Anime LQ Groups](#anime-lq-groups)                                   | [Crunchyroll](#cr)            |                                       |
|                                                                             |                                                                       | [Funimation](#funi)           |                                       |
|                                                                             |                                                                       | [HIDIVE](#hidive)             |                                       |
|                                                                             |                                                                       | [VRV](#vrv)                   |                                       |
|                                                                             |                                                                       | [ABEMA](#abema)               |                                       |
|                                                                             |                                                                       | [ADN](#adn)                   |                                       |
|                                                                             |                                                                       | [WKN](#wkn)                   |                                       |

## Audio Avancé

------

### ATMOS TrueHD

??? question "TrueHD ATMOS - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}

    Dolby Atmos est une technologie de son surround développée par Dolby Laboratories. Il étend les systèmes de son surround existants en ajoutant des canaux de hauteur, permettant aux sons d'être interprétés comme des objets tridimensionnels.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTSX

??? question "DTS:X - [Cliquez pour afficher/masquer]"

    [DTS:X est un codec audio basé sur des objets](https://www.whathifi.com/advice/dtsx-what-it-how-can-you-get-it), qui vise à créer un un son qui « bouge autour de vous comme il le ferait dans la vraie vie ».
    Vous pensez peut-être que cela ressemble beaucoup à Dolby Atmos, et vous avez raison. Mais là où DTS:X diffère, c'est dans la configuration des enceintes requise. Alors que Dolby Atmos vous oblige à ajouter des canaux aériens supplémentaires à votre configuration 5.1 ou 7.1, DTS:X fonctionne avec les configurations d'enceintes surround standard, tout comme celle que vous possédez peut-être déjà à la maison. Il peut prendre en charge jusqu'à 32 emplacements d'enceintes et jusqu'à un système à 11,2 canaux.
    DTS:X, comme les autres formats DTS de qualité supérieure (par exemple DTS-HD MA), est sans perte.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-x.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATMOS (non défini)

??? question "ATMOS (non défini) - [Cliquez pour afficher/masquer]"

    Gère les cas où seul Atmos est spécifié dans le titre mais pas DD+ ou TrueHD (où il n'est pas spécifié s'il est avec ou sans perte)

    !!! note
        Donnez-lui le même score que Lossy Atmos, puis lors de l'importation, il sera modifié en avec ou sans perte en fonction des informations sur les médias.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus ATMOS

<sub>DDPlus = DD+</sub>

??? question "DD+ ATMOS - [Cliquez pour afficher/masquer]"

    Atmos via UHD Blu-ray sera sans perte, ou avec perte via les services de streaming donc dans ce cas, ce sera avec perte + Atmos

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VraiHD

??? question "TrueHD - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}

    Dolby TrueHD est un codec audio multicanal sans perte développé par Dolby Laboratories pour la vidéo domestique, utilisé principalement dans les disques Blu-ray et le matériel compatible.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

??? question "DTS-HD MA - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}

    DTS-HD Master Audio est un codec audio multicanal sans perte développé par DTS en tant qu'extension du codec avec perte DTS Coherent Acoustics (DTS CA ; généralement lui-même appelé simplement DTS). Plutôt que d'être un mécanisme de codage entièrement nouveau, DTS-HD MA encode d'abord un maître audio en DTS avec perte, puis stocke un flux simultané de données supplémentaires représentant tout ce que l'encodeur DTS a rejeté. Cela donne au DTS-HD MA un « noyau » avec perte capable d'être lu par des appareils qui ne peuvent pas décoder l'audio sans perte plus complexe. L'application principale du DTS-HD MA est le stockage et la lecture audio pour les supports Blu-ray Disc.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###FLAC

??? question "FLAC - [Cliquez pour afficher/masquer]"

    FLAC signifie Free Lossless Audio Codec, un format audio similaire au MP3, mais sans perte, ce qui signifie que l'audio est compressé en FLAC sans aucune perte de qualité. Ceci est similaire au fonctionnement de Zip, sauf qu'avec FLAC, vous obtiendrez une bien meilleure compression car il est spécialement conçu pour l'audio.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

??? question "PCM - [Cliquez pour afficher/masquer]"

    PCM est la méthode d'encodage généralement utilisée pour l'audio numérique non compressé.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

??? question "DTS-HD HRA - [Cliquez pour afficher/masquer]"

    [Livre blanc technique](https://www.opusproductions.com/pdfs/DTS_HD_WhitePaper.pdf){:target="_blank" rel="noopener noreferrer"}

    | Codecs | Pages | Paragraphe |
    | ---------- | ------ | --------- |
    | DTS-HD MA | Page 6 | 5.1.1 |
    | DTS-HD HRA | Page 7 | 5.1.2 |

    DTS-HD HRA est la version avec perte de DTS-HD MA.

    | Codecs | DTS-HRA | DTS-MA |
    | ---------- | ---------------- | ----------------- |
    | Avec/sans perte | Avec perte | Sans perte |
    | Débit de données | 1,5 - 6,0 Mbit/s | VBR-24,5 Mbit/s |
    | Chaînes | Jusqu'à 7,1 ch | Jusqu'à 7,1 ch |
    | Fréquence d'échantillonnage. | 96 kHz | 192 kHz |
    | Résolution | - | Jusqu'à 24 bits |

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-hra.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus

<sub>Dolby Digital Plus = DD+ = DDPlus</sub>

??? question "DD+ - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Dolby_Digital_Plus){:target="_blank" rel="noopener noreferrer"}

    Dolby Digital Plus, également connu sous le nom de Enhanced AC-3 (et communément abrégé en DD+ ou E-AC-3, ou EC-3) est un système de compression audio numérique développé par Dolby Labs pour le transport et le stockage de l'audio numérique multicanal. C'est le successeur du Dolby Digital (AC-3).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

??? question "DTS-ES - [Cliquez pour afficher/masquer]"

    DTS-ES (DTS Extended Surround) comprend deux variantes, DTS-ES Discrete 6.1 et DTS-ES Matrix 5.1, selon la manière dont le son a été initialement masterisé et stocké.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

<sub>DTS = DTS de base</sub>

??? question "DTS - [Cliquez pour afficher/masquer]"
    Espace réservé pour la description

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### CAA

??? question "AAC - [Cliquez pour afficher/masquer]"

    Codage audio avancé

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
    Advanced Audio Coding (AAC) est une norme de codage audio pour la compression audio numérique avec perte. Conçu pour succéder au format MP3, l'AAC permet généralement d'obtenir une qualité sonore supérieure à celle du MP3 pour le même débit binaire.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/aac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DD

<sub>(Basique) Dolby Digital = DD</sub>

??? question "DD - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Dolby_Digital){:target="_blank" rel="noopener noreferrer"}

    Dolby Digital, également connu sous le nom de Dolby AC-3, la compression audio est avec perte.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###MP3

??? question "MP3 - [Cliquez pour afficher/masquer]"
    Espace réservé pour la description

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Opus

??? question "Opus - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}

    Opus est un format de codage audio avec perte développé par la Fondation Xiph.Org et standardisé par l'Internet Engineering Task Force, conçu pour coder efficacement la parole et l'audio général dans un format unique, tout en restant suffisamment faible pour une communication interactive en temps réel et une faible latence. - une complexité suffisante pour les processeurs embarqués bas de gamme. Opus remplace Vorbis et Speex pour de nouvelles applications, et plusieurs tests d'écoute aveugle l'ont classé comme étant de meilleure qualité que tout autre format audio standard à n'importe quel débit binaire donné jusqu'à ce que la transparence soit atteinte, y compris MP3, AAC , et HE-AAC

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Canaux audio

------

### 1.0Mono

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stéréo

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Son 3.0

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Son 4.0

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Surround 5.1

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Surround 6.1

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Surround 7.1

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Ambiance 9.1

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/91-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Formats HDR

------

### DV HDR10Plus

<sub>DV = DoVi = Dolby Vision</sub><br>
<sub>HDR10+ = HDR10P = HDR10Plus</sub>

??? question "DV HDR10+ - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/dv-hdr10plus.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV HDR10

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV HDR10 - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/dv-hdr10.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DVD

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV - [Cliquez pour afficher/masquer]"

    --8<-- "includes/cf-descriptions/dv.md"

<! -- la raison pour laquelle nous n'avons pas utilisé ici `include-markdown` est que tous les en-têtes lors de l'utilisation de `include-markdown` rechercheront dans `/includes` et non dans le fichier markdown actuel, dans ce cas le pointeur vers ` #dv-webdl` dans `includes/dv.md`-->

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV HLG

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV HLG - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/dv-hlg.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV-SDR

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV SDR - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/dv-sdr.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10Plus

<sub>HDR10+ = HDR10P = HDR10Plus</sub>

??? question "HDR10+ - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/hdr10plus.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###HDR10

<sub>HDR10</sub>

??? question "HDR10 - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/hdr10.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###HDR

<sub>HDR</sub>

??? question "HDR - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/hdr.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (non défini)

??? question "HDR (non défini) - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/hdr-undefined.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PQ

<sub>PQ = PQ10</sub>

??? question "PQ - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/pq.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HLG

<sub>HLG = HLG10</sub>

??? question "HLG - [Cliquez pour afficher/masquer]"

    {! include-markdown "../../includes/cf-descriptions/hlg.md" !}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Versions de la série

------

### Hybride

??? question "Hybride - [Cliquez pour afficher/masquer]"

    Une version hybride signifie toute combinaison de sources (vidéo + audio) et non un encodage direct d'une seule source. En général, vous pouvez être sûr que tout hybride créé constitue la version de la meilleure qualité d’un titre particulier.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hybrid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remasterisé

??? question "Remaster - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}

    Pour le terme logiciel, voir Remasterisation de logiciels.
    Le remaster (également remasterisation numérique et remasterisé numériquement) fait référence à la modification de la qualité du son ou de l'image, ou des deux, d'enregistrements précédemment créés, qu'ils soient audiophoniques, cinématographiques ou vidéographiques.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
     [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Indésirable

------

### BR-DISQUE

??? question "BR-DISK - [Cliquez pour afficher/masquer]"

    Il s'agit d'un format personnalisé permettant à Sonarr de reconnaître et d'ignorer BR-DISK (structure des dossiers ISO et Blu-ray) en plus de la qualité BR-DISK standard.

    Vous devrez ajouter les éléments suivants en tant que nouveau format personnalisé et, une fois créé, ajuster la note dans votre profil de qualité (`Setting` => `Profiles`) à `-10000`.

    !!! note

        En fonction de votre schéma de renommage, Sonarr pourrait potentiellement faire correspondre les fichiers renommés APRÈS qu'ils aient été téléchargés et importés en tant que « BR-DISK »,
        Ce n'est qu'un désagrément cosmétique jusqu'à ce que nous trouvions une autre façon de résoudre ce problème.
        Étant donné que ce format personnalisé est utilisé pour exclure le téléchargement de BR-DISK, il se comporte toujours comme prévu.

        Raisons potentielles pour lesquelles cela pourrait se produire :

        - La faute à la dénomination souvent mal utilisée des encodes x265.
        - Sonarr v3/v4 utilise des formats personnalisés dynamiques.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ

<sub>Communiqués de mauvaise qualité = LQ</sub>

??? question "LQ - [Cliquez pour afficher/masquer]"

    Une collection de groupes connus de faible qualité qui sont souvent bannis des meilleurs trackers en raison de leur manque de versions de qualité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ (titre de la version)

<sub>Communiqués de mauvaise qualité = LQ</sub>

??? question "LQ (titre de la version) - [Cliquez pour afficher/masquer]"

    Ensemble de termes présents dans les titres des versions de faible qualité qui ne sont pas capturés à l'aide d'un nom de groupe de versions.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq-release-title.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Mise à l'échelle

??? question "Mise à niveau - [Cliquez pour afficher/masquer]"

    Ce format personnalisé est utilisé pour empêcher Sonarr de récupérer les versions mises à l'échelle.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/upscaled.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (HD)

<sub>720/1080p non x265 = x265 (720/1080p) = x265 (HD)</sub>

??? question "x265 (HD) - [Cliquez pour afficher/masquer]"

    Ceci bloque/ignore les versions 720/1080p(HD) codées en x265.

    Dans votre profil de qualité, utilisez le score suivant pour ce format personnalisé : `{{ sonarr['cf']['x265-hd']['trash_scores']['default'] }}`

    !!! échec ""
        --8<-- "includes/docker/x265.md"

            !!! Danger "Ne l'utilisez pas avec [{{ sonarr['cf']['x265-no-hdrdv']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/# x265-no-hdrdv), n'incluez qu'un seul d'entre eux :avertissement:"

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-hd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Suppléments

??? question "Extras - [Cliquez pour afficher/masquer]"

    Ceci bloque/ignore les extras (images bonus, extraits, etc.)

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/extras.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Divers

------

### Reconditionner/correctement

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack v2

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack v3

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x264

??? question "x264 - [Cliquez pour afficher/masquer]"

    x264 est une *bibliothèque de logiciels gratuits* et une *application* permettant d'encoder des flux vidéo au format [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target=" _blank" rel="noopener noreferrer"} format de compression et est publié selon les termes de la [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target ="_blank" rel="noopener noreferrer"}.

    Si vous souhaitez une compatibilité maximale et bénéficier d’une bien meilleure prise en charge de la lecture directe, utilisez x264 pour 720p/1080p.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x264.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###x265

??? question "x265 - [Cliquez pour afficher/masquer]"

    x265 est une *bibliothèque de logiciels gratuits* et une *application* permettant d'encoder des flux vidéo au format [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target=" _blank" rel="noopener noreferrer"} format de compression et est publié selon les termes de la [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target ="_blank" rel="noopener noreferrer"}.

    !!! échec ""
        N'oubliez pas de lire ce qui suit [Microsized & Wrong Source](#microsized-wrong-source)

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###MPEG2

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Facultatif

------

### Mauvais groupes doubles

??? question "Mauvais groupes doubles - [Cliquez pour afficher/masquer]"
    Ces groupes prennent la version originale et ajoutent leur propre langue (par exemple le portugais) comme piste audio principale (AAC 2.0). Après avoir renommé et FFprobe, le fichier multimédia sera reconnu comme audio AAC portugais. Il est courant d'ajouter le meilleur son comme première piste.
    De plus, ils traduisent/renomment souvent même le nom de la version en portugais.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bad-dual-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV (WEBDL)

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV (WEBDL) - [Cliquez pour afficher/masquer]"
    Il s'agit d'un format personnalisé spécial qui bloque les WEBDL **avec** Dolby Vision mais **sans** solution de secours HDR10.

    Vous devrez ajouter les éléments suivants en tant que nouveau format personnalisé et, une fois créé, ajuster la note dans votre profil de qualité (`Setting` => `Profiles`) à `-10000`.

    Ce format personnalisé fonctionne avec le format personnalisé [DV](#dv) normal que vous utiliseriez pour préférer Dolby Vision.

    La plupart des WEBDL des services de streaming ne disposent pas de solution de repli vers HDR10. Ce qui peut résulter pendant la lecture, ce sont des problèmes de couleurs étranges (généralement une teinte verte) lorsque vous essayez de le lire sur une configuration non compatible Dolby Vision.

    Les remux et Bluray ont un recours au HDR10.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Boost HDR10Plus

??? question "HDR10+ Boost - [Cliquez pour afficher/masquer]"

    Facultatif. Utilisez celui-ci uniquement si vous possédez un téléviseur (Samsung) prenant en charge HDR10+ et que vous n'avez pas de configuration prenant en charge le DV ou si vous préférez HDR10+.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Boost DV HDR10Plus

??? question "DV HDR10+ Boost - [Cliquez pour afficher/masquer]"

    Facultatif : utilisez celui-ci si vous souhaitez passer du DV HDR10 au DV HDR10+ pour prendre en charge le meilleur des deux mondes.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10plus-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Sans-RlsGroup

??? question "No-RlsGroup - [Cliquez pour afficher/masquer]"

    Certains indexeurs suppriment le groupe de versions, ce qui pourrait permettre aux groupes LQ d'obtenir un score plus élevé.
    Par exemple, de nombreuses versions d'EVO finissent par être dépourvues du nom du groupe et apparaissent donc comme des "mises à niveau" et finissent par obtenir un score décent si d'autres éléments correspondent.

    !!! avertissement

        Si vous n'utilisez pas de noms de fichiers corrects (par exemple en n'ajoutant pas de groupes de versions), n'ajoutez pas ce format personnalisé, sauf si vous souhaitez les mettre à niveau.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Obscurci

??? question "Obscurci - [Cliquez pour afficher/masquer]"

    Facultatif (utilisez-les uniquement si vous n'aimez pas les versions renommées)

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Retags

??? question "Retags - [Cliquez pour afficher/masquer]"

    Facultatif (utilisez-les uniquement si vous n'aimez pas les versions retaggées)

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/retags.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Scène

??? question "Scène - [Cliquez pour afficher/masquer]"

    Ce format personnalisé tentera de reconnaître ce que l'on appelle les « versions de scène ». Selon vos préférences, vous pouvez lui attribuer un score négatif « -10 000 », un score positif, ou simplement ignorer complètement son ajout.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Pack de saison

??? question "Season Pack - [Cliquez pour afficher/masquer]"

    Ce format personnalisé peut être utilisé pour préférer ou exclure les packs de saison

    - Donnez-lui une note de « 10 » si vous préférez un pack saisonnier.
    - Donnez-lui un score de « -10000 » si vous préférez ne pas télécharger les packs de saison.
    - Les packs de saison `/\bS\d+\b(?!E\d+\b)/i` sont préférés : cependant, étant donné que le nom du dossier est ignoré, l'erreur/avertissement/problème se produit car les noms de fichiers ne seraient pas une saison paquet.
    - Gardez à l'esprit que c'est la seule façon de préférer les packs saisonniers. Si vous avez des mots préférés, en raison d'un bug de longue date => Les mots préférés annulent les préférences du pack saisonnier [Sonarr/Sonarr#3562](https://github.com/Sonarr/Sonarr/issues/3562){:target="_blank " rel="noopener noreferrer"}

    !!! danger "AVERTISSEMENT"
        - Ce format personnalisé pourrait entraîner une boucle de téléchargement :bangbang:
        - Cela mettra également à niveau vos épisodes uniques déjà téléchargés :bangbang:

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/season-pack.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (pas de HDR/DV)

??? question "x265 (pas de HDR/DV) - [Cliquez pour afficher/masquer]"

  Cela bloque la plupart des versions 720/1080p (HD) codées en x265.

    **Mais cela autorisera les versions 720/1080p x265 si elles ont HDR et/ou DV**

    *Étant donné que certaines versions NF ne seront pas publiées en 4K, mais vous souhaitez avoir des versions DV/HDR.*

    Dans votre profil de qualité, utilisez le score suivant pour ce format personnalisé : `{{ sonarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}`

    !!! Danger "Ne l'utilisez pas avec [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265- hd), n'incluez qu'un seul d'entre eux :avertissement:"

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-no-hdrdv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###AV1

??? question "AV1 - [Cliquez pour afficher/masquer]"

    - Il s'agit d'un nouveau codec et vous avez besoin d'appareils modernes qui le prennent en charge.
    - Nous avons également eu des rapports faisant état de problèmes de lecture/transcodage.
    - Aucun groupe principal ne l'utilise (encore).
    - Il est préférable d'ignorer ce nouveau codec pour éviter des problèmes de compatibilité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/av1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###VP9

??? question "VP9 - [Cliquez pour afficher/masquer]"

    - Il s'agit d'un nouveau codec et vous avez besoin d'appareils modernes qui le prennent en charge.
    - Nous avons également eu des rapports faisant état de problèmes de lecture/transcodage.
    - Aucun groupe principal ne l'utilise (encore).
    - Il est préférable d'ignorer ce nouveau codec pour éviter des problèmes de compatibilité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vp9.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Interne

??? question "Interne - [Cliquez pour afficher/masquer]"

    - Pour ceux qui préfèrent les versions de scène, vous souhaiterez peut-être améliorer les composants internes, car ils ont généralement des paramètres plus élevés qui peuvent ne pas être conformes aux règles.
    - Dans de rares cas, le P2P utilise également INTERNE.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/internal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

??? question "SDR - [Cliquez pour afficher/masquer]"

    - Cela aidera à éviter de récupérer des versions UHD/4k sans formats HDR.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SDR (pas de WEBDL)

??? question "SDR (pas de WEBDL) - [Cliquez pour afficher/masquer]"

    - Cela empêchera la récupération des versions encodées UHD/4k Remux et Bluray sans formats HDR - c'est-à-dire que les versions WEB SDR seront toujours autorisées. Les versions WEB 4K SDR peuvent être plus belles que la version 1080p, grâce à des débits binaires améliorés.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sdr-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV (Disque)

??? question "DV (Disque) - [Cliquez pour afficher/masquer]"

    - Cela augmentera le score des versions Dolby Vision en utilisant la couche Dolby Vision originale de pleine qualité de la version disque pour remplacer l'ancienne version WEBDL HYBRID.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HFR

??? question "HFR - [Cliquez pour afficher/masquer]"

    - Cela augmentera le score des versions HFR. HFR signifie High Frame Rate et fait référence à un format vidéo qui utilise un nombre d'images par seconde plus élevé que la vidéo traditionnelle, ce qui donne un mouvement plus fluide et plus détaillé.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Groupes sources du QG

------

### Remux niveau 01

??? question "Remux Tier 01 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - Se sont imposés comme fournissant constamment des versions de haute qualité.
    - Produisez des remux à partir de plusieurs sources (disques) et combinez-les pour produire le meilleur résultat final.
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remux niveau 02

??? question "Remux Tier 02 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - N'utilisez qu'une seule source (surnommée poétiquement « les merveilles d'un disque »).
    - Utilisez une méthode entièrement automatisée sans double vérification.
    - Ne vérifiez/n'examinez pas leurs versions avant de les télécharger.
    - Je n'ai pas publié grand-chose. (encore)
    - Vous avez pris votre retraite et n'avez pas la meilleure qualité selon les normes actuelles
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

### HD Blu-ray niveau 01

??? question "HD Bluray Tier 01 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - Se sont imposés comme fournissant constamment des versions de haute qualité.
    - Utilisez les remux comme source sans les micro-dimensionner.
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Blu-ray HD niveau 02

??? question "HD Bluray Tier 02 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - Utilisez les remux comme source sans les micro-dimensionner.
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

### WEB Niveau 01

??? question "WEB Tier 01 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - Se sont imposés comme fournissant constamment des versions de haute qualité.
    - Créer des hybrides.
    - Inscrivez-vous à la liste des gentlemen sur un certain tracker privé.
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Niveau 02

??? question "WEB Tier 02 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - Inscrivez-vous à la liste des gentlemen sur un certain tracker privé.
    - Je n'ai fait que quelques versions
    - Ne sont pas sur la liste mais ont quelques sorties à leur nom
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Niveau 03

??? question "WEB Tier 03 - [Cliquez pour afficher/masquer]"

    Des groupes qui :

    - Inscrivez-vous à la liste des gentlemen sur un certain tracker privé.
    - Je n'ai fait que quelques versions
    - Ne sont pas sur la liste mais ont quelques sorties à leur nom
    - Suivez les [Consignes générales de contribution](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Scène WEB

??? question "Scène WEB - [Cliquez pour afficher/masquer]"

    L'un des rares groupes de scène à avoir sorti des sorties de qualité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Services de diffusion en continu

------

###AMZN

<sub>Amazon</sub>

??? question "Amazon - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Amazon_Prime_Video){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/amzn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATVP

<sub>Apple TV+</sub>

??? question "Apple TV+ - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Apple_TV%2B){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atvp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DCU

<sub>Univers DC</sub>

??? question "DC Universe - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/DC_Universe_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dcu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###DSNP

<sub>Disney+</sub>

??? question "Disney+ - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Disney%2B){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dsnp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HMAX

<sub>HBO Max</sub>

??? question "HBO Max - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/HBO_Max){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hmax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HBO

<sub>HBO</sub>

??? question "HBO - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/HBO){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hbo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###Maximum

<sub>Maximum</sub>

??? question "Max - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Max_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/max.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Hulu

<sub>Hulu</sub>

??? question "Hulu - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Hulu){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IP

<sub>BBC iPlayer</sub>

??? question "BBC iPlayer - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/BBC_iPlayer){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ip.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### NLZ

<sub>NLZiet</sub>

??? question "NLZiet - [Cliquez pour afficher/masquer]"

    NLZIET est le service en ligne des radiodiffuseurs néerlandais qui propose une télévision en continu, sans publicité. Le service de streaming apporte le meilleur de toutes les chaînes directement sur votre appareil préféré et vous permet de voir votre contenu télévisé préféré en haute qualité sur toutes les plateformes disponibles ; N'importe quand et n'importe où.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nlz.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### NF

<sub>Netflix</sub>

??? question "Netflix - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Netflix){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###PMTP

<sub>Paramount+</sub>

??? question "Paramount+ - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Paramount%2B){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pmtp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###PCOK

<sub>Paon TV</sub>

??? question "Peacock TV - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Peacock_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcok.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Qibi

<sub>Quibi</sub>

??? question "Quibi - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Quibi){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/qibi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SHO

<sub>SHOWTIME</sub>

??? question "SHOWTIME - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Showtime_(TV_network)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sho.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VDL

<sub>Vidéoland</sub>

??? question "Videoland - [Cliquez pour afficher/masquer]"

    Videoland est un fournisseur de services en ligne OTT néerlandais appartenant à RTL Nederland. À l’origine, il s’agissait d’une chaîne de magasins de location de vidéos. Son principal concurrent est Netflix.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### STAN

<sub>Stan</sub>

??? question "STAN - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Stan_(service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/stan.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ROUGE

<sub>ROUGE = Youtube Rouge = Youtube Premium</sub>

??? question "Youtube Red - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/YouTube_Premium){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/red.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IL

<sub>iT = iTunes</sub>

??? question "iTunes - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/ITunes){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/it.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###CANALPlus

<sub>CANALPlus = CANAL+/MonCANAL</sub>

??? question "Canal+ - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Canal%2B){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-canalplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SALTO

<sub>SALTO = SⱯLTO</sub>

??? question "SⱯLTO - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Salto_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-salto.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###RTBF

<sub>RTBF = Radio-télévision belge de la Communauté française (Radio Télévision Belge Francophone)</sub>

??? question "RTBF - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/RTBF){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-rtbf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### CC

<sub>CC = Comedy Central</sub>

??? question "CC - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Comedy_Central){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Crav

<sub>Envie</sub>

??? question "CRAVE - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Crave_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/crav.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### OViD

<sub>OViD</sub>

??? question "OViD - [Cliquez pour afficher/masquer]"

    [Site Web OViD](https://search.ovid.tv/other/about){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ovid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FOD

<sub>FOD</sub>

??? question "FOD - [Cliquez pour afficher/masquer]"

    - Télévision Fuji à la demande
    - [De Wikipédia, l'encyclopédie libre](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%B8%E3%83%86%E3%83%AC%E3%83 %93%E3%82%AA%E3%83%B3%E3%83%87%E3%83%9E%E3%83%B3%E3%83%89){:target="_blank" rel="noopener aucun référent"}
    - [Site Web FOD](https://fod-sp.fujitv.co.jp){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fod.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Téléviseur

<sub>TVeur</sub>

??? question "TVer - [Cliquez pour afficher/masquer]"

    - [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/TVer_(streaming_service)){:target="_blank" rel="noopener noreferrer"}
    - [Site Web TVer](https://tver.jp){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/tver.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### U-SUIVANT

<sub>U-NEXT</sub>

??? question "U-NEXT - [Cliquez pour afficher/masquer]"

    - [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/U-Next){:target="_blank" rel="noopener noreferrer"}
    - [Site Web U-NEXT](https://video.unext.jp){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/u-next.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TOUS4

<sub>TOUS4</sub>

??? question "ALL4 - [Cliquez pour afficher/masquer]"

    - [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Channel_4_(VoD_service)){:target="_blank" rel="noopener noreferrer"}
    - ALL4 est l'ancien nom du service britannique Channel4 VOD. Les versions sont généralement identifiées par « ALL4 » ou « 4OD », et non par « Channel4 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/all4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4OD

<sub> 4OD</sub>

??? question "4OD - [Cliquez pour afficher/masquer]"

    - [De Wikipédia, l'encyclopédie gratuite](https://en.wikipedia.org/wiki/Channel_4_(VoD_service)){:target="_blank" rel="noopener noreferrer"}
    - 4OD est l'ancien nom du service britannique Channel4 VOD. Les versions sont généralement identifiées par « ALL4 » ou « 4OD », et non par « Channel4 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/4od.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Amélioration du streaming UHD

??? question "UHD Streaming Boost - [Cliquez pour afficher/masquer]"

    Certains services de streaming proposent des versions UHD qui sont généralement meilleures que leurs homologues HD. Le format personnalisé UHD Streaming Boost augmente les scores de ces services de streaming de manière appropriée pour les versions UHD. Utilisez-le en conjonction avec les formats personnalisés du service de streaming habituel.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uhd-streaming-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Coupe du streaming UHD

??? question "UHD Streaming Cut - [Cliquez pour afficher/masquer]"

    Certains services de streaming proposent des versions UHD généralement pires que leurs homologues HD. Le format personnalisé UHD Streaming Cut diminue les scores de ces services de streaming de manière appropriée pour les versions UHD. Utilisez-le en conjonction avec les formats personnalisés du service de streaming habituel.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uhd-streaming-cut.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Animés

------

### Anime BD Tier 01 (meilleurs multiplexeurs SeaDex)

??? question "Anime BD Tier 01 (Meilleurs multiplexeurs SeaDex) - [Cliquez pour afficher/masquer]"
    Groupes qui font les meilleures versions selon SeaDex. Ils sont plus cohérents et surpassent les autres

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-01-top-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 02 (Muxeurs SeaDex)

??? question "Anime BD Tier 02 (SeaDex Muxers) - [Cliquez pour afficher/masquer]"
    Groupes qui font les meilleures versions selon SeaDex. Ils sont plus cohérents et surpassent les autres

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-02-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 03 (Muxeurs SeaDex)

??? question "Anime BD Tier 03 (SeaDex Muxers) - [Cliquez pour afficher/masquer]"
    Groupes qui font les meilleures versions selon SeaDex. Ils sont plus cohérents et surpassent les autres

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-03-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 04 (Muxeurs SeaDex)

??? question "Anime BD Tier 04 (SeaDex Muxers) - [Cliquez pour afficher/masquer]"
    Groupes qui font les meilleures versions selon SeaDex. Ils sont plus cohérents et surpassent les autres

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-04-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Niveau 05 (Remux)

??? question "Anime BD Tier 05 (Remuxes) - [Cliquez pour afficher/masquer]"
    Des groupes cohérents et qui font des Remux

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-05-remuxes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD niveau 06 (FanSubs)

??? question "Anime BD Tier 06 (FanSubs) - [Cliquez pour afficher/masquer]"
    Groupes FanSub cohérents

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Niveau 07 (P2P/Scène)

??? question "Anime BD Tier 07 (P2P/Scène) - [Cliquez pour afficher/masquer]"
    Groupes P2P et Scene Anime connus

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-07-p2pscene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD niveau 08 (mini-encodages)

??? question "Anime BD Tier 08 (Mini Encodes) - [Cliquez pour afficher/masquer]"
    Connaître les groupes qui effectuent des mini-encodages

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-08-mini-encodes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 01 (Muxeurs)

??? question "Anime Web Tier 01 (Muxers) - [Cliquez pour afficher/masquer]"
    Groupes qui font les meilleures versions selon SeaDex. Ils sont plus cohérents et surpassent les autres

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-01-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Niveau 02 (Meilleurs FanSubs)

??? question "Anime Web Tier 02 (Top FanSubs) - [Cliquez pour afficher/masquer]"
    Groupes qui font les meilleures versions selon SeaDex. Ils sont plus cohérents et surpassent les autres

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-02-top-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 03 (Sous-marins officiels)

??? question "Anime Web Tier 03 (Sous-marins officiels) - [Cliquez pour afficher/masquer]"
    Sous-groupes officiels qui ont tendance à être plus cohérents et à sortir rapidement

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-03-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 04 (Sous-marins officiels)

??? question "Anime Web Tier 04 (Sous-marins officiels) - [Cliquez pour afficher/masquer]"
    Sous-groupes officiels

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-04-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web niveau 05 (FanSubs)

??? question "Anime Web Tier 05 (FanSubs) - [Cliquez pour afficher/masquer]"
    Groupes FanSub cohérents

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-05-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web niveau 06 (FanSubs)

??? question "Anime Web Tier 06 (FanSubs) - [Cliquez pour afficher/masquer]"
    Groupes FanSub cohérents

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime bruts

??? question "Anime Raws - [Cliquez pour afficher/masquer]"
    Une collection de groupes connus qui publient des bruts

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-raws.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Groupes Anime LQ

??? question "Groupes Anime LQ - [Cliquez pour afficher/masquer]"
    Une collection de groupes connus de faible qualité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-lq-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Non censuré

??? question "Non censuré - [Cliquez pour afficher/masquer]"
    Ce CF couvre les sorties non censurées

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uncensored.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###v0

??? question "v0 - [Cliquez pour afficher/masquer]"
    CF couvrira les versions nommées avec v0 dont nous ne voulons pas

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v0.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###v1

??? question "v1 - [Cliquez pour afficher/masquer]"
    CF pour couvrir les versions v1

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###v2

??? question "v2 - [Cliquez pour afficher/masquer]"
    CF pour couvrir les versions v2

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###v3

??? question "v3 - [Cliquez pour afficher/masquer]"
    CF pour couvrir les versions v3

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v4

??? question "v4 - [Cliquez pour afficher/masquer]"
    CF pour couvrir les versions v4

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### B-Global

??? question "B-Global - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/Bilibili){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bglobal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Bilibili

??? question "Bilibili - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/Bilibili){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bilibili.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### cr

<sub>Crunchyroll</sub>

??? question "Crunchyroll - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/Crunchyroll){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### amusant

<sub>Funimation</sub>

??? question "Funimation - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/Funimation){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/funi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### CACHER

??? question "HIDIVE - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/HIDIVE){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hidive.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###VRV

??? question "VRV - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/VRV_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vrv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###ABÉMA

??? question "ABMEA - [Cliquez pour afficher/masquer]"
    [De Wikipédia, l'encyclopédie gratuite](https://www.wikiwand.com/en/Abema){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/abema.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ADN

<sub>ADN = Réseau Numérique d'Animation</sub>

??? question "ADN - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie gratuite](https://fr.wikipedia.org/wiki/Animation_Digital_Network){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-adn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WKN

<sub>WKN = Wakanim</sub>

??? question "WKN - [Cliquez pour afficher/masquer]"

    [De Wikipédia, l'encyclopédie libre](https://fr.wikipedia.org/wiki/Wakanim){:target="_blank" rel="noopener noreferrer"}

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-wkn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 10 bits

??? question "10 bits - [Cliquez pour afficher/masquer]"
    Ce CF couvre les versions 10 bits

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime double audio

??? question "Anime Dual Audio - [Cliquez pour afficher/masquer]"
    Ce CF couvre les versions dotées de Dual Audio

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Doublage uniquement

??? question "Dubs uniquement - [Cliquez pour afficher/masquer]"
    Ce CF couvre les versions qui ne contiennent que des doublages

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dubs-only.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Version audio française

------

### Multi-Français

??? question "Multi-Français - [Cliquez pour afficher/masquer]"

    Reconnaissez les films qui incluent l’original et l’audio français. Fonctionne uniquement après l'importation car il a besoin du résultat de FFprobe pour obtenir quels fichiers audio sont présents. Renomme la version pour conserver la reconnaissance de « Multi » par le format personnalisé [Multi-Audio](#multi-audio).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi-Audio

??? question "Multi-Audio - [Cliquez pour afficher/masquer]"

    Un format personnalisé [Multi](#multi) légèrement modifié qui reconnaît VF et VO dans le nom.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Audio français

??? question "Audio français - [Cliquez pour afficher/masquer]"

    Cela reconnaîtra tous les types d’audio français.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFF

??? question "VFF - [Cliquez pour afficher/masquer]"

    Version française complète (doublage réalisé en France) et version française (normalement équivalente à VFQ).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vff.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOF

??? question "VOF - [Cliquez pour afficher/masquer]"

    Version originale française.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vof.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

###VFI

??? question "VFI - [Cliquez pour afficher/masquer]"

    Version française internationale.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VF2

??? question "VF2 - [Cliquez pour afficher/masquer]"

    VF[1-9] ou FR[1-9] indique le nombre de doublages présents (normalement VF2 étant VFF et VFQ).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vf2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFQ

??? question "VFQ - [Cliquez pour afficher/masquer]"

    Version française canadienne.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOQ

??? question "VOQ - [Cliquez pour afficher/masquer]"

    Version originale québécoise.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-voq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VQ

??? question "VQ - [Cliquez pour afficher/masquer]"

    Version québécoise (fort accent québécois, ex : film Les Simpsons).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFB

??? question "VFB - [Cliquez pour afficher/masquer]"

    Version française belge.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfb.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOSTFR

??? question "VOSTFR - [Cliquez pour afficher/masquer]"

    Indique la bande sonore en langue originale, sous-titrée en français. Il convient de noter que SUBFRENCH est inclus dans ce format personnalisé. Cependant, SUB signifie souvent que le sous-titre a été intégré à l'image (codé en dur). Les versions françaises ont tendance à mélanger les deux, ce qui conduit certains VOSTFR à être étiquetés SUBFRENCH et SUBFRENCH à VOSTFR.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vostfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FanSUB

??? question "FanSUB - [Cliquez pour afficher/masquer]"

    Action de sous-titrer une vidéo à des fins personnelles et non professionnelles. La qualité des FanSUB peut varier énormément (précision de la traduction, erreurs, etc.) et peut conduire à ce que l'on appelle des FastSUB.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FastSUB

??? question "FastSUB - [Cliquez pour afficher/masquer]"

    FanSUB, mais réalisé le plus rapidement possible, au détriment de la qualité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fastsub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Groupes sources du siège français

------

### FR Remux Niveau 01

??? question "Remux Tier 01 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Des groupes qui produisent des remux à partir de plusieurs sources (disques) et les combinent pour produire le meilleur résultat final.
    - Groupes effectuant activement des remux à partir d'une seule source (disques).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR HD Bluray Niveau 01

??? question "FR HD Bluray Tier 01 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Des groupes qui créent des encodages à partir de remux sans les micro-dimensionner.
    - Les groupes qui ajoutent la meilleure piste audio française à une version anglaise du Tier 01 ou 02.
    - Groupes qui ont un minimum de bonnes versions (meilleur encodage de sa catégorie 1080p et inférieur).

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Niveau 01

??? question "FR WEB Tier 01 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Groupes qui obtiennent leurs sorties directement de la source.
    - Regroupe cette source et ajoute la piste audio française de la source à une version anglaise du niveau 01 ou 02.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Niveau 02

??? question "FR WEB Tier 02 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Des groupes qui obtiennent leurs sorties directement de la source mais qui ne sont pas aussi actifs.
    - Regroupe cette source et ajoute la piste audio française de la source à une version anglaise.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Niveau 03

??? question "FR WEB Tier 03 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Des groupes qui n'ont pas beaucoup sorti ou qui ne sont pas bien reconnus. (encore)
    - Des groupes qui ont pris leur retraite et qui n'ont pas la meilleure qualité selon les normes actuelles.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime Niveau 01

??? question "FR Anime Tier 01 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Groupes connus pour être actifs et ne faisant que de l'Anime
    - Les groupes dont les versions sont au moins comparables à celles recommandées par SeaDex.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime Niveau 02

??? question "FR Anime Tier 02 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Des groupes connus pour être actifs et ne faisant que de l'Anime, mais avec peu de sorties par an.
    - Des groupes connus pour être actifs et qui font des Anime ET d'autres types de sorties.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime Niveau 03

??? question "FR Anime Tier 03 - [Cliquez pour afficher/masquer]"

    - En-cours
    - Des groupes pas ou peu d'activité qui ont à un moment donné réalisé une sortie intéressante qui est soit la seule disponible (en VOSTFR/MULTi), soit encore première de sa catégorie.
    - Des groupes qui n'ont pas beaucoup sorti ou qui ne sont pas bien reconnus. (encore)
    - Les groupes qui font uniquement des dessins animés qui ont pris leur retraite (ou n'existent plus) et qui n'offrent peut-être pas la meilleure qualité selon les normes actuelles.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime FanSub

??? question "FR Anime FanSub - [Cliquez pour afficher/masquer]"

    Bons groupes connus qui ne font que du FanSub de bonne qualité.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Groupes de scènes FR

??? question "Groupes de scènes FR - [Cliquez pour afficher/masquer]"

    Groupes connus de la scène française.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### EN LQ

<sub>Sorties françaises de basse qualité = FR LQ</sub>

??? question "FR LQ - [Cliquez pour afficher/masquer]"

    Une collection de groupes français connus de Low-Quality qui sont souvent bannis des top trackers en raison de leur manque de qualité.

    !!! note

        - Annonces/Filigranes = Groupes connus pour mettre des publicités ou des filigranes dans leurs versions.
        - Mauvaises/Fausses versions = Groupes connus pour mentir sur la qualité, le type ou le nom de leurs versions.
        - DeTAG/ReTAG = Détagging ou vol de groupes.
        - Autres raisons = Groupes de libération interdits.

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index