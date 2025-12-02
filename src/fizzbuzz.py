from domain.service import FizzBuzzService
from domain.result import Result


def fizzbuzz(n: int) -> str:
    service_result = FizzBuzzService.execute(n)
    return service_result.value if service_result is not None else str(n)


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
