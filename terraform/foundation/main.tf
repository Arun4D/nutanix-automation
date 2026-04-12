module "foundation" {
  source             = "../modules/nutanix_foundation"
  cluster_name       = "${var.env}-${var.cluster_name}"
  cluster_ip         = var.cluster_ip
  ahv_image_url      = var.ahv_image_url
  cvm_ip_pool        = var.cvm_ip_pool
  hypervisor_ip_pool = var.hypervisor_ip_pool
  ipmi_ip_pool       = var.ipmi_ip_pool
  nodes              = var.nodes
}
