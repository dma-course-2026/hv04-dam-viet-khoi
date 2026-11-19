s = int(input().strip())
gio, rem = divmod(s, 3600)
phut, giay = divmod(rem, 60)
print(f"{gio} giờ : {phut} phút : {giay} giây")
