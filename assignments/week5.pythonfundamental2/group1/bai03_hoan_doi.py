tokens = input().split()
if len(tokens) >= 2:
    a, b = int(tokens[0]), int(tokens[1])
else:
    a = int(tokens[0])
    b = int(input().strip())
a, b = b, a
print(f"Sau khi hoán đổi: a = {a}, b = {b}")
