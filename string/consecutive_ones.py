from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    """Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Args:
        nums: List[int], A list of numbers.

    Returns:
        int: Count of consecutive 1s in the input list.
    """
    maxOne, curr = 0, 0

    for num in nums:
        if num == 1:
            curr += 1
        else:
            if curr > maxOne:
                maxOne = curr
                curr = 0

    return max(maxOne, curr)


if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
