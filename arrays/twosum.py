def twoSum(nums: list[int], target: int) -> list[int]:
    idx_map = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff in idx_map:
            return [idx_map[diff], idx]
        idx_map[num] = idx


if __name__ == "__main__":
    print(twoSum([3, 4, 5, 6], 7))
    print(twoSum([4, 5, 6], 10))
    print(twoSum([5, 5], 10))
    print(twoSum([3, 2, 4], 6))
