def isPowerofTwo(n: int) -> bool:
    """Given an integer n, return true if it is a power of two. Otherwise, return false.

    Args:
         n: int, input

    Returns:
        bool: True if power of 2 else False.
    """
    if n == 1:
        return True
    elif n % 2 != 0:
        return False
    else:
        return isPowerofTwo(n//2)


if __name__ == "__main__":
    print(isPowerofTwo(1))
    print(isPowerofTwo(8))
    print(isPowerofTwo(24))
    print(isPowerofTwo(128))