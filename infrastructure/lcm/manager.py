#!/usr/bin/env python3
import requests
import json
import os
import sys

class LCMManager:
    def __init__(self, prism_ip, username, password):
        self.base_url = f"https://{prism_ip}:9440/api/nutanix/v3"
        self.auth = (username, password)
        requests.packages.urllib3.disable_warnings()

    def _post(self, endpoint, payload):
        resp = requests.post(
            f"{self.base_url}/{endpoint}", 
            auth=self.auth, 
            json=payload, 
            verify=False
        )
        resp.raise_for_status()
        return resp.json()

    def perform_inventory(self):
        """Triggers local LCM inventory."""
        print("Triggering LCM Inventory task...")
        payload = {"spec": {}} 
        try:
            task = self._post("lcm/inventory", payload)
            print(f"Inventory Task UUID: {task.get('task_uuid')}")
        except Exception as e:
            print(f"Inventory failed: {str(e)}")

    def apply_updates(self):
        """Triggers Rolling Updates."""
        print("Executing rolling HW/AOS cluster updates...")
        payload = {"spec": {}} 
        try:
            task = self._post("lcm/update", payload)
            print(f"Update Task UUID: {task.get('task_uuid')}")
        except Exception as e:
            print(f"Update failed: {str(e)}")

if __name__ == "__main__":
    prism_ip = os.environ.get("PRISM_IP")
    if not prism_ip:
        print("Missing PRISM_IP env var.")
        sys.exit(1)
        
    manager = LCMManager(prism_ip, "admin", "password")
    
    if len(sys.argv) > 1 and sys.argv[1] == "inventory":
        manager.perform_inventory()
    elif len(sys.argv) > 1 and sys.argv[1] == "update":
        manager.apply_updates()
    else:
        print("Usage: manager.py [inventory|update]")
