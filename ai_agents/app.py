from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Nutanix AI Agent API", version="1.0.0")

class EventPayload(BaseModel):
    event_id: str
    action_type: str
    resource: Dict[str, Any]

@app.post("/api/v1/event")
async def process_event(payload: EventPayload):
    # This endpoint receives events from SNOW or Alertmanager
    return {"status": "Event received", "event_id": payload.event_id}

@app.post("/api/v1/snow/webhook")
async def snow_webhook(payload: Dict[str, Any]):
    """Receives approval triggers from SNOW when a RITM/Change is approved."""
    event_type = payload.get("event")
    
    if event_type == "RITM_APPROVED":
        print(f"Triggering day1 provision for {payload.get('vm_name')}")
        return {"status": "Provisioning Initiated"}
    
    elif event_type == "CHG_APPROVED":
        print(f"Triggering day2 operations for {payload.get('target_ci')}")
        return {"status": "Operations Initiated"}
        
    raise HTTPException(status_code=400, detail="Unknown SNOW Event")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
