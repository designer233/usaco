# Enter your code here. Read input from STDIN. Print output to STDOUT

def myKey(ch):
    ret = ord(ch)
    if (ch.isdigit()): 
        ret += ord('z') + ord('Z')
        if (int(ch) % 2 == 0): ret += ord('9')
    elif (ch.isupper()): 
        ret += ord('z')
        
    return ret


string = input()

res = sorted(string, key=myKey)
res = "".join(res)

print(res)
