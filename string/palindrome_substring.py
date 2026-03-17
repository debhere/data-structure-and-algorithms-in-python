def longestPalindrome(s: str) -> str:
    """Given a string s, return the longest palindromic substring in s.

    There is specifically two case of this problem when the palindrome is even and when the palindrome
    is odd.

    A two-pointer approach has been taken where the pointer initialization varies depending upon the type
    of palindrome.

    Args:
        s: The input string.

    Returns:
        str: The longest palindrome substring exists within the input string.
    """
    n = len(s)
    res = ''

    for i in range(n):
        tmp = expand(s, i, i)
        if len(tmp) > len(res):
            res = tmp

        tmp = expand(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp

    return res


def expand(s, start, end):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    temp = s[start + 1: end]
    return temp


if __name__ == "__main__":
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("ac"))
    print(longestPalindrome("abb"))
