s = int(input())
print(-int(str(-s)[::-1]) if s <= 0 else int(str(s)[::-1]))

