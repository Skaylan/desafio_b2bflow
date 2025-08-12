from app.ZApi import zapi_client

class MessageService:
    @staticmethod
    def send_message(message: str, number: str) -> None:
        return zapi_client.send_message(message, number)