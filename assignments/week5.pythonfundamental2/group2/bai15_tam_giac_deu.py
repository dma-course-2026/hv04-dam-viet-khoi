import sys


def la_tam_giac_deu(a: float, b: float, c: float) -> bool:
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        return a == b == c
    return False


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        a, b, c = map(float, tokens[:3])
        if la_tam_giac_deu(a, b, c):
            print("Là tam giác đều")
        else:
            print("Không phải tam giác đều")
