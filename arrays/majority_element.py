from typing import List


def getMajorityElementHashMap(nums: List[int]) -> int:
    """This is a LeetCode problem to find the majority element within an array. This problem can be
    solved using Moore's voting algorithm as well (done below). However here I have used hash map.

    Args:
        nums(List[int]): An array of integers

    Returns:
        int: An integer which is the majority element of the array.
    """
    d: dict = {}
    result = majority = 0

    for num in nums:
        d[num] = d.get(num, 0) + 1
        if d[num] > majority:
            result = num
            majority = d[num]
    return result


def getMajorityElementMooreAlgo(nums: List[int]) -> int:
    times = 0
    element = 0

    for num in nums:
        if times == 0:
            element = num

        if num == element:
            times += 1
        else:
            times -= 1

    times = 0

    for num in nums:
        if num == element:
            times += 1

    return element


if __name__ == "__main__":
    print(getMajorityElementHashMap([3, 2, 3]))
    print(getMajorityElementHashMap([2, 2, 1, 1, 1, 2, 2]))
    print(getMajorityElementHashMap([2, 2, 1, 1, 1, 1, 1, 2, 2]))
    print(getMajorityElementHashMap([1, 1, 1, 2, 5, 6, 1, 1, 2, 2, 6, 6, 6, 1]))
    print()
    print(getMajorityElementMooreAlgo([3, 2, 3]))
    print(getMajorityElementMooreAlgo([2, 2, 1, 1, 1, 2, 2]))
    print(getMajorityElementMooreAlgo([2, 2, 1, 1, 1, 1, 1, 2, 2]))


