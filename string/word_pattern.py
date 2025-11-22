from typing import List


def wordPattern(pattern: str, s: str) -> bool:
    """This is a LeetCode problem to check if the string is following the pattern. i) Each letter in pattern maps to exactly one unique
    word in s. ii) Each unique word in s maps to exactly one letter in pattern. iii) No two letters map to the same word, and no two words map
    to the same letter.

    Args:
        pattern (str): The pattern that the string follows.
        s (str): Given string to check.

    Returns:
        bool: Whether the string follows the pattern or not.
    """
    isMatched: bool = True
    words: List[str] = s.split()
    pcount = {}
    if len(set(words)) != len(set(pattern)) or len(pattern) != len(words):
        return False
    for p, w in zip(pattern, words):
        if pcount.get(p, '') == '' and w not in pcount.values():
            pcount[p] = w
        elif pcount.get(p) != w:
            return False
        elif pcount.get(p) == w:
            isMatched = True
    return isMatched


if __name__ == "__main__":
    print(wordPattern("abba", "dog cat cat fish"))
    print(wordPattern("abab", "dog cat cat dog"))
    print(wordPattern("abba", "dog cat cat dog"))
    print(wordPattern("abba", "dog dog dog dog"))
