a = input()
b = input()
c = input()

if a[-1] == b[0]:
    if b[-1] == c[0]:
        if c[-1] == a[0]:
            print("good")
        else:
            print("bad")
    else:
        print("bad")
else:
    print("bad")
