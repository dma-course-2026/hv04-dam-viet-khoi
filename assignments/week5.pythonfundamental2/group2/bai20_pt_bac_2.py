import math
import sys


def giai_pt_bac_2(a: float, b: float, c: float) -> tuple[str, list[float]]:
    if a == 0:
        if b == 0:
            if c == 0:
                return "VO_SO_NGHIEM", []
            return "VO_NGHIEM", []
        return "MOT_NGHIEM", [-c / b]
    delta = b * b - 4 * a * c
    if delta < 0:
        return "VO_NGHIEM", []
    if math.isclose(delta, 0.0, abs_tol=1e-12):
        return "NGHIEM_KEP", [-b / (2 * a)]
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    return "HAI_NGHIEM", sorted([x1, x2], reverse=True)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        a, b, c = map(float, tokens[:3])
        trang_thai, nghiem = giai_pt_bac_2(a, b, c)
        if trang_thai == "HAI_NGHIEM":
            print(f"x1 = {nghiem[0]}, x2 = {nghiem[1]}")
        elif trang_thai == "NGHIEM_KEP":
            print(f"Nghiệm kép: x = {nghiem[0]}")
        elif trang_thai == "MOT_NGHIEM":
            print(f"Phương trình có một nghiệm: x = {nghiem[0]}")
        elif trang_thai == "VO_SO_NGHIEM":
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
