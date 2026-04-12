terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.9.0"
    }
  }
}

provider "nutanix" {
  # Provider credentials should be passed via env vars
}

variable "vm_name" {
  type = string
}

module "nutanix_vm" {
  source = "../../modules/nutanix_vm"

  cluster_name    = "prod-cluster"
  vm_name         = var.vm_name
  subnet_name     = "prod-vlan-200"
  memory_size_mib = 8192
  num_sockets     = 2
}
