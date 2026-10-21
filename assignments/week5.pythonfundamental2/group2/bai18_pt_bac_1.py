import sys


def giai_pt_bac_1(a: float, b: float) -> tuple[str, float | None]:
    if a == 0:
        if b == 0:
            return "VO_SO_NGHIEM", None
        return "VO_NGHIEM", None
    return "MOT_NGHIEM", -b / a


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        a = float(tokens[0])
        b = float(tokens[1])
        trang_thai, x = giai_pt_bac_1(a, b)
        if trang_thai == "MOT_NGHIEM":
            print(f"Phương trình có một nghiệm: x = {x}")
        elif trang_thai == "VO_SO_NGHIEM":
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
