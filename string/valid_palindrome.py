def validPalindromeBruteForce(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        for i, ele in enumerate(s):
            temp = s[:i] + s[i:].replace(ele, '', 1)
            if temp == temp[::-1]:
                return True
    return False


def validPalindrome(s: str) -> bool:
    """Given a string s, return true if the s can be palindrome after deleting at most one character
    from it.

    Args:
        s: str, given string.

    Returns:
        bool: True if the string is palindrome after deleting at most one character.
    """
    if s == s[::-1]:
        return True
    else:
        n = len(s)
        front, rear = 0, n - 1
        i = 0
        while front != rear and i <= 2:
            if s[front] == s[rear]:
                front += 1
                rear -= 1
            else:
                i += 1
                temp = s[:front] + s[front:].replace(s[front], '', 1)
                if temp == temp[::-1]:
                    return True
                else:
                    temp = s[:rear] + s[rear:].replace(s[rear], '', 1)
                    if temp == temp[::-1]:
                        return True

    return False


def attempt():
    l = ['d', 'e', 'm']
    l1 = ['m', 'e', 'd']





if __name__ == "__main__":
    print(validPalindrome("aba"))
    print(validPalindrome("abca"))
    print(validPalindrome("pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"))