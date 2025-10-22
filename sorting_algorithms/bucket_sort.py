import math


def bucketSort_solution(nums: list[int]):
    num_of_buckets = round(math.sqrt(len(nums)))
    buckets = [[] for _ in range(num_of_buckets)]
    maxVal = max(nums)
    sorted_list = []

    for element in nums:
        idx = math.floor((element / maxVal + 1) / num_of_buckets)
        #idx = math.floor((element * num_of_buckets) / maxVal)
        buckets[idx].append(element)

    for bucket in buckets:
        bucket.sort()
        sorted_list.extend(bucket)

    print(sorted_list)


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

# This function is not correct
# def bucketSort(customList):
#     numberofBuckets = round(math.sqrt(len(customList)))
#     maxValue = max(customList)
#     arr = []
#
#     for i in range(numberofBuckets):
#         arr.append([])
#     for j in customList:
#         index_b = math.ceil(j * numberofBuckets / maxValue)
#         arr[index_b - 1].append(j)
#
#     for i in range(numberofBuckets):
#         arr[i] = insertionSort(arr[i])
#
#     k = 0
#     for i in range(numberofBuckets):
#         for j in range(len(arr[i])):
#             customList[k] = arr[i][j]
#             k += 1
#     return customList


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
        bucketSort_solution(num_list)
    except Exception as e:
        print("Some error occurred", e)


if __name__ == "__main__":
    # print(bucketSort([2, 1, 7, 6, 5, 3, 4, 9, 8]))
    # print(bucketSort([2, 1, 7, 6, 0, 3, 4, 9, 8]))
    # bucketSort_solution([2, 1, 7, 6, 0, 3, 4, 9, 8])
    main()
