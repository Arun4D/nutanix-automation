#!/usr/bin/env python3
import os
import sys
import requests
import json

def update_cmdb(vm_name, state):
    snow_url = os.environ.get("SNOW_INSTANCE_URL")
    user = os.environ.get("SNOW_USER")
    password = os.environ.get("SNOW_PASSWORD")
    
    if not all([snow_url, user, password]):
        print("Required SNOW credentials not found in environment, skipping SNOW update.")
        sys.exit(0)
        
    url = f"{snow_url}/api/now/table/cmdb_ci_vm_instance"
    payload = {
        "name": vm_name,
        "install_status": 1 if state == "SUCCESS" else 4,
        "u_cluster_name": "nutanix-ahv-cluster"
    }
    
    response = requests.post(
        url, 
        auth=(user, password), 
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        data=json.dumps(payload)
    )
    
    if response.status_code in [200, 201]:
        print(f"Successfully updated CMDB for {vm_name}. SysID: {response.json().get('result', {}).get('sys_id')}")
    else:
        print(f"Failed to update CMDB: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: snow_updater.py <vm_name> <status>")
        sys.exit(1)
        
    update_cmdb(sys.argv[1], sys.argv[2])
