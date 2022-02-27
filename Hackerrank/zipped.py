# Enter your code here. Read input from STDIN. Print output to STDOUT
stu_num, sub_num = map(int, input().split())

subjects = []
for x in range(sub_num):
    subjects.append(list(map(float, input().split())))

avg =[]
for y in zip(*subjects):
    avg.append(sum(y)/len(y))

for x in avg:
#    print(x)
    print("%.1f" %x)
