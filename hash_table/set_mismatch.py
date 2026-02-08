from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    """You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
    due to some error, one of the numbers in s got duplicated to another number in the set, which results
    in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.
    Find the number that occurs twice and the number that is missing and return them in the form of an array.

    Args:
        nums: List[int], an array of integers

    Returns:
        List[int]: A list of the numbers which are duplicate in nums and are missing in the ideal sequence.
    :param nums:
    :return:
    """
    length: int = len(nums)
    numMap: List[int] = [0] * (length + 1)
    missing, duplicate = 0, 0

    for num in nums:
        numMap[num] += 1

    for i in range(1, len(numMap)):
        if numMap[i] == 2:
            duplicate = i
        if numMap[i] == 0:
            missing = i

    return [duplicate, missing]


if __name__ == "__main__":
    print(findErrorNums([1, 2, 2, 4]))
    print(findErrorNums([1, 1]))
    print(findErrorNums([2, 2]))
