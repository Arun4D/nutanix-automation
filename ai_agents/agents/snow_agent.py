class ServiceNowAgent:
    def __init__(self, instance_url, token):
        self.instance_url = instance_url
        self.token = token

    def create_change(self, details: dict) -> str:
        """Create an emergency change ticket in ServiceNow."""
        print(f"Creating SNOW ticket with {details}")
        return "CHG001234"
