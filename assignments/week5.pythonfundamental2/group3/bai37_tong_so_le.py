def tong_so_le(n: int) -> int:
    return sum(range(1, n + 1, 2))


if __name__ == "__main__":
    n = int(input().strip())
    print(f"Tổng các số lẻ từ 1 đến {n} = {tong_so_le(n)}")
