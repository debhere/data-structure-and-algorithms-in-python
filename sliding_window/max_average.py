from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    """You are given an integer array nums consisting of n elements, and an integer k. Finding a
    contiguous subarray whose length is equal to k that has the maximum average value and return this
    value.

    Args:
        nums: List[int], the input array of numbers.
        k: int, number of elements in the sub-array.

    Returns:
        float: Highest average among the contagious sub-arrays.

    """
    max_sum = sum(nums[: k])
    window = max_sum

    for i in range(k, len(nums)):
        window -= nums[i-k]
        window += nums[i]

        if window > max_sum:
            max_sum = window

    return max_sum / k


if __name__ == "__main__":
    print(findMaxAverage([1, 12, -5, -6, 50, 3], k=4))
