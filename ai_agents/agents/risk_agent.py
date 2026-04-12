class RiskAgent:
    def __init__(self, graph_client):
        self.graph_client = graph_client

    def evaluate_risk(self, resource_id: str) -> dict:
        """Evaluate risk of an operation on a resource by looking up graph dependencies."""
        dependencies = self.graph_client.get_dependencies(resource_id)
        if len(dependencies) > 5:
            return {"level": "HIGH", "reason": "Many dependencies found"}
        return {"level": "LOW", "reason": "Few dependencies"}
