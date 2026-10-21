import math


def hinh_tron(r: float, pi: float = math.pi) -> tuple[float, float]:
    return pi * r * r, 2 * pi * r


if __name__ == "__main__":
    r = float(input().strip())
    dt, cv = hinh_tron(r)
    print(f"Diện tích {dt:.2f}, Chu vi {cv:.2f}")
