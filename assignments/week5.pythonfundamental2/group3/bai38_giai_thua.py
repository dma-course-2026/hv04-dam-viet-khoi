n = int(input().strip())
res = 1
for i in range(1, n + 1):
    res *= i
print(f"{n} giai thừa = {res}")
