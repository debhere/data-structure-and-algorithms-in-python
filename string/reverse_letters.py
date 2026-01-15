
def reverseOnlyLetters(s: str) -> str:
    front = 0
    rear = len(s) - 1
    res: str = ''

    if not any(c.isalpha() for c in s):
        return s

    while rear >= 0 or front < len(s):
        if len(s) == len(res):
            break
        elif not s[front].isalpha():
            res += s[front]
            front += 1
        elif not s[rear].isalpha():
            rear -= 1
        else:
            res += s[rear]
            front += 1
            rear -= 1

    return res


def optimumSolution(s: str) -> str:
    """Given a string s, reverse the string according to the following rules:
    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.
    Return s after reversing it.

    Args:
        s: string, the input of the string

    Returns:
        string: String where only the letter position is reversed.
    """
    s = list(s)
    stack = [c for c in s if c.isalpha()]
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = stack.pop()

    return ''.join(s)


if __name__ == "__main__":
    print(reverseOnlyLetters("ab-cd"))
    print(reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
    print(reverseOnlyLetters("-"))
    print(reverseOnlyLetters("7_28]"))
    print(reverseOnlyLetters(";1yDV"))

    print()

    print(optimumSolution("ab-cd"))
    print(optimumSolution("a-bC-dEf-ghIj"))
    print(optimumSolution("Test1ng-Leet=code-Q!"))
    print(optimumSolution("-"))
    print(optimumSolution("7_28]"))
    print(optimumSolution(";1yDV"))

