def tach_chu_so(n: int) -> tuple[int, int, int]:
    n = abs(n)
    return n // 100, (n % 100) // 10, n % 10


if __name__ == "__main__":
    n = int(input().strip())
    tram, chuc, don_vi = tach_chu_so(n)
    print(f"hàng trăm = {tram}, hàng chục = {chuc}, hàng đơn vị = {don_vi}")
