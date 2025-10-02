a1, b1, c1, a2, b2, a3 = map(int, input().split())
dtb =  ((a1 + b1 + c1)+( a2 + b2) * 2 + a3 *3)/10
print(f'Điểm trung bình là: {dtb:.1f}')
