from .base import BaseAgent
from typing import Dict, Any

class ActionAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[Action Agent] Assembling automation payload parameters...")
        
        intent = context.get("intent")
        
        # This agent maps intent to GH Actions payload structures for Nutanix Automation
        payload = {}
        if intent == "PROVISION":
            payload = {
                "action_type": "day1_provision",
                "hypervisor": "AHV",
                "vm_name": "ai-deployed-vm-01",
                "vcpu": 2,
                "memory_gb": 4,
                "network": "vlan-100",
                "storage_container": "default-container-123",
                "image": "RHEL_8_Gold"
            }
        elif intent == "PATCH":
            payload = {
                "action_type": "day2_patch",
                "target": "all_ahv_nodes",
                "lcm_update": True
            }
        elif intent == "REMEDIATE":
            payload = {
                "action_type": "day2_remediate",
                "target": "alerting-vms",
                "playbook": "restart_services"
            }
            
        context["action_payload"] = payload
        return context
