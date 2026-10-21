def tong_so_chan(n: int) -> int:
    return sum(range(2, n + 1, 2))


if __name__ == "__main__":
    n = int(input().strip())
    print(f"Tổng các số chẵn từ 1 đến {n} = {tong_so_chan(n)}")
