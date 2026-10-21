tokens = input().split()
if len(tokens) >= 2:
    a, b = int(tokens[0]), int(tokens[1])
else:
    a = int(tokens[0])
    b = int(input().strip())

if a != 0 and b % a == 0:
    print(f"{a} là ước của {b}")
else:
    print(f"{a} không là ước của {b}")

if b != 0 and a % b == 0:
    print(f"{b} là ước của {a}")
else:
    print(f"{b} không là ước của {a}")
