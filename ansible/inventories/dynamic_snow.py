#!/usr/bin/env python3
import json

def get_inventory():
    return {
        "_meta": {
            "hostvars": {}
        },
        "all": {
            "children": ["nutanix_vms"]
        },
        "nutanix_vms": {
            "hosts": ["placeholder_vm_from_snow"],
            "vars": {
                "ansible_user": "admin"
            }
        }
    }

if __name__ == "__main__":
    print(json.dumps(get_inventory(), indent=2))
