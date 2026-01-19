from typing import List


def getSummaryRanges(nums: List[int]) -> List[str]:
    """You are given a sorted unique integer array nums. A range [a,b] is the set of all integers from
    a to b (inclusive). Return the smallest sorted list of ranges that cover all the numbers in the array
    exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no
    integer x such that x is in one of the ranges but not in nums.
    """
    ranges: List[str] = []
    if not nums:
        return ranges
    if len(nums) == 1:
        ranges.append(str(nums[0]))
        return ranges
    temp = nums[0]
    ele: str = str(nums[0])
    for num in nums[1:]:
        # if temp + 1 == num:
        #     ele += '->' + str(num)
        #     # temp = num
        if temp + 1 != num:
            if ele != str(temp):
                ele += '->' + str(temp)
            ranges.append(ele)
            ele = str(num)
            # temp = num
        if num == nums[-1]:
            if num == temp + 1:
                ele += '->' + str(num)
            ranges.append(ele)
            if str(num) not in ele:
                ranges.append(str(num))
        temp = num

    return ranges


if __name__ == "__main__":
    print(getSummaryRanges([0, 1, 2, 4, 5, 7]))
    print(getSummaryRanges([1, 4]))
    print(getSummaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(getSummaryRanges([-1]))
