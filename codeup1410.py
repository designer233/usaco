txt = input().strip()
#txt = "((())()(()))"

o_num = 0
c_num = 0

for x in range(len(txt)):
    if txt[x] == '(':
        o_num += 1
    else:
        c_num += 1

print(o_num, c_num)
