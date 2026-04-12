terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.9.0"
    }
  }
}

resource "nutanix_foundation_central_image_cluster" "cluster_build" {
  cluster_name        = var.cluster_name
  cluster_external_ip = var.cluster_ip
  redundancy_factor   = 2

  common_network_settings {
    cvm_vlan_id        = 0
    hypervisor_vlan_id = 0
    subnet_mask        = "255.255.255.0"
    default_gateway    = "10.0.0.1"
  }

  dynamic "node_list" {
    for_each = var.nodes
    content {
      mac_address   = node_list.value.mac_address
      cvm_ip        = var.cvm_ip_pool[node_list.key]
      hypervisor_ip = var.hypervisor_ip_pool[node_list.key]
      ipmi_ip       = var.ipmi_ip_pool[node_list.key]
      node_position = node_list.key
      image_now     = true
    }
  }
}

output "cluster_name" {
  value = nutanix_foundation_central_image_cluster.cluster_build.cluster_name
}
