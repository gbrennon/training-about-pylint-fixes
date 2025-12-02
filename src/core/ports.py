"""Protocol definitions for user repository."""

from typing import Protocol
from .user import User


class UserRepository(Protocol):
    """Protocol for user repository operations."""

    def read(self, user_id: str) -> User:
        """Read a user by ID."""
        raise NotImplementedError("Method must be implemented")

    def delete(self, user_id: str) -> None:
        """Delete a user by ID."""

    def save(self, user: User) -> None:
        """Save (upsert) a user."""
