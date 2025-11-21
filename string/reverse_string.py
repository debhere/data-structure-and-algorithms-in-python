from typing import List


def reverseString(s: List[str]) -> None:
    """A LeetCode problem to reverse string in a list but the modifications should be done in-place
    i.e., not return anything. Achieved using simple indexing logic.

    Args:
        s (List[str]): A list of strings
    """
    s[:] = s[::-1]
    print(s)


if __name__ == "__main__":
    reverseString(["h", "e", "l", "l", "o"])
