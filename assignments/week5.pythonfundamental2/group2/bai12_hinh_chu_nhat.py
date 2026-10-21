import sys


def hinh_chu_nhat(dai: float, rong: float) -> tuple[float, float]:
    return dai * rong, 2 * (dai + rong)


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        dai = float(tokens[0])
        rong = float(tokens[1])
        dt, cv = hinh_chu_nhat(dai, rong)
        print(f"Diện tích {dt}, Chu vi {cv}")
