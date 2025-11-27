from typing import List


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """This is a LeetCode problem which is given two strings ransomNote and magazine, return true if
    ransomNote can be constructed by using the letters from magazine and false otherwise. Each letter in
    magazine can only be used once in ransomNote.

    The approach is simple i.e., check if a letter exist in magazine, if not return false else replace
    the letter by a blank space.

    Args:
        ransomNote (str): String to be checked.
        magazine (str): String to be checked against.

    Returns:
        bool: True if ransomNote cam be constructed with magazine else False.
    """
    isPossible = False
    # mList: List[str] = list(magazine)
    #
    # for r in ransomeNote:
    #     if r in mList:
    #         mList.remove(r)
    #         isPossible = True
    #     else:
    #         isPossible = False
    #         break

    for r in ransomNote:
        if r in magazine:
            magazine = magazine.replace(r, '', 1)
            isPossible = True
        else:
            isPossible = False
            break

    return isPossible


if __name__ == "__main__":
    print(canConstruct("aa", 'b'))
    print(canConstruct("aa", 'aab'))
    print(canConstruct("aa", 'ab'))
