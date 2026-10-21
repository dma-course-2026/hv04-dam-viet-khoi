tokens = input().split()
if len(tokens) >= 2:
    a, b = float(tokens[0]), float(tokens[1])
else:
    a = float(tokens[0])
    b = float(input().strip())

if a > 0:
    x = -b / a
    print(f"Bất phương trình có nghiệm: x >= {x}")
elif a < 0:
    x = -b / a
    print(f"Bất phương trình có nghiệm: x <= {x}")
else:
    if b >= 0:
        print("Bất phương trình đúng với mọi x")
    else:
        print("Bất phương trình vô nghiệm")
