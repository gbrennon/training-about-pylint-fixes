"""Composition root for wiring dependencies."""

from infrastructure.user_repository import JsonUserRepository
from core.services import UserService

# Wire dependencies
user_repository = JsonUserRepository()
user_service = UserService(user_repository)
