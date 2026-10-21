tokens = input().split()
if len(tokens) >= 3:
    a = float(tokens[0])
    b = float(tokens[1])
    op = tokens[2]
else:
    a = float(tokens[0])
    b = float(input().strip())
    op = input().strip()

a_display = int(a) if a.is_integer() else a
b_display = int(b) if b.is_integer() else b

if op == "+":
    res = a + b
    res_display = int(res) if isinstance(res, float) and res.is_integer() else res
    print(f"{a_display} + {b_display} = {res_display}")
elif op == "-":
    res = a - b
    res_display = int(res) if isinstance(res, float) and res.is_integer() else res
    print(f"{a_display} - {b_display} = {res_display}")
elif op == "*":
    res = a * b
    res_display = int(res) if isinstance(res, float) and res.is_integer() else res
    print(f"{a_display} * {b_display} = {res_display}")
elif op == "/":
    if b == 0:
        print("Lỗi: Phép chia cho 0")
    else:
        res = a / b
        res_display = int(res) if res.is_integer() else res
        print(f"{a_display} / {b_display} = {res_display}")
