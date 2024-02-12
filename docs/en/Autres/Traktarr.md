#Traktarr

Traktarr uses Trakt.tv to find shows and movies to add to Sonarr and Radarr, respectively.  

https://github.com/Cloudbox/Community/wiki/Traktarr-Tips  

Example:  
```
traktarr movies -t person -f /home/yohann/Media/Classics -a 'fernandel' -l 10
```

#### 1. Supported task list types:

* Official trakt lists
        Trends
        Popular
        Anticipated
        Box office
        Most viewed
        Most played

* Public lists

* Private lists

* Watchlist

*Custom List(s)

* Support for multiple (authenticated) users.


<a href="https://asciinema.org/a/180044" target="_blank"><img src="https://asciinema.org/a/180044.svg" /></a>

#### 2. Create a Trakt app
1. Create a Trakt application by going to https://trakt.tv/oauth/applications/new

2. Enter a name for your application. for example traktarr

3. Enter ```urn:ietf:wg:oauth:2.0:oob``` in the Redirect uri field

4. Click “SAVE APP”

Then open the config.json configuration file and
insert your client ID and client secret into the config.json, like this:
```
      "trakt": {
         "client_id": "your_trakt_client_id",
         “client_secret”: “your_trakt_client_secret”
     }
```

#### 3. Authenticate user(s) (optional)

For each user whose private lists you want to access (e.g. checklist and/or custom lists), you must authenticate.

Repeat the following steps for each user to be authenticated:

1. Run traktarr trakt_authentication

2. You will get the following prompt:
```
     - We're talking to Trakt to get your verification code. Please wait a moment... - Go to: https://trakt.tv/activate on any device and enter A0XXXXXX. We'll be polling Trakt every 5 seconds for a reply
```
3. Go to https://trakt.tv/activate

4. Enter the code you see in your terminal.

5. Click Continue.

6. If you are not logged in to Trakt, log in now.

7. Click "Accept".

You will receive the message: "Woohoo! Your device is now connected and will automatically refresh in a few seconds."

You have now authenticated the user.

You can repeat this procedure for as many users as you want.

#### Setup

1. Automatic

Used for automatic/scheduled Traktarr tasks.

Movies can be streamed separately and then as part of series.

Note: These settings are only necessary if you plan to use Traktarr on a schedule (versus using it only as a CLI command; see Usage).
```
"automatic": {
  "movies": {
    "anticipated": 3,
    "boxoffice": 10,
    "interval": 24,
    "popular": 3,
    "trending": 2,
    "watched": 2,
    "played_all": 2,
    "watchlist": {},
    "lists": {},
  },
  "shows": {
    "anticipated": 10,
    "interval": 48,
    "popular": 1,
    "trending": 2,
    "watched_monthly": 2,
    "played": 2,
    "watchlist": {},
    "lists": {}
  }
},
```

interval - Specify the frequency (in hours) to run the Traktarr task.

anticipated, popular, trending, boxoffice (movies only) - Specify the number of items to search for in each Trakt list.

watched - Adds the most watched items by unique Trakt users (multiple views excluded).

* watched_weekly / watched_weekly - Most watched of the week.

* watched_monthly - Most watched during the month.

* watched_yearly - Most watched of the year.

* watched_all - Most watched of all time.

played - Adds items most often played by Trakt users (multiple views included).

* played / played_weekly - Most played_weekly of the week.

* played_monthly - Most played in the month.

* played_yearly - Most played_yearly of the year.

* played_all most played of all time.

watchlist - Specify watchlists to retrieve (see explanation below).

lists - Specify custom lists to retrieve (see explanation below).

The options are numerous, I invite you to consult the wiki at https://github.com/l3uddz for more information.

#### example with lists and radarr

For public and private lists, you will need the URL of that list. When viewing the listing on Trakt, simply copy the URL from your browser's address bar.

```
{
  "automatic": {
    "movies": {
      "anticipated": 3,
      "boxoffice": 10,
      "interval": 24,
      "popular": 3,
      "trending": 2,
      "lists": {
      "https://trakt.tv/users/toto/lists":10
      }
    },
    "shows": {
      "anticipated": 10,
      "interval": 48,
      "popular": 1,
      "trending": 2
    }
```

**traktarr movies --list-type watchlist**
![Imgur](https://i.imgur.com/3qawDFd.png)

chrome plugin for trak.tv french

https://github.com/nliautaud/trakttvstats