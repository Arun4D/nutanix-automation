from .base import BaseAgent
from typing import Dict, Any

class DecisionAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[Decision Agent] Synthesizing context to determine next steps...")
        
        intent = context.get("intent")
        risk = context.get("risk_analysis", {}).get("level", "HIGH")
        
        if intent == "PROVISION":
            decision = "APPROVED_FOR_ACTION"
            reasoning = "Standard request, low risk footprint."
        elif intent == "PATCH" or intent == "REMEDIATE":
            if risk == "HIGH":
                decision = "REQUIRE_MANUAL_REVIEW"
                reasoning = "High risk detected. Proceeding to lodge explicit Change Request in SNOW for board review."
            else:
                decision = "APPROVED_FOR_ACTION"
                reasoning = "Acceptable risk profile. Lodging Standard Change in SNOW."
        else:
            decision = "HALT"
            reasoning = "Could not parse safe intention."
            
        context["decision"] = {
            "status": decision,
            "reasoning": reasoning
        }
        return context
