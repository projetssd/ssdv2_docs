# Conclusion and recommendations

It looks like the app setup is complete! There are still avenues to explore, such as sending notifications for different events, customizing formats in Radarr and Sonarr, using lists to automatically add content, etc. It may be worth exploring these options based on your specific needs.

As for recommendations going forward, here is what you can consider:

### Improved SSH security

To improve security, consider configuring SSH to disable root login and change the default port:

```bash
sudo nano /etc/ssh/sshd_config
```

- Change `PermitRootLogin yes` to `PermitRootLogin no`.
- Change the default port by choosing a non-standard port number.

Don't forget to restart the SSH service after your changes:

```bash
sudo systemctl restart sshd
```

## Additional security

1. **Credentialing protocol**: If you haven't already, consider implementing a secure credentialing protocol, such as Google OAuth2 or Authelia, to strengthen the security of your system.
2. **Cloudflare Optimization**: You can optimize your use of Cloudflare by following the guide available at this address: [Cloudflare Optimization Guide](https://projetssd.github.io/ssdv2_docs/Installation/optimization- cloudflare/). This can help improve the performance and security of your system.
3. **Installation and configuration of UFW**: You can install and configure Uncomplicated Firewall (UFW) by following the guide available here: [UFW installation and configuration guide](https://projetssd.github.io /ssdv2_docs/Installation/ufw-Installation-configuration/). This will help you manage firewall rules to enhance security.

## **Recommended tools and guides**

**TRaSH-Guides**:

- These guides are valuable resources for configuring and optimizing Sonarr, Radarr, and other media management applications. They offer advice on configuring grades, profiles, and indexers to achieve the best possible results.

**Notify**:

- This tool helps synchronize configurations between your media management applications and TRaSH guides, ensuring that your settings are always optimized according to best practices. Notifiarr can also send custom notifications for various events on your server.

**Tautulli**:

- Tracking and monitoring application for Plex Media Server. It allows you to monitor your Plex server activity, generate detailed statistics on your media usage, receive notifications about new additions and user activities, and much more. It is an essential tool for Plex server administrators.

**LunaSea**:

- User-friendly mobile app designed to manage apps like Radarr, Sonarr, Lidarr, and others, right from your device. It offers a clean interface for managing and monitoring your movie, series and music collections, as well as searching and adding.

**nzb360**:

- nzb360 is a mobile application that allows you to intuitively manage and control your media management applications such as Sonarr, Radarr, Sabnzbd, NZBGet, and more, directly from your smartphone. It's a powerful tool for keeping an eye on your Plex server and related services, even when you're on the move.

## Additional applications according to needs

**Organize**:

- Customizable web portal that acts as a unified interface to access your favorite applications, services and websites. You can consolidate and organize all your links and apps in one place, making it easier to navigate and manage your online resources.

**Lidarr**:

- If you also manage a music collection, Lidarr is to music what Sonarr is to TV shows and Radarr is to movies. It can automate the downloading of your favorite music tracks.

**Bazarr**:

- For managing subtitles, Bazarr is an excellent addition. It works well with Sonarr and Radarr to automatically download subtitles for your movies and series.

**Readdarr**:

- It is a book and comics manager that automates the download of content based on criteria you define. Like Sonarr and Radarr for series and films, Readdarr can manage your literature and comics needs, keeping your library up to date with the latest releases.

**Whisparr**:

- Focuses on managing adult movie collections, incorporating similar tracking and automatic organization features.

**Jacket**:

- Jackett serves as a proxy between your torrent downloading apps and 100+ torrent trackers, allowing you to search a wide range of trackers directly from Sonarr, Radarr, etc. Although Prowlarr offers similar features, Jackett remains a solid alternative or complement, especially if you need to support specific trackers not supported by Prowlarr.

**Jellyfin**:

- Although you already use Plex, Jellyfin can serve as an open-source alternative or add-on for media streaming. It is a media server solution that allows you to manage and distribute your digital media collection without the restrictions of licensing.

**Mylar**:

- For comic book fans, Mylar automates the download of comics, similar to what Sonarr does for television series.

**Calibre-Web**:

- If you also manage an e-book collection, Calibre-Web can be a great addition. It allows you to manage and read your e-books in a web browser.

**Requestr**:

- It is a chatbot tool that allows your friends and family to request movies and TV shows via Discord or Telegram directly to your Sonarr or Radarr server. This is a great way to simplify the request process without needing to grant direct access to your media management tools. Requestrr can automate the process of requesting and adding content to your Plex server, making the experience more interactive and user-friendly.

## Server management and monitoring

**Uptime-Kuma**:

- Server monitoring tool that allows you to monitor the availability of your services and websites in real time. It generates reports on availability, latency and errors, allowing you to quickly detect problems and ensure maximum availability of your online services.

**Portainer**:

- Docker container management interface that simplifies managing and deploying Docker containers on your system. It offers an intuitive user interface to manage your containers, monitor their performance, make updates and much more. It is a powerful tool for Docker users.

**Grafana** or **Prometheus**:

- For advanced users interested in monitoring and visualizing their server performance. These tools can help you monitor resource usage, network performance, and more with customizable dashboards.

**Glances**:

- A cross-platform system monitoring tool that can give you a quick overview of resource usage on your server. It is less complex than Grafana and Prometheus for quick and easy setup.

## Exploring new features

**Nextcloud**:

- A personal cloud storage solution that can be used to backup setups, media files or even share files with friends and family securely. Nextcloud can complement your Plex server by offering flexible file storage and sharing.

**Home Assistant**:

- For those interested in home automation, integrating Home Assistant into your network can allow you to create interesting automations around your Plex viewing experience, like adjusting the lighting or thermostat when you start watching a movie.

And many others that you can find here: https://github.com/Ravencentric/awesome-arr

## Congratulations on reading through this comprehensive guide on setting up your server with SSDV2! **[🎉](https://emojipedia.org/fr/cotillons)**

We hope that the detailed instructions, practical tips, and recommendations provided have equipped you with the knowledge needed to build a high-performance and secure server. You now have a robust environment for your streaming and media file management needs. Remember, the journey doesn't end here, keep exploring, learning and adapting your server to better meet your needs. Once again, **well done** and good luck in your digital adventures!