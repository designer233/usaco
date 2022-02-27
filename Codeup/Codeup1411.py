N = int(input())
arr = []
for x in range(1, N+1):
    arr.append(x)

for y in range(N-1):
    val = int(input())
    arr.remove(val)
print(arr[0])
