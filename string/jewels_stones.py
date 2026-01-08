def numJewelsInStones(jewels: str, stones: str) -> int:
    """You're given strings jewels representing the types of stones that are jewels, and stones
    representing the stones you have. Each character in stones is a type of stone you have. You want
    to know how many of the stones you have are also jewels.

    Letters are case-sensitive, so "a" is considered a different type of stone from "A".

    Args:
        jewels(str): stones that are jewels.
        stones(str): stones.

    Returns:
        int: how many stones are jewels
    """
    num = 0
    for letter in stones:
        if letter in jewels:
            num += 1

    return num


if __name__ == "__main__":
    print(numJewelsInStones("aA", "aAAbbbb"))
    print(numJewelsInStones("z", "ZZ"))
