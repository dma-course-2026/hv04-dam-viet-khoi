import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 4:
    a, b, c, d = map(int, tokens[:4])
    print(max(a, b, c, d))
