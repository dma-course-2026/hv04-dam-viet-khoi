import sys


def thuc_hien_phep_toan(a: float, b: float, op: str) -> float | str:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Không thể chia cho 0"
        return a / b
    return "Phép toán không hợp lệ"


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    if len(tokens) >= 3:
        a = float(tokens[0])
        b = float(tokens[1])
        op = tokens[2]
        res = thuc_hien_phep_toan(a, b, op)
        if isinstance(res, (int, float)):
            print(f"{a:g} {op} {b:g} = {res:g}")
        else:
            print(res)
