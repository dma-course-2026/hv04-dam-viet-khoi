import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 3:
    a, b, c = map(float, tokens[:3])
    if a + b > c and a + c > b and b + c > a and (a == b or b == c or a == c):
        print("Là tam giác cân")
    else:
        print("Không phải tam giác cân")
