from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    """Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all
    the integers in the range [1, n] that do not appear in nums.

    Args:
        nums: List[int], a list of integers

    Returns:
        List[int]: A list of integers that do not appear in the range[1, n]

    """
    limit = len(nums) + 1
    return list(set(list(range(1, limit))) - set(nums))


def findDisappearedNumbersBruteForce(nums: List[int]) -> List[int]:
    limit = len(nums) + 1
    ideal = list(range(1, limit))
    nums[:] = [num for num in ideal if num not in nums]
    return nums


if __name__ == "__main__":
    print(findDisappearedNumbersBruteForce([4, 3, 2, 7, 8, 2, 3, 1]))
    print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
