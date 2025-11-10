from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """The function is a solution of a LeetCode problem
    where it adds 1 to the number represented by a given array and returns
    the resulting number in an array. Eg:- If [1, 2, 3] is passed as a parameter
    the function will add 1 to the number i.e., 124 and then return [1, 2, 4]

    Args:
        digits (List[int]): An integer number represented in a list of integers.

    Returns:
        List[int]: Resulting number after adding one represented in a list of integers.
    """
    dstr = ''.join([str(digit) for digit in digits])
    dstr = str(int(dstr) + 1)
    return [int(d) for d in dstr]


if __name__ == "__main__":
    print(plusOne([1, 2, 3]))

