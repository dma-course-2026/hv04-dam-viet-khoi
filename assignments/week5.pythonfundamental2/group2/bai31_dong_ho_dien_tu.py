tokens = input().split()
if len(tokens) >= 3:
    h, p, s = map(int, tokens[:3])
else:
    h = int(tokens[0])
    p = int(input().strip())
    s = int(input().strip())

tong = (h * 3600 + p * 60 + s + 1) % 86400
h_moi = tong // 3600
p_moi = (tong % 3600) // 60
s_moi = tong % 60
print(f"{h_moi} {p_moi} {s_moi}")
