def countSegments(s: str) -> int:
    """Given a string s, return the number of segments in the string. A segment is defined to
    be a contiguous sequence of non-space characters.

    Args:
        s (string): The input string

    Returns:
        int: The number of segment in the given string
    """
    return len(s.split())


if __name__ == "__main__":
    print(countSegments("Hello, my name is John"))
    print(countSegments("Hello"))
