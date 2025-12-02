"""Service to evaluate FizzBuzz results."""

from typing import Optional
from .result import Result


class FizzBuzzService:  # pylint: disable=too-few-public-methods
    """Service class for FizzBuzz logic."""

    @staticmethod
    def execute(n: int) -> Optional[Result]:
        """Determine the appropriate FizzBuzz result for n."""
        if n % 15 == 0:
            return Result.FIZZBUZZ
        if n % 3 == 0:
            return Result.FIZZ
        if n % 5 == 0:
            return Result.BUZZ
        return None
