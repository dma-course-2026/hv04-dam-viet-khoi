tokens = input().split()
if len(tokens) >= 2:
    a, n = int(tokens[0]), int(tokens[1])
else:
    a = int(tokens[0])
    n = int(input().strip())
res = a ** n
print(f"{a} lũy thừa {n} = {res}")
