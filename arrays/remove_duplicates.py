from typing import List


# sol 1: returns the number of unique numbers
def getUniqueNumbers(nums: List[int]) -> int:
    if len(nums) in [0, 1]:
        return len(nums)
    prev = nums[0]
    size = 1
    for num in nums:
        if prev != num:
            prev = num
            size += 1
    return size


# Beats only 9.5% in LeetCode
def removeDuplicates(nums: List[int]) -> int:
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def removeDupesWithTwoPointer(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(removeDuplicates([1, 1, 2]))
    print(removeDuplicates([]))
    print(removeDuplicates([2]))
