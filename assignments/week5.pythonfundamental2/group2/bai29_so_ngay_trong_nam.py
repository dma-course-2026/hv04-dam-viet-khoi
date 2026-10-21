def so_ngay_trong_nam(nam: int) -> int:
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return 366
    return 365


if __name__ == "__main__":
    nam = int(input().strip())
    print(f"Số ngày của năm {nam} là {so_ngay_trong_nam(nam)}")
