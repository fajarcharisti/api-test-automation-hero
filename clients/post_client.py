from utils.api_client import APIClient
from config.paths import POST_ENDPOINT_PATH

class PostClient:
    def __init__(self):
        self.client = APIClient()

    def create_post(self, payload):
        return self.client.post(POST_ENDPOINT_PATH, payload)