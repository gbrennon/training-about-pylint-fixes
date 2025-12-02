"""User model for the application."""

from typing import Optional


class User:  # pylint: disable=too-few-public-methods
    """Represent a user in the system."""
    def __init__(self, user_id: str, name: Optional[str] = None, email: Optional[str] = None):
        self.id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
