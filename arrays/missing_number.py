from typing import List


def missingNumber(nums: List[int]) -> int:
    """Given an array nums containing n distinct numbers in the range [0, n], return the only
    number in the range that is missing from the array.

    Args:
        nums: List[int], an array with integers

    Returns:
        int: The missing integer
    """
    limit = len(nums)

    while limit >= 0:
        if limit not in nums:
            return limit
        else:
            limit -= 1


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([0, 1]))
