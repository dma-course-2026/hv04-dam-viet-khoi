import sys


def xet_diem(d1: float, d2: float, d3: float) -> tuple[float, str]:
    dtb = (d1 + d2 + d3) / 3
    ket_qua = "Đậu" if dtb >= 5.0 else "Rớt"
    return dtb, ket_qua


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        d1, d2, d3 = map(float, tokens[:3])
        dtb, ket_qua = xet_diem(d1, d2, d3)
        print(f"Điểm trung bình là: {dtb:.1f}")
        print(ket_qua)
