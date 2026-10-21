tokens = input().split()
if len(tokens) >= 2:
    m, n = int(tokens[0]), int(tokens[1])
else:
    m = int(tokens[0])
    n = int(input().strip())

if m % 2 == n % 2:
    print("ĐÚNG")
else:
    print("SAI")
