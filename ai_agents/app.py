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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
