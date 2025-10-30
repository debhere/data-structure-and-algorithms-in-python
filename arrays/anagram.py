from collections import Counter


# def isAnagram(s: str, t: str) -> bool:
#     c1 = Counter(s)
#     c2 = Counter(t)
#
#     return c1 == c2

def isAnagram(s: str, t: str) -> bool:
    scount, tcount = {}, {}

    for idx in range(len(s)):
        scount[s[idx]] = 1 + scount.get(s[idx], 0)
        tcount[t[idx]] = 1 + tcount.get(t[idx], 0)

    return scount == tcount


if __name__ == "__main__":
    print(isAnagram("racecar", "carrace"))
    print(isAnagram("jar", "jam"))
    print(isAnagram("hoglabon", "bonhogla"))
