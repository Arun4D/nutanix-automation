variable "image_name" {
  type        = string
  description = "The name of the image to build/import"
}

variable "image_source_uri" {
  type        = string
  description = "The HTTP URI to the cloud-init ready image (e.g., qcow2 or img)"
}
