def fun(s):
    lst = s.split('@')

    if len(lst) < 2 or len(lst[0]) == 0 or len(lst[1]) ==0:
        return False
    
    #print(lst[0], lst[1])
    for item in lst[0]:
        if item not in ['_', '-'] and not item.isalnum():
            return False

    lst = lst[1].split('.')
    
    if len(lst) < 2:
        return False

    #print(lst[0], lst[1])
    if not lst[0].isalnum() or len(lst[1]) > 3:
        return False


    return True
