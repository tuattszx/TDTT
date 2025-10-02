h, m = map(int, input("Nhập giờ và phút: ").split())
s = h * 3600 + m * 60
print(f'{h} giờ {m} phút tương ứng với {s} giây')