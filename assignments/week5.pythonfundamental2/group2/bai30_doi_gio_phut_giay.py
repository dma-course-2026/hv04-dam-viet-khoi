def doi_gio_phut_giay(tong_giay: int) -> tuple[int, int, int]:
    gio, rem = divmod(tong_giay, 3600)
    phut, giay = divmod(rem, 60)
    return gio, phut, giay


if __name__ == "__main__":
    tong_giay = int(input().strip())
    gio, phut, giay = doi_gio_phut_giay(tong_giay)
    print(f"{gio} giờ : {phut} phút : {giay} giây")
