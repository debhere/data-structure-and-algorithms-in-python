import string


def isPalindrome(s: str) -> bool:
    """This is a famous LeetCode problem. So the approach is to get the punctuations i.e., all the
    non-alphanumeric characters. Using maketrans() method, I have created the replacement table and
    then translate() method helps me to make the changes and save into a new string.

    In the end, compare both the translated string and the reversed translated string in lower case to
    check if both are identical.

    Args:
        s(str): input string

    Returns:
        bool: If the given string is a palindrome.
    """
    punctuations = string.punctuation + " "
    new_s = s.translate(s.maketrans('', '', punctuations))
    return new_s.lower() == new_s[::-1].lower()


if __name__ == "__main__":
    print(isPalindrome("race a car"))
    print(isPalindrome("A man, a plan, a canal: Panama"))
