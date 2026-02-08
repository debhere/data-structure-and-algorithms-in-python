def isPowerOfFour(n: int) -> bool:
    """Given an integer n, return true if it is a power of four. Otherwise, return false. An integer n
    is a power of four, if there exists an integer x such that n == 4x.

    Args:
        n: an integer.

    Returns:
        bool: True if the input is a power of 4 else False.

    """
    if n == 1:
        return True
    elif n % 4 != 0 or n < 4:
        return False
    else:
        return isPowerOfFour(n // 4)


if __name__ == "__main__":
    print(isPowerOfFour(16))
    print(isPowerOfFour(24))
