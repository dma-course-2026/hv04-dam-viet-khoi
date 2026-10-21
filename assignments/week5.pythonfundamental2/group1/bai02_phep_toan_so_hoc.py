tokens = input().split()
if len(tokens) >= 2:
    a, b = int(tokens[0]), int(tokens[1])
else:
    a = int(tokens[0])
    b = int(input().strip())
print(f"Tổng {a + b}, Hiệu {a - b}, Tích {a * b}, Thương {a / b}")
