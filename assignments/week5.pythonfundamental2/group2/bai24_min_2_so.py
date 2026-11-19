tokens = input().split()
if len(tokens) >= 2:
    a, b = int(tokens[0]), int(tokens[1])
else:
    a = int(tokens[0])
    b = int(input().strip())
res = min(a, b)
print(f"{res} là giá trị nhỏ nhất")
