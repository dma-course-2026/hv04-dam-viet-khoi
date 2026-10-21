def hoan_doi(a: int, b: int) -> tuple[int, int]:
    return b, a


if __name__ == "__main__":
    tokens = input().split()
    if len(tokens) >= 2:
        a, b = int(tokens[0]), int(tokens[1])
    else:
        a = int(tokens[0])
        b = int(input().strip())
    a, b = hoan_doi(a, b)
    print(f"Sau khi hoán đổi: a = {a}, b = {b}")
