
# Add Remote Worker
This role is designed for downloading ISO from `infraEnv` and extracting all files to 
needed locations tfpd and http servers.


### The Flow
---
There are a few Stages for Downloading the ISO

1. Getting Download URL from `infraEnv` on `Assisted-Installer` cluster
2. Extracting files to `HTTP_DIR` and `TFTP_DIR`
3. Create ignition file from ISO
4. Downloading `rootfs` from URL


### **Variables**
---

`Assisted-Installer` 
```yaml
# Mandatory
KUBECONFIG_FILE:    ""
INFRA_ENV_NAME:     ""

# Optional -  Default Values
NAMESPACE:          "default"

# Optional -  Default Values
## ISO params
URL_PORT:           ""
DOWNLOADED_ISO:     "image.iso"
TFTP_DIR:           "/var/lib/tftpboot"
MNT_EFIBOOT:        "/mnt/iso"
HTTP_DIR:           "/var/www/html/pxe"




