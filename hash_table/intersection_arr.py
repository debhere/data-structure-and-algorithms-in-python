from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    intersect = {'common': []}

    for num in nums1:
        if num in nums2 and num not in intersect['common']:
            intersect['common'].append(num)

    return intersect['common']


def intersectionBestSolution(nums1: List[int], nums2: List[int]) -> List[int]:
    """Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique, and you may return the result in any order.

    Args:
        nums1: List[int], first array of numbers.
        nums2: List[int], second array of numbers.

    Returns:
        List[int]: A list of common integers in both arrays.
    """
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print()
    print(intersectionBestSolution([1, 2, 2, 1], [2, 2]))
    print(intersectionBestSolution([4, 9, 5], [9, 4, 9, 8, 4]))
