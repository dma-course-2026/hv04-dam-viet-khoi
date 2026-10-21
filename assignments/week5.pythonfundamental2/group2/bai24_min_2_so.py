import sys


def tim_min_2(a: int, b: int) -> int:
    return min(a, b)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        a = int(tokens[0])
        b = int(tokens[1])
        print(f"{tim_min_2(a, b)} là giá trị nhỏ nhất")
