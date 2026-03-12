from typing import List


def moveZeroes(nums: List[int]) -> None:
    """Given an integer array nums, move all 0's to the end of it while maintaining the relative order
    of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Args:
        nums: A List of numbers.

    Returns:
        None
    """
    zeroCount = nums.count(0)
    zeroes = [0] * zeroCount
    nums[:] = [num for num in nums if num != 0]
    nums.extend(zeroes)
    print(nums)


if __name__ == "__main__":
    moveZeroes([0, 1, 0, 3, 12])
