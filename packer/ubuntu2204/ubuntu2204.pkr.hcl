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

source "nutanix" "ubuntu" {
  cluster_name     = var.nutanix_cluster
  
  vm_nics {
    subnet_name    = var.nutanix_subnet
  }
  
  os_type          = "Linux"
  boot_type        = "uefi"
  image_name       = "Ubuntu-22.04-Golden"
  
  vm_disks {
    image_type = "ISO_IMAGE"
    source_uri = "https://releases.ubuntu.com/22.04.3/ubuntu-22.04.3-live-server-amd64.iso"
  }
  
  vm_disks {
    image_type = "DISK"
    disk_size_mb = 51200
  }
  
  cd_files = ["./http/user-data", "./http/meta-data"]
  cd_label = "cidata"

  ssh_username = "ubuntu"
  ssh_password = "ubuntu_password"
  ssh_timeout  = "20m"
}

build {
  sources = ["source.nutanix.ubuntu"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get upgrade -y",
      "sudo apt-get install -y qemu-guest-agent chrony",
      "sudo systemctl enable qemu-guest-agent"
    ]
  }
}
