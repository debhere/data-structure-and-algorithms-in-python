from typing import List


def findLHS(nums: List[int]) -> int:
    """We define a harmonious array as an array where the difference between its maximum value and its
    minimum value is exactly 1. Given an integer array nums, it returns the length of its longest
    harmonious subsequence among all its possible subsequences.

    Args:
        nums: List[int], an array of numbers

    Returns:
        int: The size of the harmonious subsequence.
    """
    nums.sort()
    j, maxLen = 0, 0

    for i in range(len(nums)):
        while nums[i] - nums[j] > 1:
            j += 1
        if nums[i] - nums[j] == 1:
            maxLen = max(maxLen, i - j + 1)
    return maxLen


if __name__ == "__main__":
    print(findLHS([1, 2, 3, 4]))
    print(findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
