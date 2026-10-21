def tong_1_den_n(n: int) -> int:
    return n * (n + 1) // 2


if __name__ == "__main__":
    n = int(input().strip())
    print(f"Tổng từ 1 đến {n} = {tong_1_den_n(n)}")
