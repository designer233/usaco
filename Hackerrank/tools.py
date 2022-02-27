def merge_the_tools(string, k):
    # your code goes here
    n = 1
    tmp = ""
    for x in string:
        if (x not in tmp): tmp += x
        
        if (n % k == 0):
            print(tmp)
            tmp = ""
            
        n += 1
