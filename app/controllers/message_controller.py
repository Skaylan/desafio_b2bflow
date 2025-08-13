from app.services.user_service import UserService
from app.services.message_service import MessageService
from app.utils import get_logger

logger = get_logger()

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
            logger.info("Enviando mensagem para todos os usuários")
            for user in users:
                personalized_message  = message.format(name=user["name"])
                MessageService.send_message(personalized_message , user["phone_number"])
                logger.info(f"Mensagem enviada para {user['name']} ({user['phone_number']})")
        except Exception as e:
            logger.exception("Erro ao enviar mensagem para todos os usuários")

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
        logger.info(f"Enviando mensagem para o usuário com e-mail: {user_email}")
        try:
            user = UserService.get_user_by_email(user_email)
            message = message.format(name=user["name"])
            MessageService.send_message(message, user["phone_number"])
            logger.info(f"Mensagem enviada para {user['name']} ({user['phone_number']})")
        except Exception as e:
            logger.exception(f"Erro ao enviar mensagem para o e-mail {user_email}")

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
        logger.info(f"Enviando mensagem para o número: {user_phone_number}")
        try:
            user = UserService.get_user_by_phone_number(user_phone_number)
            message = message.format(name=user["name"])
            MessageService.send_message(message, user["phone_number"])
            logger.info(f"Mensagem enviada para {user['name']} ({user['phone_number']})")
        except Exception as e:
            logger.exception(f"Erro ao enviar mensagem para o número {user_phone_number}")
