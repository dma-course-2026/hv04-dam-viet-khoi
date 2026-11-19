n = int(input().strip())
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    so_ngay = 366
else:
    so_ngay = 365
print(f"Số ngày của năm {n} là {so_ngay}")
