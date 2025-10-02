name = input("Ten chu ho: ")
pre = int(input("Chi so thang truoc: "))
cur = int(input("Chi so thang nay: "))
coin = [1984, 2050, 2380, 2998, 3350, 3460]
total = cur - pre
energy = [50, 50, 100, 100, 100, total]
s = 0
for i in range(6):
    s += min(total, energy[i]) * coin[i]
    total -= min(total, energy[i])
s = int(round(s * 1.08))
print(f"Ho va ten: {name}")
print(f"Tien phai tra la: {s}")