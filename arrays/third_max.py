from typing import List


def thirdMax(nums: List[int]) -> int:
    """Given an integer array nums, return the third distinct maximum number in this array.
    If the third maximum does not exist, return the maximum number.

    nums:
        nums: List[int], A list of integers

    Returns:
        int: Third-largest distinct number of the list. If the list consist less than 3 distinct numbers
        then return the maximum number.


    """
    nums[:] = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    else:
        nums.sort(reverse=True)
        return nums[2]


if __name__ == "__main__":
    print(thirdMax([3, 2, 1]))
    print(thirdMax([1, 2]))
    print(thirdMax([2, 2, 3, 1]))
