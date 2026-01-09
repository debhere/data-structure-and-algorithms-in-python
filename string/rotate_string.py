def rotateString(s: str, goal: str) -> bool:
    """Given two strings s and goal, return true if and only if s can become goal after some number of
    shifts on s. A shift on s consists of moving the leftmost character of s to the rightmost position.

    Args:
        s: initial string
        goal: string formed after rotating s
    Returns:
        bool: True if goal can be achieved after rotation else False
    """
    s = list(s)
    goal = list(goal)

    for _ in s:
        letter = s.pop(0)
        s.append(letter)

        if s == goal:
            return True
    return False


if __name__ == "__main__":
    print(rotateString("abcde", "cdeab"))
    print(rotateString("abcde", "abced"))
    print(rotateString("defdefdefabcabc", "defdefabcabcdef"))
    print(rotateString("ohbrwzxvxe", "uornhegseo"))
    print(rotateString("bbbacddceeb", "ceebbbbacdd"))
