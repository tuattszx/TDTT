a, b = map(int, input().split())
print(f"{a * b - (min(a, b) / 2) ** 2 * 3.14:.2f}")