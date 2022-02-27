txt = input()
b = 0

for x in range(len(txt)):
    b += int(txt[x])
if b % 3 == 0:
    print("1")
else:
    print("0")
