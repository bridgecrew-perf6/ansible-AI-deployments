# Setup Boot PXE
This role is design for installing and configuring services for `bootpxe`


## Services
---
The following Services will be installed

1. `DHCPD` address and bootpxe option for clients
2. `HTTPD` Web Service to store files
3. `TFTP-SERVER` tftpd service with contains kernel boot files


## Variables
---
example of values and defaults 

`DHCPD`
```yaml
# Mandatory
INTERFACE: ""   # Interface name

# Optional -  Default Values
# DHCP addressing pool with DNS and NTP
DHCP_SUBNET:    "10.255.255.0"
DHCP_NETMASK:   "255.255.255.0"
DHCP_RANGE:     "10.255.255.1 10.255.255.10"
DHCP_ROUTER:    "10.255.255.254"
DHCP_DNS:       "10.19.143.247"
DHCP_NTP:       "clock.redhat.com"
```

`HTTPD`
```yaml
# Optional -  Default Values
HTTP_DIR:       "/var/www/html/pxe"
```

`TFTP-SERVER`
```yaml
# Optional -  Default Values
TFTP_DIR:       "/var/lib/tftpboot"
```

