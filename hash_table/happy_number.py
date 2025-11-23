from typing import List


def isHappy(n: int) -> bool:
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
