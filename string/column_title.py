import string


def convertToNumberBestSolution(columnTitle: str) -> int:
    """This is a LeetCode problem. There is another solution below but with more lines of code and a
    greater space complexity.

    Here again I have leveraged Python's ord() function. The approach is simple i.e., for any given column
    title, loop through to get each character's ordinal number, multiple 26 with the previous character and
    store the summation in a variable. Return the consolidated result.

    Args:
        columnTitle(str): Column title of an Excel file.

    Returns:
        int: Corresponding column number of a given column title
    """
    result = 0

    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)

    return result


def convertToTitleBestSolution(columnNumber: int) -> str:
    """While ConvertToNumber() solution is great and beats 100% of the solutions in terms of time complexity,
    it is a little lagging in space complexity.

    Using Python's default ord() method is doing the trick here with considerably lesser lines of code.

    Args:
        columnNumber(int): Column number of an Excel file.

    Returns:
        str: Corresponding column title of a given column number
    """
    result = ''
    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        letter = chr(ord('A') + remainder)
        result = letter + result
        columnNumber //= 26

    return result


def convertToNumber(columnTitle: str) -> int:
    number: int = 0
    numberMap: dict[str] = {string.ascii_uppercase[i - 1]: i for i in range(1, 27)}

    titleLen = len(columnTitle)

    if titleLen == 1:
        number += numberMap[columnTitle]
    else:
        number = numberMap[columnTitle[0]]
        while titleLen > 1:
            number = number * 26 + numberMap[columnTitle[1]]
            titleLen -= 1
            columnTitle = columnTitle[1:]

    return number


def convertToTitle(columnNumber: int) -> str:
    """This is a LeetCode problem where the function returns the column title for a given column
    number.

    While the approach seems simple but things get a little interesting when the column number
    is a quite bigger. Moreover, special logic has to be deduced for edge cases. So here you go.

    Initiate title as a blank string and a mapping for column number to column title.

    If column number is less than or equal to 26 then it is straightforward and return the corresponding
    letter as found in the mapping.

    When column number is greater than 26 then we need to do certain tricks. Start a while loop and
    create two variables as 'front' which is the integer division result divided by 26 and 'rear' which
    is modulus of that.

    If modulus is 0 then rear is equal to 26 af front should be decremented by 1. Then prefix the
    corresponding letter for rear and continue the while loop.

    At the end, prefix the letter for front with the title and return.

    Args:
        columnNumber(int): Column number of an Excel file.

    Returns:
        str: Corresponding column title of a given column number
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
    # print(convertToTitle(1))
    # print(convertToTitle(28))
    # print(convertToTitle(701))
    # print(convertToTitle(702))
    # print(convertToTitle(703))
    # print(convertToTitle(2147483647))
    # print(convertToTitle(52))
    # print(convertToTitle(7020))
    # print(convertToTitle(5473578))
    # print()
    # print(convertToNumber('A'))
    # print(convertToNumber('AB'))
    # print(convertToNumber('ZY'))
    # print(convertToNumber('ZZ'))
    # print(convertToNumber('AAA'))
    # print(convertToNumber('FXSHRXW'))
    print(convertToTitleBestSolution(2147483647))
    print(convertToTitleBestSolution(701))
    print(convertToTitleBestSolution(703))
    print(convertToTitleBestSolution(28))
