def hasDuplicate(nums: list[int]) -> bool:
    """This is LeetCode problem  to check if list has duplicate digits.

    This function converts the list into a set and then compares the length of both the set and
    the list. In case of dupes, the length of the set should be less.

    Args:
        nums(List[int]): list of integers

    Returns:
        bool: True if dupes exist otherwise False.
    """
    return len(set(list(nums))) < len(nums)


if __name__ == "__main__":
    print(hasDuplicate([1, 2, 3, 3]))
    print(hasDuplicate([1, 2, 3, 4]))
