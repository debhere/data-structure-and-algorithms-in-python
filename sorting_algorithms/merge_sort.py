def merge_sort(dlist: list):
    if len(dlist) <= 1:
        return dlist

    mid = len(dlist) // 2
    left = dlist[:mid]
    right = dlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    while i < len(left):
        merged_arr.append(left[i])
        i += 1

    while j < len(right):
        merged_arr.append(right[j])
        j += 1

    return merged_arr


if __name__ == "__main__":
    print(merge_sort([2, 8, 66, 36, 0, 7]))
    print(merge_sort([12, 11, 9, 100, 4, 10, 24, 88, -2, 17]))
