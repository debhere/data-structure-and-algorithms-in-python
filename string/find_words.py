from typing import List


def findWords(words: List[str]) -> List[str]:
    """Given an array of strings words, return the words that can be typed using letters of the alphabet
    on only one row of American keyboard. Note that the strings are case-insensitive, both lower-cased
    and upper-cased of the same letter are treated as if they are at the same row.

    In American Keyboard, the first row contains "qwertyuiop", the second row "asdfghjkl" and the third row
    contains "zxcvbnm" letters.

    Args:
        words: List[str], A list of words.

    Returns:
        List[str]: A list of words which can created using only onw row otherwise return an empty list.
    """
    res: List[str] = []
    for word in words:
        if set("qwertyuiop").issuperset(set(word.lower())) or \
                set("asdfghjkl").issuperset(set(word.lower())) or \
                set("zxcvbnm").issuperset(set(word.lower())):
            res.append(word)

    return res


if __name__ == "__main__":
    print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(findWords(["adsdf","sfd"]))
