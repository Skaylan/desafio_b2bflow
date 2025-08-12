from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_users(limit: int = None):
        return UserRepository.get_users(limit)