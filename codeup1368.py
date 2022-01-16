a, b, c = input().split()  # '2 3 L' -> ['2', '3', 'L']
a = int(a)
b = int(b)

if c == "R":
    for x in range (a):
        for y in range (a-x-1):
            print(" ", end="")
        for z in range(b):
            print("*", end="")
        print()
else:
    for x in range (a):
        for y in range (x):
            print(" ", end="")
        for z in range(b):
            print("*", end="")
        print()
