n = int(input())
arr = list(map(int, input().split()))

for x in range(len(arr)):
    print(f'{x+1}:', end = " ")
    for y in range(len(arr)):
        if x != y:
            if arr[x] < arr[y]:
                print('<', end = " ")
            elif arr[x] > arr[y]:
                print('>', end = " ")
            else:
                print('=', end = " ")

    print()
