from typing import List


def containsNearbyDuplicates(nums: List[int], k: int) -> bool:
    """This is a famous LeetCode problem. Given an integer array nums and an integer k, return true if there are two
    distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

    Args:
        nums (List[int]): An array of integers.
        k (int): An integer

    Returns:
        bool
    """
    temp: int = -1
    dupeMap: dict[int] = {}

    for i, n in enumerate(nums):
        if n in dupeMap:
            if temp == -1 or temp > abs(dupeMap[n] - i):
                temp = abs(dupeMap[n] - i)
        dupeMap[n] = i

    return True if temp <= k and temp != -1 else False


if __name__ == "__main__":
    print(containsNearbyDuplicates([1, 2, 3, 1], 3))
    print(containsNearbyDuplicates([1, 0, 1, 1], 1))
    print(containsNearbyDuplicates([1, 2, 3, 1, 2, 3], 2))
