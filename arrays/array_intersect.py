from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays and you may return
    the result in any order.

    Args:
        nums1: First list of numbers.
        nums2: Second list of numbers.

    Returns:
        List[int]: A list of numbers that are the intersection of the input lists.

    """
    intersection = []
    for num in nums1:
        if num in nums2:
            intersection.append(num)
            nums2.remove(num)

    return intersection


if __name__ == "__main__":
    print(intersect([1, 2, 2, 1], [2, 2]))
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
