
def reverseOnlyLetters(s: str) -> str:
    # punctuations: str = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
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


if __name__ == "__main__":
    print(reverseOnlyLetters("ab-cd"))
    print(reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
    print(reverseOnlyLetters("-"))
    print(reverseOnlyLetters("7_28]"))
    print(reverseOnlyLetters(";1yDV"))


    # a = "d1a2$"
    # for i, l in enumerate(a):
    #     print(f"{i}: {l.isdigit()}")
    #     print(f"{i}: {l.isalpha()}")
