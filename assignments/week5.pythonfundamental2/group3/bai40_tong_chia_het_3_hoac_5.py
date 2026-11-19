tokens = input().split()
if len(tokens) >= 2:
    m, n = int(tokens[0]), int(tokens[1])
else:
    m = int(tokens[0])
    n = int(input().strip())

tong = sum(i for i in range(m, n + 1) if i % 3 == 0 or i % 5 == 0)
print(f"Kết quả: {tong}")
