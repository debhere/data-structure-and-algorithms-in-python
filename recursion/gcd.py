def greatest_common_divisor(p, q):
    if p > q:
        p, q = q, p
    if p % q == 0:
        return p
    else:
        remainder = p % q
        return greatest_common_divisor(remainder, p)


if __name__ == "__main__":
    print(greatest_common_divisor(6, 8))
    print(greatest_common_divisor(120, 500))
