from typing import List


def distributeCandies(candyType: List[int]) -> int:
    """Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she
    started to gain weight, so she visited a doctor. The doctor advised Alice to only eat n / 2
    of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat
    the maximum number of different types of candies while still following the doctor's advice.
    Given the integer array candyType of length n, return the maximum number of different types of candies
    she can eat if she only eats n / 2 of them.

    Args:
        candyType: List[int], types of candies.

    Returns:
        int: number of candies Alice can eat.
    """
    no_of_candies = len(candyType) // 2
    candy_limit = len(set(candyType))
    return min(no_of_candies, candy_limit)


if __name__ == "__main__":
    print(distributeCandies([1, 1, 2, 2, 3, 3]))
    print(distributeCandies([1, 1, 2, 3]))
