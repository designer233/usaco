N = int(input())
arr = []

for x in range(N):
    name, score = input().split()
    score = int(score)
    arr.append([score, name])

arr.sort(reverse=True)
print(arr[2][1])
