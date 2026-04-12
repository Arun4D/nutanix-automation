packer {
  required_plugins {
    nutanix = {
      version = ">= 0.8.0"
      source  = "github.com/nutanix-cloud-native/nutanix"
    }
    windows-update = {
      version = "0.14.3"
      source = "github.com/rgl/windows-update"
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

source "nutanix" "windows2022" {
  cluster_name     = var.nutanix_cluster

  vm_nics {
    subnet_name    = var.nutanix_subnet
  }
  
  os_type          = "Windows"
  boot_type        = "uefi"
  image_name       = "Windows-2022-Golden"

  # Windows OS ISO
  vm_disks {
    image_type = "ISO_IMAGE"
    source_uri = "https://example.com/windows_server_2022.iso"
  }

  # Nutanix VirtIO ISO mapping (Required for network and disk drivers on AHV)
  vm_disks {
    image_type = "ISO_IMAGE"
    source_uri = "http://download.nutanix.com/mobility/1.1.7/Nutanix-VirtIO-1.1.7.iso"
  }
  
  vm_disks {
    image_type = "DISK"
    disk_size_mb = 102400
  }

  cd_files = ["./http/autounattend.xml", "./http/setup.ps1"]
  boot_command = ["<spacebar><wait><spacebar>"]

  communicator   = "winrm"
  winrm_username = "Administrator"
  winrm_password = "WinPassword123!"
  winrm_insecure = true
  winrm_use_ssl  = false
  winrm_timeout  = "45m"
}

build {
  sources = ["source.nutanix.windows2022"]

  # Need to wait for Sysprep to fully complete before initiating updates
  provisioner "powershell" {
    inline = [
      "Write-Host 'System Successfully Bootsrapped'",
      "# Additional hardening blocks here"
    ]
  }

  # Windows Updates run
  provisioner "windows-update" {
    search_criteria = "IsInstalled=0"
    filters = [
      "exclude:$_.Title -like '*VMware*'",
      "include:$true"
    ]
  }
  
  # Final Sysprep execution
  provisioner "powershell" {
    inline = [
      "C:\\Windows\\system32\\sysprep\\sysprep.exe /generalize /oobe /shutdown /quiet"
    ]
  }
}
