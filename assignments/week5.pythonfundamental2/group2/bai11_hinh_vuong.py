def hinh_vuong(a: float) -> tuple[float, float]:
    return a * a, 4 * a


if __name__ == "__main__":
    a = float(input().strip())
    dt, cv = hinh_vuong(a)
    print(f"Diện tích {dt}, Chu vi {cv}")
