# Cloudflare Optimization

**1. SSL/TLS Options**  
<br>
Activer **Full SSL mode**  
<br>
![68747470733a2f2f77696b692e73637269707473656564626f78646f636b65722e636f6d2f75706c6f6164732f696d616765732f67616c6c6572792f323032302d31312f7363616c65642d313638302d2f73736c2d746c732e706e67](https://user-images.githubusercontent.com/64525827/105626452-ebf35a00-5e2f-11eb-991f-a491e98fd1b5.png)
 
### Then in the Edge Certificates tab  

![](https://user-images.githubusercontent.com/64525827/105626484-3543a980-5e30-11eb-8d2d-37657b581a0a.png)
 
Always Use HTTPS: **ON** ==> Automatically redirects all http requests to https.  

HTTP Strict Transport Security (HSTS): **Enable**  
(Attention). HSTS improves the level of security. However, activate this option with caution. Any certificate issues/changes (e.g. Cloudflare suspension) may prevent you from accessing your services (you can still access them locally with IP:port). I therefore recommend only activating it after verifying that everything is working perfectly.   
<br>
Minimum TLS Version: **1.2**  
Only connections with TLS version 1.2 or later will be allowed for enhanced security.  
<br>
Opportunistic Encryption: **ON**  
Opportunistic encryption allows browsers to benefit from the improved performance of HTTP/2 by letting them know that your site is available over an encrypted connection.  
<br>
TLS 1.3: **ON**  
TLS 1.3 is the latest, fastest, and most secure version of the TLS protocol. Activate it.  
<br>
Automatic HTTPS Rewrites: **ON**  
This option fixes browsers' mixed content warning by automatically rewriting HTTP requests to HTTPS.  
<br>
Certificate Transparency Monitoring: **ON**  
Cloudflare sends an email when a certificate authority issues a certificate for your domain. So, when your LetsEncrypt certificate is renewed, you will receive an email.  
<br>
**2. Firewall**  
<br>
**Firewall Rules**  
Under Firewall Rules, the free plan allows you to create up to 5 rules.

Using this feature you can block certain types of traffic. For example, I block all requests from China. You can also choose to allow access only from countries you know will access your apps and block the rest.  
<br>
![cloudflare-firewall-rules-740x335](https://user-images.githubusercontent.com/64525827/105626846-f5ca8c80-5e32-11eb-94a7-663d277006a4.png)


#### Firewall Tools
You can also use the Tools section to set up certain blocks or permissions. You can even set a rule for incoming traffic.

In the example below, I whitelist traffic from my home WAN IP address so that all requests from my home IP address are allowed and not blocked or challenged.  

![cloudflare_ip_whitelist-740x309](https://user-images.githubusercontent.com/64525827/105626853-febb5e00-5e32-11eb-8322-8bb965180b13.png)


#### Firewall Settings

#### Security Level: **High**  
Blocking all visitors who have shown threatening behavior in the last 14 days.  

* Bot Fight Mode: **ON**  
Handling requests for known bot patterns before they can access your site.  

* Challenge Passage: **30 Minutes**  
Specify how long a visitor, who has passed a Captcha or JavaScript, can access your website.  

* Browser Integrity Check: **ON**  
Evaluate your visitor's browser HTTP headers for threats. If a threat is detected, a blocking page will be sent.  

* 3. Speed
This concerns servers with high traffic, particularly for a website, little impact on our sedboxes  

* Auto Minify: **OFF**  
Reduce the file size of the source code on your website. But if not done correctly, it can impact Javascript and CSS, and cause unexpected behavior.  

* Brotli: **ON**  
Speeds up page load times for HTTPS traffic by applying Brotli compression  

* Rocket Loader: **OFF**  


![](https://user-images.githubusercontent.com/64525827/105626862-14c91e80-5e33-11eb-866e-87f642d14ef1.png)

* 4. Caching

Caching Level: **Standard**  
Determine how much of your website's static content Cloudflare should cache.  

Browser Cache TTL: **1 hour**  
During this period, the browser loads files from its local cache, making pages load faster. Setting it too long may force you to clear your browser's cache to see the changes.  

Always Online: **OFF**  
If your server goes down, Cloudflare will serve your web application's "static" pages from cache  

**5. Page Rules**  
Next, we move on to one of the most important Cloudflare settings for Docker and Traefik. This is essential, especially, if you are running media servers (e.g. Plex, Emby, Jellyfin, etc.).

Page Rules provide finer-grained, URL-based control of Cloudflare settings. Some pages in our setup need to bypass Cloudflare resources. In my case, I wanted to avoid the following apps from using Cloudflare cache: plex, Emby, Jellyfin  

![](https://camo.githubusercontent.com/cda7414ca78e8e8d5ea5754390e57c0681fce71b/68747470733a2f2f692e696d6775722e636f6d2f513433304c6b7a2e706e67)  

![](https://camo.githubusercontent.com/c2cb6903c9a1279b99daeddf09430589bfe29913/68747470733a2f2f692e696d6775722e636f6d2f706c57456c6b662e706e67)  

This is important to comply with Cloudflare's terms and conditions for the free plan. Otherwise you may be banned by Cloudflare for violating their TOS.