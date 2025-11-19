from typing import List


# Expectation => O(n) time complexity and O(1) space complexity
def getSingleNumber(nums: List[int]) -> int:
    """This is a LeetCode problem. Expectation is to return only the integer which appears only
    once. This problem is solved with XOR/bit manipulation. XOR of any two number gives the difference of bits as 1 and same bit as 0. In other words, each
    time we have a difference in bits, singleNumber value will be increased by that number and when
    we encounter a same number again, the singleNumber value will be decreased by that number.

    Args:
        nums(List[int]): input array of integers

    Returns:
        int: element of the input array that appears only once.
    """
    singleNumber: int = 0
    for num in nums:
        singleNumber ^= num
    return singleNumber


if __name__ == "__main__":
    print(getSingleNumber([2, 2, 1]))
    print(getSingleNumber([4, 1, 2, 1, 2]))
