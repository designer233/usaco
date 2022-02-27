# Complete the solve function below.
def solve(s):
    lst = s.split(" ")

    res = []
    for item in lst:
        res.append(item.capitalize())
        
    return " ".join(res)
