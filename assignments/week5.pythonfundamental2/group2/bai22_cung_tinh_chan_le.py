import sys


def cung_tinh_chan_le(m: int, n: int) -> bool:
    return m % 2 == n % 2


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        m = int(tokens[0])
        n = int(tokens[1])
        if cung_tinh_chan_le(m, n):
            print("ĐÚNG")
        else:
            print("SAI")
