import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ZApi:
    def __init__(self, instance_token: str, instance_id: str, z_api_security_token: str):
        self.instance_token = instance_token
        self.instance_id = instance_id
        self.z_api_security_token = z_api_security_token
        self.url = f'https://api.z-api.io/instances/{self.instance_id}/token/{self.instance_token}/send-text'

    def send_message(self, message: str, number: str):
        try:
            return requests.post(self.url, json={'message': message, 'phone': number}, headers={'client-token': self.z_api_security_token}).json()
        except Exception as e:
            print(e)


zapi_client = ZApi(os.getenv("Z_API_INSTANCE_TOKEN"), os.getenv("Z_API_INSTANCE_ID"), os.getenv("Z_API_INSTANCE_SECURITY_TOKEN"))