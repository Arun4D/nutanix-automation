from .base import BaseAgent
from typing import Dict, Any

class MonitoringAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[Monitoring Agent] Fetching real-time Prometheus / Prism metrics...")
        
        intent = context.get("intent")
        
        # Proxying Alertmanager / Grafana API states
        if intent == "REMEDIATE" or context.get("target_vm"):
            context["monitoring_data"] = {
                "active_alerts": ["HostMemoryHigh", "ServiceDown"],
                "health_score": 45,
                "cpu_utilization": "92%",
                "status": "CRITICAL"
            }
        else:
            context["monitoring_data"] = {
                "active_alerts": [],
                "health_score": 100,
                "cpu_utilization": "15%",
                "status": "OK"
            }
            
        return context
