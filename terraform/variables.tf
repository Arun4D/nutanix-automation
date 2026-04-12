variable "env" {
  type        = string
  description = "Environment name (dev, prod)"
}

variable "cluster_name" {
  type        = string
  description = "Nutanix cluster name"
}

variable "subnet_name" {
  type        = string
  description = "Nutanix subnet name"
}

variable "vm_name" {
  type        = string
  description = "Name of the VM"
}

variable "num_vcpus_per_socket" {
  type    = number
  default = 2
}

variable "num_sockets" {
  type    = number
  default = 1
}

variable "memory_size_mib" {
  type    = number
  default = 4096
}

variable "image_name" {
  type    = string
  default = "Ubuntu-22.04"
}

variable "image_source_uri" {
  type    = string
  default = "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img"
}

variable "admin_pub_key" {
  type    = string
  default = "ssh-rsa dummy-key-replace-me user@host"
}
