from enum import Enum
from typing import Optional


class Result(Enum):
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    FIZZBUZZ = "FizzBuzz"


def evaluate(n: int) -> Optional[Result]:
    """Determine the appropriate FizzBuzz result for n."""
    if n % 15 == 0:
        return Result.FIZZBUZZ
    elif n % 3 == 0:
        return Result.FIZZ
    elif n % 5 == 0:
        return Result.BUZZ
    else:
        return None


def fizzbuzz(n: int) -> str:
    result = evaluate(n)
    return result.value if result is not None else str(n)
