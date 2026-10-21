import sys


def tinh_tien_dien(cu: int, moi: int) -> float:
    kwh = max(0, moi - cu)
    if kwh <= 60:
        tien = kwh * 5
    elif kwh <= 160:
        tien = 60 * 5 + (kwh - 60) * 8
    else:
        tien = 60 * 5 + 100 * 8 + (kwh - 160) * 10
    return float(tien)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        cu = int(tokens[-2])
        moi = int(tokens[-1])
        tien = tinh_tien_dien(cu, moi)
        print(f"Số tiền phải trả là: {tien:.2f}")
