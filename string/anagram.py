def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i], 0) + 1
        t_map[t[i]] = t_map.get(t[i], 0) + 1

    return s_map == t_map


def isAnagramOptimum(s: str, t: str) -> bool:
    """Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Args:
        s: str, first string
        t: str, second string

    Returns:
        bool: True if anagram else False
    """
    if len(s) != len(t):
        return False

    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True


if __name__ == "__main__":
    print(isAnagram(s="anagram", t="nagaram"))
    print(isAnagramOptimum(s="anagram", t="nagaram"))
