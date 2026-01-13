
def detectCapitalUse(word: str) -> bool:
    """We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Given a string word, return true if the usage of capitals in it is right.

    Args:
        word(str): Input string

    Returns:
        bool: Returns True if usage is correct.
    """
    isCorrect: bool = False

    if word.istitle():
        isCorrect = True
    elif word.isupper():
        isCorrect = True
    elif word.islower():
        isCorrect = True

    return isCorrect


if __name__ == "__main__":
    print(detectCapitalUse("USA"))
    print(detectCapitalUse("FlaG"))
    print(detectCapitalUse("g"))