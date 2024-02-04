# Prerequisites to follow the guide

## Domain name

Access to your applications requires a domain name. Our script makes it easy to add and customize the subdomain for each application.

- **Example:** `https://rutorrent.mondomaine.com`

Note that some free domain name providers, like Freenom, are not compatible with Cloudflare.

**Recommended domain name providers:**

-Gandi
-LWS
- OVH
- Ionos
- InternetBS
- And many others...

---

## Configure Cloudflare

### Presentation

Cloudflare offers more than CDN services. Its global network is designed to improve the security, performance and reliability of everything connected to the Internet, with easy setup for anyone.

### Configuration Steps

#### 1. Creating or Login to a Cloudflare Account

- Go to [the Cloudflare website](https://dash.cloudflare.com/sign-up).
- Enter your email address and a password.
- Click on "Create an account".
- Add your site by clicking on the blue “Add site” button.

**Add your domain** by entering the root domain, then click "Add Site". Cloudflare will identify your DNS records.

- Choose the free offer and confirm.
- Follow the instructions to change your DNS servers to those provided by Cloudflare.

#### 2. Change DNS Servers to Cloudflare

- Access the administration console of your domain provider, for example OVH.
- Change DNS servers to those provided by Cloudflare.
- Apply the configuration and wait for DNS propagation (up to 24 hours).

#### 3. Retrieving Global Cloudflare API

- In your Cloudflare account, click "Overview", then "Get your API token".
- Click "View" next to "Global API Key".
- Keep your token for installing the script.

#### 4. Configuring SSL/TLS Encryption Mode

- Set SSL/TLS mode to "Full".