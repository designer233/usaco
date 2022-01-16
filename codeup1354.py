a = int(input())

for x in range(a):
    for y in range(a-x):
        print("*", end="")
    print()
