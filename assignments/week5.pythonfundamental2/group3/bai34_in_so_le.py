def cac_so_le(n: int) -> list[int]:
    return list(range(1, n + 1, 2))


if __name__ == "__main__":
    n = int(input().strip())
    print(*(cac_so_le(n)))
