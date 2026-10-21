import sys


def tong_chia_het_3_hoac_5(m: int, n: int) -> int:
    return sum(i for i in range(m, n + 1) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        m = int(tokens[0])
        n = int(tokens[1])
        print(f"Kết quả: {tong_chia_het_3_hoac_5(m, n)}")
