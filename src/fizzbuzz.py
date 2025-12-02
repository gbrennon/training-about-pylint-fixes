def fizzbuzz(n: int) -> str:
    """Return FizzBuzz solution for n."""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
