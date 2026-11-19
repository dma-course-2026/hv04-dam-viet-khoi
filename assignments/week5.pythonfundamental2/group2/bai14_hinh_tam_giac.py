import math
import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 3:
    a, b, c = map(float, tokens[:3])
    if a + b > c and a + c > b and b + c > a:
        cv = a + b + c
        p = cv / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Chu vi {cv:.2f}, Diện tích {s:.2f}")
    else:
        print("Không phải tam giác")
