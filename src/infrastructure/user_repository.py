"""Infrastructure for user repository implementation."""

import json
import os
from core.ports import UserRepository
from core.user import User


class JsonUserRepository(UserRepository):
    """User repository implementation using JSON file storage."""
    def __init__(self, db_path="data/database.json"):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Create the database file with an empty list if it doesn't exist."""
        dir_path = os.path.dirname(self.db_path)
        os.makedirs(dir_path, exist_ok=True)
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _read_db(self):
        """Read the current state of the database."""
        with open(self.db_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write_db(self, data):
        """Write the updated state back to the database."""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def read(self, user_id: str) -> User:
        """Retrieve a user by ID."""
        db = self._read_db()
        for user_dict in db:
            if user_dict['id'] == user_id:
                return User(
                    user_id=user_dict['id'],
                    name=user_dict.get('name'),
                    email=user_dict.get('email')
                )
        raise ValueError(f"User {user_id} not found")

    def delete(self, user_id: str) -> None:
        """Delete a user by ID."""
        db = self._read_db()
        db = [user for user in db if user['id'] != user_id]
        self._write_db(db)

    def save(self, user: User) -> None:
        """Upsert (insert or update) a user."""
        db = self._read_db()
        user_dict = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        found = False
        for idx, existing_user in enumerate(db):
            if existing_user['id'] == user.id:
                db[idx] = user_dict
                found = True
                break
        if not found:
            db.append(user_dict)
        self._write_db(db)
