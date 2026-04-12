env           = "prod"
cluster_name  = "foundation-cluster"
cluster_ip    = "10.0.2.100"
ahv_image_url = "http://web.local/ahv.tar"
cvm_ip_pool   = ["10.0.2.101", "10.0.2.102", "10.0.2.103"]
hypervisor_ip_pool = ["10.0.2.111", "10.0.2.112", "10.0.2.113"]
ipmi_ip_pool  = ["10.0.2.121", "10.0.2.122", "10.0.2.123"]
nodes = [
  { mac_address = "FF:BB:CC:DD:EE:01" },
  { mac_address = "FF:BB:CC:DD:EE:02" },
  { mac_address = "FF:BB:CC:DD:EE:03" }
]
