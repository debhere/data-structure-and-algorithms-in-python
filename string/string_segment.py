def countSegments(s: str) -> int:
    return len(s.split())


if __name__ == "__main__":
    print(countSegments("Hello, my name is John"))
    print(countSegments("Hello"))
