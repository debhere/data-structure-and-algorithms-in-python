def insertionSort(nums: list[int]):
    for i in range(1, len(nums)):
        key: int = nums[i]
        j: int = i - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    print(nums)


def main():
    num_list: list[int] = []
    try:
        size: int = int(input("How many numbers you like to enter? "))
        if size == 0:
            raise ValueError
        print("Enter random numbers to sort......")
        i = size
        while i >= 1:
            num: int = int(input())
            num_list.append(num)
            i -= 1
        insertionSort(num_list)
    except Exception as e:
        print("Some error occurred")


if __name__ == "__main__":
    main()
