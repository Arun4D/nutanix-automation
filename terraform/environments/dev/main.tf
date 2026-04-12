terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.9.0"
    }
  }
}

provider "nutanix" {
  # Provider credentials should be passed via env vars: NUTANIX_ENDPOINT, NUTANIX_USERNAME, NUTANIX_PASSWORD
}

variable "vm_name" {
  type = string
}

module "nutanix_vm" {
  source = "../../modules/nutanix_vm"

  cluster_name = "dev-cluster"
  vm_name      = var.vm_name
  subnet_name  = "dev-vlan-100"
}
