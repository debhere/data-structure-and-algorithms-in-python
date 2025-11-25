from typing import List


def getSummaryRanges(nums: List[int]) -> List[str]:
    """Need to complete

    :param nums:
    :return:
    """
    l: List[str] = []
    temp = nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] + 1 != nums[i]:
            if temp == nums[i-1]:
                l.append(str(temp))
            else:
                l.append(f"{temp}->{nums[i-1]}")
            temp = nums[i]
    return l


if __name__ == "__main__":
    print(getSummaryRanges([0, 1, 2, 4, 5, 7]))
    print(getSummaryRanges([0, 2, 3, 4, 6, 8, 9]))
