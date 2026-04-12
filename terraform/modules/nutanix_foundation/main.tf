terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.9.0"
    }
  }
}

resource "null_resource" "foundation_imaging" {
  count = length(var.nodes)

  provisioner "local-exec" {
    command = "echo 'Imaging Node MAC: ${var.nodes[count.index].mac_address} via Foundation API...'"
  }
}

resource "null_resource" "cluster_creation" {
  depends_on = [null_resource.foundation_imaging]

  provisioner "local-exec" {
    command = "echo 'Executing Cluster Create for ${var.cluster_name} with IP ${var.cluster_ip}'"
  }
}

output "cluster_name" {
  value = var.cluster_name
}
