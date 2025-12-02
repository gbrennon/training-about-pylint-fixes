from typing import Optional
from .result import Result


class FizzBuzzService:
    @staticmethod
    def execute(n: int) -> Optional[Result]:
        """Determine the appropriate FizzBuzz result for n."""
        if n % 15 == 0:
            return Result.FIZZBUZZ
        elif n % 3 == 0:
            return Result.FIZZ
        elif n % 5 == 0:
            return Result.BUZZ
        else:
            return None
