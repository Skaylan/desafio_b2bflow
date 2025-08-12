from app.services.user_service import UserService
from app.services.message_service import MessageService


class MessageController:
    @staticmethod
    def send_message_to_all_users(message: str):

        """
        Sends a message to all users in the database.

        Args:
            message (str): A message with a {name} placeholder for the user's name.

        Returns:
            None
        """

        try:
            users = UserService.get_users()
            for user in users:
                personalized_message  = message.format(name=user["name"])
                MessageService.send_message(personalized_message , user["phone_number"])
        except Exception as e:
            print(e)

    @staticmethod
    def send_message_by_user_email(user_email: str, message: str):

        """
        Sends a message to a user by their email address.

        Args:
            user_email (str): The email address of the user to send the message to.
            message (str): A message with a {name} placeholder for the user's name.

        Returns:
            None
        """
        try:
            user = UserService.get_user_by_email(user_email)
            message = message.format(name=user["name"])
            MessageService.send_message(message, user["phone_number"])
        except Exception as e:
            print(e)

    @staticmethod
    def send_message_by_user_phone_number(user_phone_number: str, message: str):

        """
        Sends a message to a user by their phone number.

        Args:
            user_phone_number (str): The phone number of the user to send the message to.
            message (str): A message with a {name} placeholder for the user's name.

        Returns:
            None
        """

        try:
            user = UserService.get_user_by_phone_number(user_phone_number)
            message = message.format(name=user["name"])
            MessageService.send_message(message, user["phone_number"])
        except Exception as e:
            print(e)
