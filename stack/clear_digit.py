def clearDigits(s: str) -> str:
    """You are given a string s.

    Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left. Return the resulting
    string after removing all digits.

    Args:
        s: string, input string

    Returns:
        string: Return the resulting string after removing digit and left adjacent.

    """
    stack = list(s)

    for e in s:
        if e.isdigit():
            idx = stack.index(e)
            stack.remove(e)
            if idx > 0:
                stack.pop(idx - 1)

    return ''.join(stack)


if __name__ == "__main__":
    print(clearDigits("abc"))
    print(clearDigits("cb34"))
