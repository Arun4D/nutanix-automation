module "nutanix_os_build" {
  source           = "./modules/nutanix_os_build"
  image_name       = var.image_name
  image_source_uri = var.image_source_uri
}

module "nutanix_vm" {
  source               = "./modules/nutanix_vm"
  cluster_name         = var.cluster_name
  vm_name              = "${var.env}-${var.vm_name}"
  subnet_name          = var.subnet_name
  num_vcpus_per_socket = var.num_vcpus_per_socket
  num_sockets          = var.num_sockets
  memory_size_mib      = var.memory_size_mib
  image_name           = module.nutanix_os_build.image_name
  admin_pub_key        = var.admin_pub_key
  
  depends_on           = [module.nutanix_os_build]
}
