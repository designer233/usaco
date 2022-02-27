a = int(input())

marker = " "

for x in range(a):
    for y in range(a):
        if x == 0 or x == a-1 or y == 0 or y == a-1 or x == y or x + y == a-1:
            marker = '*'
        else:
            marker = ' '
        print(marker, end="")
        #marker = ' '
    print()
