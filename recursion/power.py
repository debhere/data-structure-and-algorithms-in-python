def calc_power(n, m):
    if m == 1:
        return n
    if m == 0:
        return 1
    else:
        return n * calc_power(n, m - 1)


if __name__ == "__main__":
    print(calc_power(4, 2))
    print(calc_power(100, 0))
    print(calc_power(15, 3))
