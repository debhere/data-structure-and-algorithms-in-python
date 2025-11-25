from typing import List


def isHappy(n: int) -> bool:
    """This is a LeetCode problem, Given an integer number if the summation of the square of its digits
    results into 1 then it is a happy number.

    I am taking the digits and getting summation and storing the result into a dictionary. If I get the
    summation as 1 then return as True else I continue the process until I encounter a result which is present
    in the map denoting a repetition.

    Args:
        n (int): An integer.

    Returns:
        bool: Whether the argument is a happy number
    """
    sq_map: dict[int] = {}
    while n >= 1:
        temp = 0
        for digit in str(n):
            temp += int(digit) ** 2
        if temp == 1:
            return True
        elif sq_map.get(n, 0) == temp:
            return False
        else:
            sq_map[n] = temp
            n = temp
    return False


if __name__ == "__main__":
    print(isHappy(19))
    print(isHappy(2))
    print(isHappy(7))
