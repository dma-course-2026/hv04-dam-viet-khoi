import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 3:
    d1, d2, d3 = map(float, tokens[:3])
    dtb = (d1 + d2 + d3) / 3
    ket_qua = "Đậu" if dtb >= 5.0 else "Rớt"
    print(f"Điểm trung bình là: {dtb:.1f}")
    print(ket_qua)
