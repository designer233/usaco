N, C = list(map(int, input().split()))
arr = list(map(int, input().split()))

#N, C = [9, 6]
#arr = [160, 165, 164, 165, 150, 165, 168, 145, 170]

arr.sort()
#print(arr)

for x in range(N):
    print(arr[x], end= " ")
    if (x+1) % C == 0:
        print()
