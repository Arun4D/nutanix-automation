env           = "dev"
cluster_name  = "foundation-cluster"
cluster_ip    = "10.0.1.100"
ahv_image_url = "http://web.local/ahv.tar"
cvm_ip_pool   = ["10.0.1.101", "10.0.1.102", "10.0.1.103"]
hypervisor_ip_pool = ["10.0.1.111", "10.0.1.112", "10.0.1.113"]
ipmi_ip_pool  = ["10.0.1.121", "10.0.1.122", "10.0.1.123"]
nodes = [
  { mac_address = "AA:BB:CC:DD:EE:01" },
  { mac_address = "AA:BB:CC:DD:EE:02" },
  { mac_address = "AA:BB:CC:DD:EE:03" }
]
