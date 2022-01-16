n = int(input())  # 5
arr = list(map(int, input().split()))  # [1, 2, 3, 4, 5]

for x in range(n):
    for y in range(n):  # 0,1,2,3,4
        print(arr[(y+x) % n], end=" ")

    print()
