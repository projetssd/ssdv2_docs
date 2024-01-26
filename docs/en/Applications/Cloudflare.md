# Cloudflare

### Presentation
More than CDN services, customers trust Cloudflare's global network to improve the security, performance, and reliability of everything connected to the Internet.

Cloudflare is designed to be easily configured. Anyone with a website and personal domain can use Cloudflare, regardless of their choice of platform. Cloudflare does not require any special hardware, software or code changes.

> Here is the official presentation

### The steps must be carried out in the following order:
* Create a Cloudflare account and add a website
* Transfer DNS management to cloudflare
* Retrieve cloudflare global API
* Switch SSL/TLS mode to full type

### Step 1. Create a Cloudflare account or log in.

Go here: [https://href.li/?https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up):

- Enter your email address and password

- Click **Create Account**

- then click on the blue button ``add a site``


Enter the root domain for your website then click **Add Site**. For example, if your site is www.example.com, enter example.com.

Cloudflare attempts to automatically identify your DNS records. This will take approximately 60 seconds.

- Click **Next**.

- Choose an offer level, free, and click on **Confirm offer**:

- Click Continue

- Copy the 2 Cloudflare nameservers displayed then click: **Done, check nameservers**.

***

### Step 2. Change your domain nameservers to Cloudflare

In this example I will use OVH which is relatively common.

If you have a different provider, we invite you to Discord to guide you.

We will go to the OVH administration console:

[https://href.li/?https://www.ovh.com/manager/web/#/configuration/domains](https://www.ovh.com/manager/web/#/configuration/domains )

Click on your domain and go to the section: **DNS Servers**.

- Click Change DNS Servers
- Indicate the DNS copied previously in Cloudflare

- Click **Apply configuration**

Now you will have to wait a bit for the DNS propagation to take place (up to 24 hours).

##### You will receive a confirmation email.

***

### Step 3. Retrieve Cloudflare Global API

- Go to your Clouflare account and click on ``Overview`` on the left side of the screen.

- Bottom right ``Get your API token``

- Then the ``API token`` tab

- Click on ``display`` opposite the ``Global API Key`` line

- Collect your token and **keep it for installing the script**

***

### Step 4. Changing the SSL/TLS encryption mode

![Cloudflare - SSL:TLS](https://user-images.githubusercontent.com/64525827/105042745-e5966400-5a64-11eb-9dd9-aa4bed5bd8b7.png)
