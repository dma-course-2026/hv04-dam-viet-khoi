import sys


def dien_tich_con_lai(a: float, b: float, pi: float = 3.14) -> float:
    return a * b - pi * (a / 2) ** 2


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        a = float(tokens[0])
        b = float(tokens[1])
        res = dien_tich_con_lai(a, b)
        print(f"Diện tích còn lại: {res:.2f}")
