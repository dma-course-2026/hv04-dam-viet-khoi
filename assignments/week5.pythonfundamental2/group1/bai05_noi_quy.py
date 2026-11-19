import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 6:
    a, b, c, t, n, m = map(int, tokens[:6])
    chi_phi = t * a + n * b + m * c
    print(f"Tổng chi phí là: {chi_phi}")
