def factorial(n):
    return n if n in [0, 1] else n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(10))
    print(factorial(7))
    print(factorial(6))