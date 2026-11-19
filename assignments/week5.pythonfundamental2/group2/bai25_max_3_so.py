import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 3:
    a, b, c = map(int, tokens[:3])
    res = max(a, b, c)
    print(f"Giá trị lớn nhất trong 3 số là: {res}")
