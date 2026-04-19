from .base import BaseAgent
from typing import Dict, Any

class DecisionAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[Decision Agent] Synthesizing context to determine next steps...")
        
        intent = context.get("intent")
        risk = context.get("risk_analysis", {}).get("level", "HIGH")
        cluster_data = context.get("cluster_data", {})
        
        # Example: check if there's enough capacity for provision
        memory_capacity = cluster_data.get("memory_capacity_bytes", 1)
        memory_usage = cluster_data.get("memory_usage_bytes", 0)
        memory_usage_percent = (memory_usage / memory_capacity) * 100
        
        if intent == "PROVISION":
            if memory_usage_percent > 85:
                decision = "REQUIRE_MANUAL_REVIEW"
                reasoning = f"Cluster memory usage is high ({memory_usage_percent:.1f}%). Requires review before provisioning."
            else:
                decision = "APPROVED_FOR_ACTION"
                reasoning = "Standard request, low risk footprint, cluster has sufficient capacity."
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
