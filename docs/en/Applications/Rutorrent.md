#Rutorrent

## Separation of Completed Downloads
> You will then need to indicate the path in Radarr and Sonarr.

<img width="582" alt="Rutorrent" src="https://user-images.githubusercontent.com/64525827/105710575-998d6880-5f17-11eb-853c-ff649a4c7f20.png">


## For those who occasionally have a core blocked at 100% with rutorrent

	docker exec rutorrent-user sh -c "curl --version"
	docker exec rutorrent-user sh -c "echo http://dl-cdn.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories"
	docker exec rutorrent-user sh -c "apk update"
	docker exec rutorrent-user sh -c "apk add libcurl=7.65.0-r0"
	docker exec rutorrent-user sh -c "apk add curl=7.65.0-r0"
	docker exec rutorrent-user sh -c "curl --version"


Generally go to http://dl-cdn.alpinelinux.org/alpine/edge/main, look for the most recent curl version, and replace it in the command lines above

## rtorrent-cleaner commands from @Magicalex

	rtorrent-cleaner report
	rtorrent-cleaner rm
	rtorrent-cleaner mv /data/old
	rtorrent-cleaner torrents
	rtorrent-cleaner --version