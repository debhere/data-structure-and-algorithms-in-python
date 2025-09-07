def bubbleSort(nums: list[int]):
    for i in range(len(nums) - 1):
        is_sorted: bool = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = True
        if not is_sorted:
            break

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
        bubbleSort(num_list)
    except Exception as e:
        print("Some error occurred")


if __name__ == "__main__":
    main()
