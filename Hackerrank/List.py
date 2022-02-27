if __name__ == '__main__':
    N = int(input())

    tmp = []

    for _ in range(N):
        cmd, *rest = input().split()
        if (cmd == "insert"):
            idx, val = list(map(int, rest))
            tmp.insert(idx, val)
        elif (cmd == "remove"):
            val = list(map(int, rest))
            tmp.remove(val[0])
        elif (cmd == "sort"):
            tmp.sort()
        elif (cmd == "print"):
            print(tmp)
        elif (cmd == "append"):
            val = list(map(int, rest))
            tmp.append(val[0])
        elif (cmd == "pop"):
            tmp.pop()
        elif (cmd == "reverse"):
            tmp.reverse()
