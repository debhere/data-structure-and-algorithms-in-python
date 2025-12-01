def isSubsequence(s: str, t: str) -> bool:
    """This problem is about find if given two strings s and t, s is a subsequence of t.

    A subsequence of a string is a new string that is formed from the original string by deleting some
    (can be none) of the characters without disturbing the relative positions of the remaining characters.

    Args:
        s(str): The sequence to check.
        t(str): The string where the sequence needs to be checked.

    Returns:
        bool: True if sequence can be found with t else False
    """
    idx = 0
    for letter in t:
        if idx == len(s):
            return True
        if letter == s[idx]:
            idx += 1
    return idx == len(s)


if __name__ == "__main__":
    print(isSubsequence("abc", "ahbgdc"))
    print(isSubsequence("axc", "ahbgdc"))
    print(isSubsequence("ab", "baab"))
    print(isSubsequence("bac", "ababc"))
    print(isSubsequence("ab", "abbbb"))
    print(isSubsequence("acb", "ahbgdc"))
