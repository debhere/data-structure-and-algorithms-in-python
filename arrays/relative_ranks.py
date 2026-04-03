from typing import List


def findRelativeRanks(score: List[int]) -> List[str]:
    """You are given an integer array score of size n, where score[i] is the score of the ith athlete in
    a competition. All the scores are guaranteed to be unique.

    Args:
        score: List[int], a list of scores

    Returns:
        List[str]: Relative position of the athletes.

    """
    res: List[str] = [''] * len(score)
    ref: List[int] = sorted(score, reverse=True)
    # pos: str = ''

    for i, s in enumerate(ref):
        idx = score.index(s)
        if i == 0:
            pos = "Gold Medal"
        elif i == 1:
            pos = "Silver Medal"
        elif i == 2:
            pos = "Bronze Medal"
        else:
            pos = str(i + 1)
        res[idx] = pos

    return res


if __name__ == "__main__":
    print(findRelativeRanks([5, 4, 3, 2, 1]))
    print(findRelativeRanks([10, 3, 8, 9, 4]))
