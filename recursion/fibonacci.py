def fib(n: int) -> int:
    """The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1.

    Args:
        n: int, number of terms in the sequence.

    Returns:
        int: summation of prev two numbers in the sequence.
    """
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(3))
    print(fib(4))
    print(fib(20))
