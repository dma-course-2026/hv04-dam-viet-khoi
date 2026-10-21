import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 6:
    a, b, m, c, d, n = map(float, tokens[:6])
    det = a * d - b * c
    dx = m * d - b * n
    dy = a * n - m * c
    if det != 0:
        x = dx / det
        y = dy / det
        print(f"x = {x:.3f}, y = {y:.3f}")
    else:
        if dx == 0 and dy == 0:
            print("Hệ phương trình có vô số nghiệm")
        else:
            print("Hệ phương trình vô nghiệm")
