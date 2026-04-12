from typing import Dict, Any
from .agents.intent_agent import IntentAgent
from .agents.insight_agent import InsightAgent
from .agents.monitoring_agent import MonitoringAgent
from .agents.risk_agent import RiskAgent
from .agents.decision_agent import DecisionAgent
from .agents.action_agent import ActionAgent
from .agents.snow_agent import SnowAgent
from .agents.execution_agent import ExecutionAgent

class AIOpsOrchestrator:
    def __init__(self):
        # Instantiate the 8 Agent Nodes
        self.intent_agent = IntentAgent()
        self.insight_agent = InsightAgent()
        self.monitoring_agent = MonitoringAgent()
        self.risk_agent = RiskAgent()
        self.decision_agent = DecisionAgent()
        self.action_agent = ActionAgent()
        self.snow_agent = SnowAgent()
        self.execution_agent = ExecutionAgent()
        
    def process_chat(self, user_message: str) -> Dict[str, Any]:
        """Main synchronous pass-through for the chat layer until SNOW halts it."""
        context = {"message": user_message}
        
        print(f"\n--- Orchestrator Pipeline Start ---\nUser: {user_message}\n")
        
        # 1. Parsing intent
        context = self.intent_agent.process(context)
        
        # 2. Parallel data gathering (Mocked as sequential for now)
        context = self.insight_agent.process(context)
        context = self.monitoring_agent.process(context)
        context = self.risk_agent.process(context)
        
        # 3. Aggregation & Decision
        context = self.decision_agent.process(context)
        
        # 4. Form Action Payload
        context = self.action_agent.process(context)
        
        # 5. Governance Check (Halt Loop if not standard)
        context = self.snow_agent.process(context)
        
        # 6. Execute if Approved
        if context.get("process_status") == "AUTO_APPROVED":
            context = self.execution_agent.process(context)
            
        print("\n--- Orchestrator Pipeline End ---\n")
        return context
        
    def process_webhook_approval(self, snow_ticket: str, action_payload: Dict[str, Any]) -> Dict[str, Any]:
        """Entry point for asynchronous wakes from SNOW."""
        print(f"\n--- Orchestrator Woken By Webhook for {snow_ticket} ---\n")
        
        context = {
            "snow_ticket": snow_ticket,
            "action_payload": action_payload,
            "process_status": "WEBHOOK_APPROVED"
        }
        
        context = self.execution_agent.process(context)
        return context
