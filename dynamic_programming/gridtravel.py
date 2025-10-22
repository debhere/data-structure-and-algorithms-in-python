def grid_traveller(x: int, y: int, memo=None):
    if memo is None:
        memo = {}

    key = str(x) + ',' + str(y)
    if x == 0 or y == 0:
        return 0
    if x == 1 and y == 1:
        return 1
    if key in memo:
        return memo[key]
    memo[key] = grid_traveller(x - 1, y, memo) + grid_traveller(x, y - 1, memo)
    return memo[key]


if __name__ == "__main__":
    print(grid_traveller(3, 2))
    print(grid_traveller(5, 8))
    print(grid_traveller(18, 18))
