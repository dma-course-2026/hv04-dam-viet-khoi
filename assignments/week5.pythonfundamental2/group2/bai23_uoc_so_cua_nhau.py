import sys


def kiem_tra_uoc(a: int, b: int) -> tuple[bool, bool]:
    a_la_uoc_b = (a != 0) and (b % a == 0)
    b_la_uoc_a = (b != 0) and (a % b == 0)
    return a_la_uoc_b, b_la_uoc_a


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        a = int(tokens[0])
        b = int(tokens[1])
        a_uoc_b, b_uoc_a = kiem_tra_uoc(a, b)
        if b_uoc_a:
            print(f"{b} là ước của {a}")
        else:
            print(f"{b} không là ước của {a}")
        if a_uoc_b:
            print(f"{a} là ước của {b}")
        else:
            print(f"{a} không là ước của {b}")
