#QbitorrentVPN

> > Repository: https://hub.docker.com/r/dyonr/qbittorrentvpn

## Installing Qbitorrent VPN

Environment variables to fill during installation:

| Varies | Required | Function | Example | Default |
|--------------|---------|---------------------------- ----------------------------------------|---------- -----|---------|
| VPN_ENABLED | Yes | Enable VPN (yes/no)? | yes | yes |
| VPN_TYPE | Yes | WireGuard or OpenVPN (wireguard/openvpn)? | wire guard | openvpn |
| VPN_USERNAME | No | | username | |
| VPN_PASSWORD | No | | password | |
| LAN_NETWORK | Yes | Comma-Delimited Local Area Networks with CIDR Notation | 172.18.0.0/24 | |

Warning -> currently not functional with wireguard.


## Qbitorrent settings

By default you must use as username (admin/adminadmin)

### File saving path

data source: /home/user/local/qbitorrent/downloads/…

> From the interface, you must start with downloads/...

We will start by securing and putting the interface in French

#### Language (Tools/Option/web interface)
![french](https://user-images.githubusercontent.com/64525827/107520001-33f4d980-6bb1-11eb-8690-249c3723710c.png)

#### Authentication (Tools/Option/web interface)
![auth](https://user-images.githubusercontent.com/64525827/107520003-348d7000-6bb1-11eb-9693-c6499659648d.png)


#### Download (Tools/Option/Downloads)
![record](https://user-images.githubusercontent.com/64525827/107518518-63a2e200-6baf-11eb-828b-2891a6c16588.png)


## Optimizations   


#### Cache management (Tools/Option/Advanced/libtorrent section)
you need to disable the use of cache

![cache](https://user-images.githubusercontent.com/64525827/107519416-8aade380-6bb0-11eb-82bb-15065cacc821.png)


#### Connections (Tools/Option/Connection)   
![connections](https://user-images.githubusercontent.com/64525827/107518883-d2803b00-6baf-11eb-97da-bc94d2bc2baf.png)


#### Prioritization (Tools/Option/BitTorrent)   

![prioritization](https://user-images.githubusercontent.com/64525827/107518996-f774ae00-6baf-11eb-9a90-31e456974b22.png)
