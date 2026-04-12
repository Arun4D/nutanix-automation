class Neo4jClient:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password

    def get_dependencies(self, node_id: str) -> list:
        """Stub for cypher query fetching dependencies."""
        return ["App1", "App2"]
