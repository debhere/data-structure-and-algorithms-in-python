def add_elements(dlist):
    if len(dlist) == 1:
        return dlist[0]
    return dlist[0] + add_elements(dlist[1:])


if __name__ == "__main__":
    print(add_elements([40, 50, 10, 20]))
    print(add_elements([100, 50, 40, 150]))
