terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.9.0"
    }
  }
}

resource "nutanix_image" "os_image" {
  name        = var.image_name
  description = "Automatically built OS Image from ${var.image_source_uri}"
  source_uri  = var.image_source_uri
}

output "image_name" {
  value = nutanix_image.os_image.name
}

output "image_id" {
  value = nutanix_image.os_image.id
}
