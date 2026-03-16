def lengthOfLongestSubstring(s: str) -> int:
    """Given a string s, find the length of the longest substring without duplicate characters.

    Create and initialize couple of local variables as MaxLen and substring. Loop through the input
    string and add characters into substring and maxLen should be max of maxLen value and length of the
    substring. If a repeating character occurs which already exists in the substring then we have two
    logic in place as pee the condition --i) get the right index of the repeating char, add 1 to it then
    get the slice of the substring from that index till end and at last concat the repeating character.
    ii) If the repeating character is occurring more than one times in the input string then just assign the
    same with the substring variable.

    Args:
        s: input String

    Returns:
        int: the maximum length of the substring with no repeating characters.
    """
    maxLen = 0
    substring = ''
    for i, l in enumerate(s):
        if l not in substring:
            substring += l
            maxLen = max(maxLen, len(substring))
        else:
            if l == s[i - 1]:
                substring = l
            else:
                idx = substring.rfind(l)
                substring = substring[idx + 1:] + l

    return maxLen



if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("aab"))
    print(lengthOfLongestSubstring("  "))
    print(lengthOfLongestSubstring("dvdf"))
    print(lengthOfLongestSubstring("aabaab!bb"))
