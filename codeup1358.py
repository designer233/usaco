n = int(input())

for x in range(0, n, 2): # 0, 2, 4
    for z in range((n-x)//2): # 5, 3, 1,
        print(" ", end="")
    for y in range(x+1): # 1, 3, 5
        print("*", end = "" ) 
    print()
