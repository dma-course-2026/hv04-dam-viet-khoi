import sys


def tinh_chi_phi(a: int, b: int, c: int, t: int, n: int, m: int) -> int:
    return t * a + n * b + m * c


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 6:
        a, b, c, t, n, m = map(int, tokens[:6])
        print(f"Tổng chi phí là: {tinh_chi_phi(a, b, c, t, n, m)}")
