def isIsomorphic(s: str, t: str) -> bool:
    if s is None or t is None:
        return False
    elif len(s) != len(t):
        return False
    else:
        sMap = {}
        for i, l in enumerate(s):
            if t[i] in sMap.values() and sMap.get(l, 'NF') == 'NF':
                return False
            elif sMap.get(l, 'NF') == 'NF':
                sMap[l] = t[i]
            else:
                continue
        # print(sMap)
        new_s = ''
        for s_ in s:
            new_s += sMap[s_]

        return new_s == t


def optimumSolution(s: str, t: str) -> bool:
    """Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic
    if the characters in s can be replaced to get t. All occurrences of a character must be replaced with
    another character while preserving the order of characters. No two characters may map to the same character,
    but a character may map to itself.

    Args:
        s: str, first string
        t: str, second string

    Returns:
        bool: True if both the strings are isomorphic.
    """
    if s is None or t is None:
        return False
    if len(s) != len(t):
        return False
    map_st = {}
    map_ts = {}

    for e1, e2 in zip(s, t):
        if e1 in map_st:
            if map_st[e1] != e2:
                return False
        else:
            if e2 in map_ts:
                return False
            map_st[e1] = e2
            map_ts[e2] = e1

    return True


if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))
    print(isIsomorphic("paper", "title"))
    print(isIsomorphic("foo", "bar"))
    print(isIsomorphic("bbbaaaba", "aaabbbba"))
    print(isIsomorphic("badc", "baba"))
    print('\n')
    print(optimumSolution("egg", "add"))
    print(optimumSolution("badc", "baba"))
