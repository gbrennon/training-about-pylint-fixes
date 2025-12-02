"""Module to run FizzBuzz implementation."""

from .domain.service import FizzBuzzService  # pylint: disable=no-name-in-module


def fizzbuzz(n: int) -> str:
    """Return FizzBuzz result for n."""
    service_result = FizzBuzzService.execute(n)
    return service_result.value if service_result is not None else str(n)


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
