# This is a memoization example
def fibonacci_memo(n: int, memo=None) -> int:
    if memo is None:
        memo: dict = {}
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dlist = [0] * (n + 1)
    dlist[0] = 0
    dlist[1] = 1

    for i in range(2, n+1):
        dlist[i] = dlist[i-2] + dlist[i-1]

    return dlist[n]


if __name__ == "__main__":
    print(fibonacci_memo(8))
    print(fibonacci_memo(10))
    print(fibonacci_memo(50))

    print(fibonacci_tabulation(8))
    print(fibonacci_tabulation(10))
    print(fibonacci_tabulation(50))
