import sys

lines = sys.stdin.read().split()
if len(lines) >= 2:
    cu, moi = int(lines[-2]), int(lines[-1])
    kwh = moi - cu
    if kwh < 0:
        kwh = 0
    if kwh <= 60:
        tien = kwh * 5.0
    elif kwh <= 160:
        tien = 60 * 5.0 + (kwh - 60) * 8.0
    else:
        tien = 60 * 5.0 + 100 * 8.0 + (kwh - 160) * 10.0
    print(f"Số tiền phải trả là: {tien:.2f}")
