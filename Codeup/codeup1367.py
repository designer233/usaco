a = int(input())

for x in range (a):
    for y in range (a-x-1):
        print(" ", end="")
    for z in range(a):
        print("*", end="")
    print()
