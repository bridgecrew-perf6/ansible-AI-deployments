# Ansible Assisted Installer Deployment

This Ansible roles is for deploying remote worker node with `CRD's`. 
The installation is without `BMH`, instead we are downloading the ISO and bootpxe the remote node.

### **Requirements** 
---
1. the installation will run on a `jump host` which is directly connected to the remote host. the `jump host` will be used to running services such as DHCP, HTTP and TFTP 
2. The `jump host` and the `remote-node` will need internet access and access to the API of the cluster and assisted installer cluster

### **Roles**
---
[setup-bootpxe](docs/setup-bootpxe.md) role design to install and configure services for boot pxe  
[add-remote-worker](docs/add-remote-worker.md) adding remote worker with CRD's for Assisted-installer

<BR>

### **How To Use**
---
Running the `playbook.yaml` will contain all relevant roles for the deployment. 
with mandatory vars in `vars.yaml`
```yaml
# playbook.yaml
- hosts: all
  roles:
    - setup-bootpxe
    - add-remote-worker
  vars_files:
    - vars.yaml 
  
```

This example show to minimum vars required to run
```yaml
# vars.yaml

# Boot PXE Network
INTERFACE:              # Interface  name connected to the remote worker

KUBECONFIG_FILE:        # local kubeconfig file fot Asisted installer 
KUBECONFIG_CLUSTER:     # local kubeconfig file for remote worker cluster should be installed on

### Assisted Installer config
NAMESPACE:      # namespace where the cluster is installed /imported
INFRA_ENV_NAME: # name of the infrEnv of the cluster

### BMC 
BMC_ADDRESS:    # BMC IP / FQDN
BMC_USER:       # BMC Username
BMC_PASSWORD:   # BMC Password

```
Create a Basic Inventory file
> **note:** default user is `kni`, add `ansible_user="username"` for a different username
```ini
[jump-server]
server01 
```

finally run `start.sh`.

### **Known Issues and Limitations**
---
1. The repo support `ARM` deployments only.
2. The `Agent` must be a Bluefield card
3. when the `Agent` exist on `Assisted-installer` the deployment will fail, must delete the `Agent` before starting the deployment.



## Thanks
---