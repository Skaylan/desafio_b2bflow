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