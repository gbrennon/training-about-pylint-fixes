"""Service implementations for user management."""

from core.ports import UserRepository
from core.user import User


class UserService:
    """Service class for managing users using the UserRepository interface."""
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: str) -> User:
        """Retrieve a user by ID."""
        return self.user_repository.read(user_id)

    def save_user(self, user: User) -> None:
        """Save (create or update) a user."""
        self.user_repository.save(user)

    def delete_user(self, user_id: str) -> None:
        """Delete a user by ID."""
        self.user_repository.delete(user_id)
