# Plex-Dupfinder

Plex Dupefinder [(by l3uddz)](https://github.com/l3uddz/plex_dupefinder) is a python application that searches for duplicate versions of media (episodes and movies) in your Plex library and asks Plex to remove the versions from lowest quality (based on a scoring algorithm), automatically or interactively (i.e. a prompt on each search), leaving you with a high quality media file.  

Configuration is automated by the script, but you can change some settings in /home/user/scripts/plex_dupefinder/config.json

#### Example  

```
{
    "AUDIO_CODEC_SCORES": {
        "aac": 1000,
        "ac3": 1000,
        "dca": 2000,
        "dca-ma": 4000,
        "eac3": 1250,
        "flac": 2500,
        "mp2": 500,
        "mp3": 1000,
        "cpm": 2500,
        "truehd": 4500,
        "Unknown": 0,
        "wmapro": 200
    },
    "AUTO_DELETE": false,
    "FILENAME_SCORES": {
        "*.avi": -1000,
        "*.ts": -1000,
        "*.vob": -5000,
        "*1080p*BluRay*": 15000,
        "*720p*BluRay*": 10000,
        "*dvd*": -1000,
        "*HDTV*": -1000,
        "*PROPER*": 1500,
        "*Remux*": 20000,
        "*REPACK*": 1500,
        "*WEB*CasStudio*": 5000,
        "*WEB*KINGS*": 5000,
        "*WEB*NTB*": 5000,
        "*WEB*QOQ*": 5000,
        "*WEB*SiGMA*": 5000,
        "*WEB*TBS*": -1000,
        "*WEB*TROLLHD*": 2500,
        "*WEB*VISUM*": 5000
    },
    "PLEX_SECTIONS": {
        "Movies": 1,
        "TV": 2
    },
    "PLEX_SERVER": "https://plex.yourdomain.com",
    "PLEX_TOKEN": "",
    "SCORE_FILESIZE": true,
    "SKIP_LIST": [],
    "VIDEO_CODEC_SCORES": {
        "h264": 10000,
        "h265": 5000,
        "hevc": 5000,
        "mpeg1video": 250,
        "mpeg2video": 250,
        "mpeg4": 500,
        "msmpeg4": 100,
        "msmpeg4v2": 100,
        "msmpeg4v3": 100,
        "Unknown": 0,
        "vc1": 3000,
        "vp9": 1000,
        "wmv2": 250,
        "wmv3": 250
    },
    "VIDEO_RESOLUTION_SCORES": {
        "480": 3000,
        "720": 5000,
        "1080": 10000,
        "4k": 20000,
        "sd": 1000,
        “Unknown”: 0
    }
}
```


![](https://camo.githubusercontent.com/87d1f9ea365016f35689d475be385e3d484dfe5c/68747470733a2f2f692e696d6775722e636f6d2f643173444e6c452e706e67)

Scoring is based on: non-configurable and configurable parameters.

* Non-configurable parameters are: bitrate, duration, height, width and audio channel.

* Configurable settings are: audio codec scores, video codec scores, video resolution scores, file name scores and file sizes (cannot be enabled or disabled).

Note: bitrate, duration, height, width, audio channel, audio and video codecs, video resolutions (e.g. SD, 480p, 720p, 1080p, 4K, etc.), and file sizes are all extracted from the metadata that Plex retrieves when analyzing media.

## Demo
https://asciinema.org/a/180157?cols=180&rows=50