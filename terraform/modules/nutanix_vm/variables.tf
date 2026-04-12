variable "cluster_name" {
  type = string
}

variable "vm_name" {
  type = string
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

variable "subnet_name" {
  type = string
}

variable "image_name" {
  type        = string
  description = "Name of the base OS image to clone"
  default     = "Ubuntu-22.04"
}

variable "admin_pub_key" {
  type        = string
  description = "Public SSH key for the admin user"
  default     = "ssh-rsa dummy-key-replace-me user@host"
}
