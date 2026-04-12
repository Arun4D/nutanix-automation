variable "cluster_name" {}
variable "cluster_ip" {}
variable "ahv_image_url" {}
variable "cvm_ip_pool" { type = list(string) }
variable "hypervisor_ip_pool" { type = list(string) }
variable "ipmi_ip_pool" { type = list(string) }
variable "nodes" {
  type = list(object({
    mac_address = string
  }))
}
