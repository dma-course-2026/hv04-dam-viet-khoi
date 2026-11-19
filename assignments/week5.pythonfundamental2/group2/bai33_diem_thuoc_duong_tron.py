import math
import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 5:
    x0, y0, r, xa, ya = map(float, tokens[:5])
    d = math.hypot(xa - x0, ya - y0)
    if math.isclose(d, r, rel_tol=1e-9):
        print("Điểm A nằm trên đường tròn")
    elif d < r:
        print("Điểm A nằm trong đường tròn")
    else:
        print("Điểm A nằm ngoài đường tròn")
