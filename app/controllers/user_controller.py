from app.services.user_service import UserService

class UserController:
    @staticmethod
    def get_users(limit: int = None):
        """
        Gets all users from the database.

        Args:
            limit (int): The number of records to return. If None, returns all records.

        Returns:
            list[dict[str, str]]: A list of dictionaries containing user information
        """

        return UserService.get_users(limit)

    @staticmethod
    def get_user_by_email(user_email: str):
        """
        Gets a user from the database by email.

        Args:
            user_email (str): The email of the user to retrieve

        Returns:
            dict[str, str]: A dictionary containing user information
        """

        return UserService.get_user_by_email(user_email)

    @staticmethod
    def get_user_by_phone_number(user_phone_number: str):
        """
        Gets a user from the database by phone number.

        Args:
            user_phone_number (str): The phone number of the user to retrieve

        Returns:
            dict[str, str]: A dictionary containing user information
        """

        return UserService.get_user_by_phone_number(user_phone_number)