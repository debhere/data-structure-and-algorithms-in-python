def selectionSort(nums: list[int]):
    for i in range(len(nums)):
        min_index = i
        for j in range(1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

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
        selectionSort(num_list)
    except Exception as e:
        print("Some error occurred")


if __name__ == "__main__":
    main()
