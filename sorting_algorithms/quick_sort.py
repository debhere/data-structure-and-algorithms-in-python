def quick_sort(dlist: list):
    if len(dlist) <= 1:
        return dlist
    pivot = dlist[0]
    left_arr = [element for element in dlist if element < pivot]
    mid = [element for element in dlist if element == pivot]
    right_arr = [element for element in dlist if element > pivot]

    return quick_sort(left_arr) + quick_sort(mid) + quick_sort(right_arr)


if __name__ == "__main__":
    print(quick_sort([2, 8, 66, 36, 0, 7]))
