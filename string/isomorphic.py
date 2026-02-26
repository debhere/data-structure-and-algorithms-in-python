def isIsomorphic(s: str, t: str) -> bool:
    if s is None or t is None:
        return False
    elif len(s) != len(t):
        return False
    else:
        sMap = {}
        for i, l in enumerate(s):
            if sMap.get(l, 'NF') == 'NF':
                sMap[l] = t[i]
            else:
                continue
        # print(sMap)
        new_s = ''
        for s_ in s:
            new_s += sMap[s_]

        return new_s == t


if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))
    print(isIsomorphic("paper", "title"))
    print(isIsomorphic("foo", "bar"))
    print(isIsomorphic("bbbaaaba", "aaabbbba"))
