import json
import os
from src.ports import UserRepository

class JsonUserRepository(UserRepository):
    def __init__(self, db_path="data/database.json"):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Create the database file with an empty list if it doesn't exist."""
        dir_path = os.path.dirname(self.db_path)
        os.makedirs(dir_path, exist_ok=True)
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump([], f)

    def _read_db(self):
        """Read the current state of the database."""
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        """Write the updated state back to the database."""
        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=4)

    def read(self, user_id: str) -> dict:
        """Retrieve a user by ID."""
        db = self._read_db()
        for user in db:
            if user['id'] == user_id:
                return user
        return {}  # Return empty dict if user not found

    def delete(self, user_id: str) -> None:
        """Delete a user by ID."""
        db = self._read_db()
        db = [user for user in db if user['id'] != user_id]
        self._write_db(db)

    def save(self, user: dict) -> None:
        """Upsert (insert or update) a user."""
        db = self._read_db()
        found = False
        for idx, existing_user in enumerate(db):
            if existing_user['id'] == user['id']:
                db[idx] = user
                found = True
                break
        if not found:
            db.append(user)
        self._write_db(db)
