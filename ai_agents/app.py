from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from orchestrator import AIOpsOrchestrator

app = FastAPI(title="Nutanix AI Agent API", version="1.0.0")
orchestrator = AIOpsOrchestrator()

class ChatPayload(BaseModel):
    message: str

class EventPayload(BaseModel):
    event_id: str
    action_type: str
    resource: Dict[str, Any]

@app.post("/api/v1/chat")
async def chat_endpoint(payload: ChatPayload):
    """Entry point for the Multi-Agent Chat Interface."""
    result = orchestrator.process_chat(payload.message)
    return {
        "status": "success",
        "decision": result.get("decision"),
        "snow_ticket": result.get("snow_ticket"),
        "process_status": result.get("process_status"),
        "action_payload": result.get("action_payload")
    }

@app.post("/api/v1/event")
async def process_event(payload: EventPayload):
    # This endpoint receives generic events
    return {"status": "Event received", "event_id": payload.event_id}

@app.post("/api/v1/snow/webhook")
async def snow_webhook(payload: Dict[str, Any]):
    """Receives approval triggers from SNOW when a RITM/Change is approved."""
    event_type = payload.get("event")
    ticket_id = payload.get("ticket_id")
    action_payload = payload.get("action_payload", {})
    
    if event_type in ["RITM_APPROVED", "CHG_APPROVED"]:
        result = orchestrator.process_webhook_approval(ticket_id, action_payload)
        return {"status": "Execution Initiated", "execution_state": result.get("execution_status")}
        
    raise HTTPException(status_code=400, detail="Unknown SNOW Event")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
