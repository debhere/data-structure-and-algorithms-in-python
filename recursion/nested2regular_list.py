# Solution to make a nested list into a regular list with recursion

def get_regular_list(dlist):
    reg_list = []

    for element in dlist:
        if isinstance(element, int):
            reg_list.append(element)
        else:
            reg_list.extend(get_regular_list(element))

    return reg_list


if __name__ == "__main__":
    # get_regular_list([3, [4, 5], [6, [7, 8, 9]]])
    print(get_regular_list([3, [4, 5], [6, [7, 8, 9]]]))
    print(get_regular_list([3, [4, 5], [6, [7, 8, 9]], [10, [11, 12], [[13, 14, 15]]]]))
