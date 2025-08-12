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

    @staticmethod
    def get_users_by_email_list(email_list: list[str]):

        """
        Gets a list of users from the database by email.

        Args:
            email_list (list[str]): A list of email addresses to retrieve

        Returns:
            list[dict[str, str]]: A list of dictionaries containing user information
        """
        return UserService.get_users_by_email_list(email_list)

    @staticmethod
    def insert_user(user_data: dict[str, str]) -> dict[str, str] | None:

        """
        Inserts a new user into the database.

        Args:
            user_data (dict[str, str]): A dictionary containing the user's information

        Returns:
            dict[str, str] | None: The inserted user's information, or None if the insertion failed
        """

        return UserService.insert_user(user_data)