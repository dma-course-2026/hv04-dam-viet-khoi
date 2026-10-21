def la_so_chan(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    n = int(input().strip())
    if la_so_chan(n):
        print(f"{n} là số chẵn")
    else:
        print(f"{n} là số lẻ")
