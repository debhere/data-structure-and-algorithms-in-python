from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """The function is a solution of a LeetCode problem where it adds 1 to the number represented
    by a given array and returns the resulting number in an array. Eg:- 123 is represented as an array
    [1, 2, 3] and is passed as a parameter. The function will add 1 to the number i.e., 124 and then
    return [1, 2, 4] as an array.

    The function first creates a string concatenating the digits using the join() method which has O(n)
    time complexity. Then convert the string again to integer, add 1 to it and convert it back to string
    again. Create a list with comprehension and convert each element back to integer, then return it.

    So, the overall time complexity will be O(n) and space complexity will be O(1).

    Args:
        digits (List[int]): An integer number represented in a list of integers.

    Returns:
        List[int]: Resulting number after adding one represented in a list of integers.
    """
    dstr = ''.join([str(digit) for digit in digits])  # O(n) time complexity
    dstr = str(int(dstr) + 1)  # O(1) time complexity
    return [int(d) for d in dstr]  # Time complexity: O(n)


if __name__ == "__main__":
    print(plusOne([1, 2, 3]))
