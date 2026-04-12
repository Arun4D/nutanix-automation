import requests
import json

class ServiceNowAgent:
    def __init__(self, instance_url, user, password):
        self.instance_url = instance_url
        self.auth = (user, password)
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def _post(self, table, payload):
        url = f"{self.instance_url}/api/now/table/{table}"
        response = requests.post(url, auth=self.auth, headers=self.headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json().get('result', {})

    def create_change(self, details: dict) -> str:
        """Create an emergency change ticket in ServiceNow."""
        payload = {
            "short_description": details.get("description", "Automated AI Remediation"),
            "type": "emergency",
            "state": "Implement"
        }
        result = self._post("change_request", payload)
        return result.get('number', "CHG0000000")

    def create_ritm(self, details: dict) -> str:
        """Stub for creating a Request Item for Day 0 build."""
        payload = {
            "short_description": f"Provision VM {details.get('vm_name')}",
            "cat_item": "provision_vm_catalog_id"
        }
        result = self._post("sc_req_item", payload)
        return result.get('number', "RITM0000000")

    def log_activity(self, resource_id: str, action: str):
        """Log to the custom activity table."""
        payload = {
            "u_ci_sys_id": resource_id,
            "u_action_type": action,
            "u_trigger_source": "AI_Agent"
        }
        return self._post("u_lifecycle_activity", payload)
