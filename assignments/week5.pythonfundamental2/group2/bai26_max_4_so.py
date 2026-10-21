import sys


def tim_max_4(a: int, b: int, c: int, d: int) -> int:
    return max(a, b, c, d)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 4:
        a, b, c, d = map(int, tokens[:4])
        print(tim_max_4(a, b, c, d))
