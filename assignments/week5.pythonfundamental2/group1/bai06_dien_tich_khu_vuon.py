tokens = input().split()
if len(tokens) >= 2:
    a, b = float(tokens[0]), float(tokens[1])
else:
    a = float(tokens[0])
    b = float(input().strip())
pi = 3.14
s_hcn = a * b
s_tron = pi * ((a / 2) ** 2)
s_con_lai = s_hcn - s_tron
print(f"Diện tích còn lại: {s_con_lai:.2f}")
