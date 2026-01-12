from typing import List


def fizzBuzz(n: int) -> List[str]:
    """Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

    Args:
        n(int): input integer

    Returns:
        List[str]: A list consisting only strings.
    """
    res: List[str] = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            res.append("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


if __name__ == "__main__":
    print(fizzBuzz(3))
    print(fizzBuzz(5))
    print(fizzBuzz(15))
