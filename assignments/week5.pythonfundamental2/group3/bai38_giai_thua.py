import math


def giai_thua(n: int) -> int:
    return math.prod(range(1, n + 1))


if __name__ == "__main__":
    n = int(input().strip())
    print(f"{n} giai thừa = {giai_thua(n)}")
