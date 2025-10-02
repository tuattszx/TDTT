s = input("Nhập chuỗi kí tự thường: ")
print("Mã unicode của chuỗi là: ")
for i in s:
    print(f"{i}: {ord(i)}")
s = s.upper()
print("Chuỗi sau khi in hoa là: ", s)
