import math
import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 3:
    a, b, c = map(float, tokens[:3])
    if a + b > c and a + c > b and b + c > a:
        sides = sorted([a, b, c])
        if math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9):
            print("Là tam giác vuông")
        else:
            print("Không phải tam giác vuông")
    else:
        print("Không phải tam giác vuông")
