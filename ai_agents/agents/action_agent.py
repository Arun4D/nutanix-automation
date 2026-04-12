from .base import BaseAgent
from typing import Dict, Any

class ActionAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[Action Agent] Assembling automation payload parameters...")
        
        intent = context.get("intent")
        
        # This agent maps intent to GH Actions payload structures
        payload = {}
        if intent == "PROVISION":
            payload = {
                "action_type": "day1_provision",
                "vm_name": "ai-deployed-vm-01",
                "cpu": 2,
                "memory": 4096
            }
        elif intent == "PATCH":
            payload = {
                "action_type": "day2_patch",
                "target": "all"
            }
        elif intent == "REMEDIATE":
            payload = {
                "action_type": "day2_remediate",
                "target": "alerting-nodes",
                "playbook": "restart_services"
            }
            
        context["action_payload"] = payload
        return context
