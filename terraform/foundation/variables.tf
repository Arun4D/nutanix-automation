variable "env" { type = string }
variable "cluster_name" { type = string }
variable "cluster_ip" { type = string }
variable "ahv_image_url" { type = string }
variable "cvm_ip_pool" { type = list(string) }
variable "hypervisor_ip_pool" { type = list(string) }
variable "ipmi_ip_pool" { type = list(string) }
variable "nodes" {
  type = list(object({
    mac_address = string
  }))
}
