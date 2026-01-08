def numJewelsInStones(jewels: str, stones: str) -> int:
    num = 0
    for letter in stones:
        if letter in jewels:
            num += 1

    return num


if __name__ == "__main__":
    print(numJewelsInStones("aA", "aAAbbbb"))
    print(numJewelsInStones("z", "ZZ"))
