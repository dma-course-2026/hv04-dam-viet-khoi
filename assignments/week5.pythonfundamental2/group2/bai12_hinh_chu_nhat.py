tokens = input().split()
if len(tokens) >= 2:
    dai, rong = float(tokens[0]), float(tokens[1])
else:
    dai = float(tokens[0])
    rong = float(input().strip())
dt = dai * rong
cv = 2 * (dai + rong)
print(f"Diện tích {dt}, Chu vi {cv}")
