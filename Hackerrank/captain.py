# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
txt = input()

lst = list(map(int, txt.split()))
rooms = list(set(lst))


for num in rooms:
    #print("num # = ", num)
    count = 0
    for x in range(len(lst)):
        if lst[x] == num:
            count += 1
            if count >= 2:
                break
    else:
        print(num)
