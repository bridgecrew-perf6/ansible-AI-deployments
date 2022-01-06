
# Add Remote Worker
This role is Desgin for `Assisted-Installer`  for adding worker via `CRD's`.

### The Flow
---
There are a few Stages for installing the remote Worker

1. Getting Download URL from `infraEnv` on `Assisted-Installer` cluster
2. Extracting files to `HTTP_DIR` and `TFTP_DIR`
3. boot the `node` via `PXE` and wait until new `Agent` has spawn
4. Set `Agent` hostname, kernel arguments and Approve him.
5. After Approval, Wait for new `CSR` request for the `node`
6. `CSR`  Approval 


### **Variables**
---

`Assisted-Installer` 
```yaml
# Mandatory
KUBECONFIG_FILE:    ""
INFRA_ENV_NAME:     ""

# Optional -  Default Values
VALIDATE_CRET:      "yes"
REMOTE_HOSTNAME:    "remote-worker1"
NAMESPACE:          "default"

# Optional -  Default Values
## ISO params
DOWNLOADED_ISO:     "image.iso"
TFTP_DIR:           "/var/lib/tftpboot"
MNT_EFIBOOT:        "/mnt/iso"
HTTP_DIR:           "/var/www/html/pxe"
AGENT_TIMEOUT:      600

# Optional -  Default Values
KERNEL_ARGS:        '"--append-karg", "console=tty0 console=ttyS0,115200 console=ttyAMA1 console=hvc0 console=ttyAMA0 earlycon=pl011,0x01000000"'
```

`Cluster`
```yaml
# Mandatory
KUBECONFIG_CLUSTER: ""
```

`BMC`
```yaml
# Mandatory
BMC_ADDRESS:    ""
BMC_USER:       ""
BMC_PASSWORD:   ""
```


