def isPowerOfThree(n: int) -> bool:
    """Given an integer n, return true if it is a power of three. Otherwise, return false.

    Args:
        n: input number.

    Returns:
        bool: True if power of three otherwise False.
    """
    if n == 1:
        return True
    elif n == 0 or n % 3 != 0:
        return False
    else:
        return isPowerOfThree(n // 3)


if __name__ == "__main__":
    print(isPowerOfThree(27))
    print(isPowerOfThree(21))
