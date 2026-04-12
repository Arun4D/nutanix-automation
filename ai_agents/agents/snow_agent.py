from .base import BaseAgent
from typing import Dict, Any
import uuid

class SnowAgent(BaseAgent):
    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print("[ServiceNow Agent] Halting execution to enforce governance...")
        
        intent = context.get("intent")
        decision = context.get("decision", {}).get("status")
        
        ticket_id = f"CHG{str(uuid.uuid4().int)[:7]}"
        
        if intent == "PROVISION":
            ticket_id = f"RITM{str(uuid.uuid4().int)[:7]}"
            
        print(f"  -> Simulated Lodging of Ticket {ticket_id} to ServiceNow API.")
        
        context["snow_ticket"] = ticket_id
        
        # IF IT REQUIRES REVIEW, WE HALT THE PROCESS UNTIL WEBHOOK RETURNS
        if decision == "REQUIRE_MANUAL_REVIEW":
            context["process_status"] = "PENDING_APPROVAL"
            print("  -> System sleeping... awaiting SNOW Webhook approval.")
        else:
            context["process_status"] = "AUTO_APPROVED"
            print(f"  -> Ticket {ticket_id} matches Pre-Approved Standard Change Rules.")
            
        return context
