from app.services.user_service import UserService
from app.services.message_service import MessageService


class MessageController:
    @staticmethod
    def send_message_to_all_users(message: str):
        try:
            users = UserService.get_users()
            for user in users:
                personalized_message  = message.format(name=user["name"])
                MessageService.send_message(personalized_message , user["phone_number"])
        except Exception as e:
            print(e)

    @staticmethod
    def send_message_by_user_email(user_email: str, message: str):
        try:
            user = UserService.get_user_by_email(user_email)
            message = message.format(name=user["name"])
            MessageService.send_message(message, user["phone_number"])
        except Exception as e:
            print(e)
