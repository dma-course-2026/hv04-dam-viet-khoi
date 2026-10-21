import math
import sys


def tam_giac(a: float, b: float, c: float) -> tuple[bool, float, float]:
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        cv = a + b + c
        p = cv / 2
        dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return True, cv, dt
    return False, 0.0, 0.0


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        a, b, c = map(float, tokens[:3])
        hop_le, cv, dt = tam_giac(a, b, c)
        if hop_le:
            print(f"Chu vi {cv:.2f}, Diện tích {dt:.2f}")
        else:
            print("Không phải tam giác")
