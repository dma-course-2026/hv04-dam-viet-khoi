import sys


def dong_ho_sau_1_giay(h: int, p: int, s: int) -> tuple[int, int, int]:
    tong_giay = (h * 3600 + p * 60 + s + 1) % 86400
    gio, rem = divmod(tong_giay, 3600)
    phut, giay = divmod(rem, 60)
    return gio, phut, giay


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        h, p, s = map(int, tokens[:3])
        nh, np, ns = dong_ho_sau_1_giay(h, p, s)
        print(f"{nh} {np} {ns}")
