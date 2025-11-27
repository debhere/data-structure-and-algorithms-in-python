from typing import List


def reverseVowels(s: str) -> str:
    """This is a LeetCode problem but a comparatively easy one. Here we need to reverse the vowels and the vowels
    can be of any case. So I have created a list of the vowels that exist in the passing string. Then replace the
    letter with the vowel and put everything in a new string.

    Args:
        s(string): A string
    Returns:
        str: A string where the vowels arr in reverse order compared to the original string.
    """
    vowels: List[str] = [v for v in s if v.lower() in 'aeiou']

    new_s = ''

    for l in s:
        if l.lower() in 'aeiou':
            letter = vowels.pop()
        else:
            letter = l
        new_s += letter

    return new_s


if __name__ == "__main__":
    print(reverseVowels("IcecreAm"))
    print(reverseVowels("leetcode"))
