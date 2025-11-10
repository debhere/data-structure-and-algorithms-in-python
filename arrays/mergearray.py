from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """This function is the solution of a LeetCode problem regarding merging of sorted array. Given
    two list - nums1, & nums2 and m, n are the number of elements should be taken from each list. At
    the end function should not return anything but make a non-decreasing merged array in place of
    nums1 such that the time complexity is O(m + n).

    Args:
        nums1(List[int]): first array.
        m(int): number of elements to be taken from first array.
        nums2(List[int]): second array.
        n(int): number of elements to be taken from second array.

    Returns:
        None: merging to be done in place.
    """
    nums1[:] = nums1[: m] + nums2[: n]
    nums1.sort()
    print(nums1)


if __name__ == "__main__":
    merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
