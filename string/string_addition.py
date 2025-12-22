def addStrings(num1: str, num2: str) -> str:
    """
    Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and
    num2 as a string.

    The approach is to get the digit with the ordinal value and accordingly perform the addition. Using
    default int() function is not recommended.

    Args:
        num1: first number in string.
        num2: second number in string.

    Return:
        str: addition of the input params in string.
    """
    res: int = 0
    if num1 == '0' and num2 != '0':
        return num2
    elif num1 != '0' and num2 == '0':
        return num1
    elif num1 == '0' and num2 == '0':
        return '0'
    else:
        for i, d in enumerate(num1[::-1]):
            digit = ord(d) - ord('0')
            res += (10 ** i) * digit

        for i, d in enumerate(num2[::-1]):
            digit = ord(d) - ord('0')
            res += (10 ** i) * digit

    return str(res)


if __name__ == "__main__":
    print(addStrings('11', '123'))
    print(addStrings('456', '77'))
    print(addStrings('0', '0'))
