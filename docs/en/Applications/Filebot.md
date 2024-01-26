# Filebot

#### Register a license

Put the license file in /opt/seedbox/docker/${USER}/.filebot/FileBot_License.psm

```
/opt/seedbox/docker/${USER}/.filebot/filebot.sh --license /opt/seedbox/docker/${USER}/.filebot/FileBot_License.psm
```

#### Filebot tip proposed by @TEALC

How to separate 4k Movies from others (don't forget to replace USER with your nickname)

1. Create the Films4k folder in /home/USER/local/.

2. In the Plex settings, add a Films type Libraries (give it a name e.g.: 4K Films, language: Fr), with a folder in Plex --> /data/Films4k.

3. In SSH

```cd /home/USER/scripts/plex_autoscan``` 

Then

```python scan.py update_sections```

4. ``` nano /home/USER/scripts/plex_autoscan/config/config.json```

Around line 84 there should be "/data/Films4k/" (DO NOT TOUCH THE NUMBERING):

```"PLEX_SECTION_PATH_MAPPINGS": {
    "1": [
      "/data/Animes/"
    ],
    "2": [
      "/data/Films/"
    ],
    "3": [
      "/data/Music/"
    ],
    "4": [
      "/data/Series/"
    ],
    "5": [
      "/data/Films4k/"
    ]
  },

```
5. Find the line "SERVER_FILE_EXIST_PATH_MAPPINGS": { and after the last ] (just before the }, add:

```
,
    "/home/USER/local/Films4k/": [
      "/data/Films4k/"
    ]
```

6. Find the line "SERVER_PATH_MAPPINGS": { and after the last ] (just before the }, add:

```
,
    "/data/Films4k/": [
      "/movies4k/", 
      "/home/USER/Medias/Films4k/", 
      "/home/USER/local/Films4k/"
    ]
```

7. Find the line "SERVER_SCAN_PRIORITIES": { and after the last ] (just before the }, add (AAA = the following number):

```,
    "AAA": [
      "/Films4k/"
    ]
```

8. Save then close.

In SSH

```systemctl restart plex_autoscan.service```

```nano  /opt/seedbox/docker/USER/.filebot/filebot-process.sh```

Replace with:

```
#!/bin/bash

sh /opt/seedbox/docker/USER/.filebot/filebot.sh -script fn:amc --output "/home/USER/local" --action move --conflict skip -non-strict --lang fr --log-file amc.log --def unsorted=y music=y --def excludeList=/home/USER/exclude.txt "exec=/home/USER/scripts/plex_autoscan/plex_autoscan_rutorrent.sh" "ut_dir=/home/USER/filebot" --def movieFormat="/home/USER/local/{fn =~ /2160p|4K|4k|UHD/ ? 'Films4k' : 'Films'}/{n} ({y})/{n} ({y}) _ {source}.{vf} - {audioLanguages} - {textLanguages} - {vc}.{ac}-{channels}" seriesFormat="/home/USER/local/Series/{n}/Saison {s}/{n} - {s00e00} - {t} _ {source}.{vf} - {audioLanguages} - {textLanguages} - {vc}.{ac}-{channels}" animeFormat="/home/USER/local/Animes/{n}/{episode.special ? 'Special' : 'Saison '+s}/{n} - {episode.special ? 'S00E'+special.pad(2) : s00e00} - {t} _ {source}.{vf} - {audioLanguages} - {textLanguages} - {vc}.{ac}-{channels}" musicFormat="/home/USER/local/Musiques/{n}/{album+'/'}{pi.pad(2)+'. '}{artist} - {t}"
```

**WARNING** this script moves the files, to be able to stay in SEED replace: --action move with --action copy.

 Save and close.

I modified the renaming system, the files will have the format {title} (year) _ {quality}.{format} - [languages] - [languages ​​under titles] - {video codec}.{audio codec}- {number of channels}.mkv

So that filebot also sorts before 2005
Create the FilmsOdl folder (like film4k)
Replace the movieformat in filebot with

```movieFormat="/home/USER/local/{y < 2006 ? 'FilmsOld' : fn =~ /2160p|4K|4k|UHD/ ? 'Films4k' : 'Films'}/{n} ({y})/{n} ({y}) _ {source}.{vf} - {audioLanguages} - {textLanguages} - {vc}.{ac}-{channels}" ```