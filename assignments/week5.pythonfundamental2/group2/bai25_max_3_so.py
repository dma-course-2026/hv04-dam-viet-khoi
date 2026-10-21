import sys


def tim_max_3(a: int, b: int, c: int) -> int:
    return max(a, b, c)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        a, b, c = map(int, tokens[:3])
        print(f"Giá trị lớn nhất trong 3 số là: {tim_max_3(a, b, c)}")
