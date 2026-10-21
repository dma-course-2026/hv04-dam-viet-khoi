def so_gap_doi(n: float | int) -> float | int:
    return 2 * n


if __name__ == "__main__":
    raw = input().strip()
    val = float(raw) if "." in raw else int(raw)
    res = so_gap_doi(val)
    print(f"Số gấp đôi của n là: {res}")
