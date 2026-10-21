tokens = input().split()
if len(tokens) >= 2:
    a, b = float(tokens[0]), float(tokens[1])
else:
    a = float(tokens[0])
    b = float(input().strip())

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Phương trình có một nghiệm: x = {x}")
