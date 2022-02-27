alpha = "abcdefghijklmnopqrstuvwxyz"
arr = [0] * 26

txt = input()
for x in range(len(txt)):
    if 'a' <= txt[x] <='z':
        idx = alpha.index(txt[x])  # txt[x]='b' --> idx=1
        arr[idx] += 1


for x in range(len(alpha)):
    print(f"{alpha[x]}:{arr[x]}")
