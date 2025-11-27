from typing import List


def firstUniqCharBruteForce(s: str) -> int:
    i = 0
    if len(s) == 1:
        return i
    repeats: List[str] = list()
    while i < len(s):
        j = i + 1
        if s[i] not in s[j:] and s[i] not in repeats:
            return i
        else:
            repeats.append(s[i])
            i += 1

    return -1


def firstUniqChar(s: str) -> int:
    """To find the first unique character of a given string. The brute force solution above is taking
    more time to execute whereas this solution is a better option.

    Args:
        s (str): A sample string

    Returns:
        int: The index of the first unique character or -1 if no unique character is present.
    """
    set_s = set(s)
    current = len(s) + 1

    for char in set_s:
        first = s.index(char)
        last = s.rindex(char)

        if first == last:
            current = min(current, first)

    return -1 if current == len(s) + 1 else current


if __name__ == "__main__":
    print(firstUniqCharBruteForce("leetcode"))
    print(firstUniqCharBruteForce("loveleetcode"))
    print(firstUniqCharBruteForce("aabb"))
    print(firstUniqCharBruteForce("dddccdbba"))
    print()
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aabb"))
    print(firstUniqChar("dddccdbba"))
