import sys

tokens = sys.stdin.read().split()
if len(tokens) >= 5:
    vals = [float(x) for x in tokens[:5]]
    res = min(vals)
    print(int(res) if res.is_integer() else res)
