from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_users(limit: int = None):
        return UserRepository.get_users(limit)

    @staticmethod
    def get_user_by_email(user_email: str):
        return UserRepository.get_user_by_email(user_email)

    @staticmethod
    def get_user_by_phone_number(user_phone_number: str):
        return UserRepository.get_user_by_phone_number(user_phone_number)

    @staticmethod
    def get_users_by_email_list(email_list: list[str]):
        return UserRepository.get_users_by_email_list(email_list)

    @staticmethod
    def insert_user(user_data: dict[str, str]) -> dict[str, str] | None:
        return UserRepository.insert_user(user_data)