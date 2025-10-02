s = input()
print(s if (s == 'A' or s == 'a') else chr(ord(s) + 31))