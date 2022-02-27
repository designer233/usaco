a = int(input())

for x in range(a):
    for z in range(x): # 0,1,2,3,4
        print(" ", end="")
    for y in range(a-x): # 5,4,3,2,1
        print("*", end="")
    print()
