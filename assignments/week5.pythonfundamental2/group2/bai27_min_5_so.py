import sys


def tim_min_5(a: float, b: float, c: float, d: float, e: float) -> float:
    return min(a, b, c, d, e)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 5:
        a, b, c, d, e = map(float, tokens[:5])
        print(tim_min_5(a, b, c, d, e))
