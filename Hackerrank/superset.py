# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    B = set(map(int, input().split()))
    if A.issuperset(B):
        res = A.difference(B)
        if not res:
            print(False)
            break
    else:
        print(False)
        break

else:
    print(True)
