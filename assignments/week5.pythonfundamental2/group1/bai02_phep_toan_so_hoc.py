def tinh_phep_toan(a: int, b: int) -> dict[str, float | int]:
    return {
        "tong": a + b,
        "hieu": a - b,
        "tich": a * b,
        "thuong": a / b,
    }


if __name__ == "__main__":
    tokens = input().split()
    if len(tokens) >= 2:
        a, b = int(tokens[0]), int(tokens[1])
    else:
        a = int(tokens[0])
        b = int(input().strip())
    res = tinh_phep_toan(a, b)
    print(f"Tổng {res['tong']}, Hiệu {res['hieu']}, Tích {res['tich']}, Thương {res['thuong']}")
