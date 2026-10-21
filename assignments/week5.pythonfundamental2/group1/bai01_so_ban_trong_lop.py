def tinh_so_ban(si_so: int) -> int:
    return max(0, si_so - 1)


if __name__ == "__main__":
    si_so = int(input().strip())
    print(f"Vậy bạn có {tinh_so_ban(si_so)} người bạn trong lớp")
