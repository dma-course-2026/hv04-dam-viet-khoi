def la_alphabet(ch: str) -> bool:
    return len(ch) == 1 and ("a" <= ch <= "z" or "A" <= ch <= "Z")


if __name__ == "__main__":
    ch = input().strip()
    if la_alphabet(ch):
        print(f"{ch} là ký tự Alphabet")
    else:
        print(f"{ch} không phải là ký tự Alphabet")
