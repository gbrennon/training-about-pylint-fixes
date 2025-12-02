from typing import Protocol, List

class UserRepository(Protocol):
    def read(self, user_id: str) -> dict:
        ...

    def delete(self, user_id: str) -> None:
        ...

    def save(self, user: dict) -> None:
        ...
