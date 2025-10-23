def cansum_bruteforce(target, arr):
    if target == 0:
        return True
    if target < 0:
        return False
    for num in arr:
        remainder = target - num
        if cansum_bruteforce(remainder, arr) is True:
            return True

    return False


def cansum_memo(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in arr:
        remainder = target - num
        if cansum_memo(remainder, arr, memo) is True:
            memo[target] = True
            return memo[target]

    memo[target] = False
    return memo[target]


if __name__ == "__main__":
    print(cansum_bruteforce(7, [2, 3]))
    print(cansum_bruteforce(7, [5, 3, 4, 7]))
    print(cansum_bruteforce(7, [2, 4]))
    print(cansum_bruteforce(8, [2, 3, 5]))
    # print(cansum_bruteforce(300, [7, 14]))
    # As expected, the above case is getting hung-up the execution
    # in the brute-force solution. Need memoization

    print("Memoization output starts from here")

    print(cansum_memo(7, [2, 3]))
    print(cansum_memo(7, [5, 3, 4, 7]))
    print(cansum_memo(7, [2, 4]))
    print(cansum_memo(8, [2, 3, 5]))
    print(cansum_memo(300, [7, 14]))
