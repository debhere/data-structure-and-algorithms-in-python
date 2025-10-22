from typing import Any


def fibonacci_sum(n: int, memo=None) -> int:
    if memo is None:
        memo: dict = {}
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_sum(n - 1, memo) + fibonacci_sum(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fibonacci_sum(8))
    print(fibonacci_sum(10))
    print(fibonacci_sum(50))
