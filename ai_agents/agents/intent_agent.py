from .base import BaseAgent
from typing import Dict, Any

class IntentAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        message = context.get("message", "").lower()
        print("[Intent Agent] Parsing user intent from chat for Nutanix Platform...")
        
        # Natural Language heuristic proxying an LLM Intent Classifier
        if any(w in message for w in ["build", "provision", "create", "new", "deploy"]):
            intent = "PROVISION"
        elif any(w in message for w in ["patch", "update", "upgrade", "lcm"]):
            intent = "PATCH"
        elif any(w in message for w in ["scale", "expand", "grow", "add node"]):
            intent = "SCALE"
        elif any(w in message for w in ["offline", "alert", "broken", "fix", "issue", "remediate"]):
            intent = "REMEDIATE"
        else:
            intent = "UNKNOWN"
            
        context["intent"] = intent
        return context
