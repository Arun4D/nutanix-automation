terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.9.0"
    }
  }
}

data "nutanix_cluster" "cluster" {
  name = var.cluster_name
}

data "nutanix_subnet" "subnet" {
  subnet_name = var.subnet_name
}

resource "nutanix_virtual_machine" "vm" {
  name                 = var.vm_name
  cluster_uuid         = data.nutanix_cluster.cluster.id
  num_vcpus_per_socket = var.num_vcpus_per_socket
  num_sockets          = var.num_sockets
  memory_size_mib      = var.memory_size_mib

  nic_list {
    subnet_uuid = data.nutanix_subnet.subnet.id
  }

  disk_list {
    disk_size_bytes = 50 * 1024 * 1024 * 1024
    device_properties {
      device_type = "DISK"
      disk_address {
        device_index = 0
        adapter_type = "SCSI"
      }
    }
  }
}
