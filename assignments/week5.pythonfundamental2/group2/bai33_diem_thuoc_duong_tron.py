import math
import sys


def vi_tri_diem_duong_tron(
    x0: float, y0: float, r: float, xa: float, ya: float
) -> str:
    d = math.hypot(xa - x0, ya - y0)
    if math.isclose(d, r, rel_tol=1e-9, abs_tol=1e-9):
        return "TRON"
    if d < r:
        return "TRONG"
    return "NGOAI"


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 5:
        x0, y0, r, xa, ya = map(float, tokens[:5])
        vi_tri = vi_tri_diem_duong_tron(x0, y0, r, xa, ya)
        if vi_tri == "TRON":
            print("Điểm A nằm trên đường tròn")
        elif vi_tri == "TRONG":
            print("Điểm A nằm trong đường tròn")
        else:
            print("Điểm A nằm ngoài đường tròn")
