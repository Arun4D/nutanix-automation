from .base import BaseAgent
from typing import Dict, Any

class ExecutionAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        # This agent usually wakes up via webhook
        print("[Execution Agent] Initiating Infrastructure Orchestration...")
        
        status = context.get("process_status")
        ticket = context.get("snow_ticket")
        payload = context.get("action_payload", {})
        
        if status not in ["AUTO_APPROVED", "WEBHOOK_APPROVED"]:
            print("  -> Execution blocked by governance.")
            return context
            
        print(f"  -> Dispatching {payload.get('action_type')} to GitHub Actions under ticket {ticket}...")
        
        # (Mocking actual request to GH Actions API)
        
        context["execution_status"] = "DISPATCHED"
        return context
