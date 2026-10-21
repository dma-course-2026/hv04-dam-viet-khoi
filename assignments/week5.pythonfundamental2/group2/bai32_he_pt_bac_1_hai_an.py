import sys


def giai_he_pt_bac_1(
    a: float, b: float, m: float, c: float, d: float, n: float
) -> tuple[str, tuple[float, float] | None]:
    D = a * d - b * c
    Dx = m * d - b * n
    Dy = a * n - m * c
    if D != 0:
        return "NGHIEM_DUY_NHAT", (Dx / D, Dy / D)
    if Dx == 0 and Dy == 0:
        return "VO_SO_NGHIEM", None
    return "VO_NGHIEM", None


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 6:
        a, b, m, c, d, n = map(float, tokens[:6])
        trang_thai, nghiem = giai_he_pt_bac_1(a, b, m, c, d, n)
        if trang_thai == "NGHIEM_DUY_NHAT" and nghiem is not None:
            x, y = nghiem
            print(f"x ≈ {x:.3f}, y ≈ {y:.3f}")
        elif trang_thai == "VO_SO_NGHIEM":
            print("Hệ phương trình có vô số nghiệm")
        else:
            print("Hệ phương trình vô nghiệm")
