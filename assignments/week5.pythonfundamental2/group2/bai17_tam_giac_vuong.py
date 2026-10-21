import math
import sys


def la_tam_giac_vuong(a: float, b: float, c: float) -> bool:
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        x, y, z = sorted([a, b, c])
        return math.isclose(x * x + y * y, z * z, rel_tol=1e-9, abs_tol=1e-9)
    return False


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        a, b, c = map(float, tokens[:3])
        if la_tam_giac_vuong(a, b, c):
            print("Là tam giác vuông")
        else:
            print("Không phải tam giác vuông")
