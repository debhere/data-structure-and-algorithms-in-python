from typing import List


def maxArea(height: List[int]) -> int:
    n = len(height)
    areas = []
    for i in range(n):
        for j in range(i + 1, n):
            base = j - i
            h = height[i] if height[i] < height[j] else height[j]
            area = h * base
            areas.append(area)

    return max(areas)


# Need to use two-pointer technique


if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
