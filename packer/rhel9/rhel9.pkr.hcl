packer {
  required_plugins {
    nutanix = {
      version = ">= 0.8.0"
      source  = "github.com/nutanix-cloud-native/nutanix"
    }
  }
}

variable "nutanix_cluster" {
  type    = string
  default = "dev-cluster"
}

variable "nutanix_subnet" {
  type    = string
  default = "dev-vlan-100"
}

source "nutanix" "rhel9" {
  cluster_name     = var.nutanix_cluster
  
  vm_nics {
    subnet_name    = var.nutanix_subnet
  }
  
  os_type          = "Linux"
  boot_type        = "uefi"
  image_name       = "RHEL9-Golden"

  vm_disks {
    image_type = "ISO_IMAGE"
    # Example minimal boot iso
    source_uri = "https://example.com/rhel-9-x86_64-boot.iso"
  }
  
  vm_disks {
    image_type = "DISK"
    disk_size_mb = 61440
  }
  
  http_directory = "http"
  boot_command   = [
    "<up><wait><tab> inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ks.cfg<enter>"
  ]

  ssh_username = "root"
  ssh_password = "rhel_password"
  ssh_timeout  = "30m"
}

build {
  sources = ["source.nutanix.rhel9"]

  provisioner "shell" {
    inline = [
      "yum update -y",
      "yum install -y qemu-guest-agent chrony curl",
      "systemctl enable --now qemu-guest-agent chronyd"
    ]
  }
}
