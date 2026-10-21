import sys


def giai_bpt_bac_1(a: float, b: float) -> tuple[str, str]:
    if a > 0:
        val = -b / a
        return "NGHIEM", f"x >= {val}"
    if a < 0:
        val = -b / a
        return "NGHIEM", f"x <= {val}"
    if b >= 0:
        return "VO_SO_NGHIEM", "Đúng với mọi x"
    return "VO_NGHIEM", "Vô nghiệm"


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        a = float(tokens[0])
        b = float(tokens[1])
        trang_thai, ket_qua = giai_bpt_bac_1(a, b)
        if trang_thai == "NGHIEM":
            print(f"Bất phương trình có nghiệm: {ket_qua}")
        else:
            print(ket_qua)
