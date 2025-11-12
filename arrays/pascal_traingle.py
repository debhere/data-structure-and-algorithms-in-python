from typing import List


def pascalTriangle1(numRows: int) -> List[List[int]]:
    """This is a LeetCode problem for pascal's triangle where each number is the summation of
    two numbers directly above it.
    example
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    time complexity is O(n^2) and space complexity is O(n)

    Args:
        numRows(int): triangle size.

    Returns:
        List[List[int]]: A list of lists of integers
    """
    result = [[1], [1, 1]]
    if numRows == 1:
        return [result[0]]
    if numRows == 2:
        return result
    while numRows > 2:
        l = list()
        pre = result[-1]
        for i in range(1, len(pre)):
            ele = pre[i - 1] + pre[i]
            l.append(ele)
        l.append(1)
        l.insert(0, 1)
        result.append(l)
        numRows -= 1

    return result


def pascalTriangle2(rowIndex: int) -> List[int]:
    """This is another LeetCode problem with given an integer as rowIndex, the row of the Pascal's
    triangle is returned.

    Args:
        rowIndex(int): row index.

    Returns:
        A list of integers.
    """
    triangle = [[1], [1, 1]]
    idx = rowIndex
    while idx >= 2:
        l = list()
        pre = triangle[-1]
        for i in range(1, len(pre)):
            ele = pre[i - 1] + pre[i]
            l.append(ele)
        l.append(1)
        l.insert(0, 1)
        triangle.append(l)
        idx -= 1

    return triangle[rowIndex]


if __name__ == "__main__":
    print(pascalTriangle1(3))
    print(pascalTriangle1(5))
    print()
    print(pascalTriangle2(3))
    print(pascalTriangle2(5))
