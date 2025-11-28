def findTheDifference(s: str, t: str) -> str:
    """An additional letter is added with s to create t at a random place and this solution returns the
    letter that has been added.

    Args:
        s (str): The actual string.
        t (str): The string created by adding a letter at a random place.

    Returns:
        str: The letter that is added in t i.e., the difference between t and s.
    """
    res = ''
    for l in t:
        if l in s:
            s = s.replace(l, '', 1)
        else:
            res += l

    return res


if __name__ == "__main__":
    print(findTheDifference("abcd", "abcde"))
