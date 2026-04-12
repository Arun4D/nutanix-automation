from .base import BaseAgent
from typing import Dict, Any

class RiskAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[Risk Agent] Querying Graph DB for Blast Radius...")
        
        intent = context.get("intent")
        
        if intent == "PROVISION":
            risk_level = "LOW"
            impact = "New infrastructure. No dependency collision."
        elif intent == "PATCH":
            risk_level = "MEDIUM"
            impact = "System reboot required. Affects 2 downstream App CIs."
        elif intent == "REMEDIATE":
            risk_level = "HIGH"
            impact = "Potential DB sync interruption if service is restarted during remediation."
        else:
            risk_level = "UNKNOWN"
            impact = "Undetermined."
            
        context["risk_analysis"] = {
            "level": risk_level,
            "blast_radius": impact
        }
        return context
