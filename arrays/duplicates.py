def hasDuplicate(nums: list[int]) -> bool:
    return len(set(list(nums))) < len(nums)


if __name__ == "__main__":
    print(hasDuplicate([1, 2, 3, 3]))
    print(hasDuplicate([1, 2, 3, 4]))
