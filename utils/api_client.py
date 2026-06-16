import requests
from config.settings import BASE_URL

class APIClient:

    def post(self, endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}", json=payload)