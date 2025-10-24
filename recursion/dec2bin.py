def decimal_to_binary(num):
    div = num // 2
    remainder = num % 2

    if div == 1:
        return 'ob' + str(div) + str(remainder)
    else:
        return decimal_to_binary(div) + str(remainder)


if __name__ == "__main__":
    # assert bin(6) == decimal_to_binary(6), "checking"
    print(decimal_to_binary(6), bin(6))
    print(decimal_to_binary(10), bin(10))
    print(decimal_to_binary(55), bin(55))
