h, r = list(map(int, input().split()))

for m in range(r):
    for x in range(h):
        for y in range(x+1): # 0,1,2,3,4
            if y == x:
                print("*")
            else:
                print(" ", end="")
    for x in range(h):
        for y in range(h-x-1): # 5,4,3,2,1
            if y == h-x-2:
                print("*")
            else:
                print(" ", end="")
