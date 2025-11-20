import string


def convertToTitle(columnNumber: int) -> str:
    """This is a LeetCode problem where the function returns the column title for a given column
    number.

    While the approach

    :param columnNumber:
    :return:
    """
    title = ''
    titleMap: dict[int] = {i: string.ascii_uppercase[i - 1] for i in range(1, 27)}

    if columnNumber <= 26:
        return titleMap[columnNumber]
    else:
        front = columnNumber
        while front > 26:
            rear = 26 if front % 26 == 0 else front % 26
            front //= 26
            if rear == 26:
                front -= 1
            title = f"{titleMap[rear]}{title}"

        title = f"{titleMap[front]}{title}"

    return title


if __name__ == "__main__":
    print(convertToTitle(1))
    print(convertToTitle(28))
    print(convertToTitle(701))
    print(convertToTitle(702))
    print(convertToTitle(2147483647))
    print(convertToTitle(52))
    print(convertToTitle(7020))
    print(convertToTitle(5473578))
    # print(test(2147483647))
    # print(test(703))
    # print(test(702))
    # print(test(701))
