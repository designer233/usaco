a = int(input())

for x in range(a):
    for y in range(x+1): # 0,1,2,3,4
        print("*", end="")
    print()
for x in range(a):
    for y in range(a-x-1): # 5,4,3,2,1
        print("*", end="")
    print()
