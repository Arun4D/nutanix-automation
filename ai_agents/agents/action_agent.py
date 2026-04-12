class ActionAgent:
    def formulate_payload(self, intent: str, resource: dict) -> dict:
        """Formulates the execution payload for GitHub Actions based on AI intent."""
        return {
            "event_type": "remediate_alert",
            "client_payload": {
                "action": "scale_up",
                "vm_name": resource.get("name")
            }
        }
