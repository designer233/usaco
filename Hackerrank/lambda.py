cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    ret = [0, 1]
    pre1 = 0; pre2=1

    # return a list of fibonacci numbers
    ret = [0, 1]
    if (n == 0): ret.clear()
    elif (n == 1): ret.pop()
        
    for x in range(2, n):
        pre1, pre2 = pre2, pre1 + pre2
        ret.append(pre2)
    return ret
