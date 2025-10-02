a = list(map(float, input("Nhập a, b, c: ").split()))
a.sort()
if a[0] + a[1] > a[2]:
    p = (a[0] + a[1] + a[2]) / 2
    s = (p * (p - a[0]) * (p - a[1]) * (p - a[2])) ** 0.5
    print("Diện tích tam giác là:", s)
else:
    print("Khong phai 3 canh cua tam giac")