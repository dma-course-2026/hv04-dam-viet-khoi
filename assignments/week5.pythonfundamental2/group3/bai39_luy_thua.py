import sys


def luy_thua(a: float | int, n: int) -> float | int:
    return a**n


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        raw_a = tokens[0]
        a = float(raw_a) if "." in raw_a else int(raw_a)
        n = int(tokens[1])
        print(f"{a} lũy thừa {n} = {luy_thua(a, n)}")
