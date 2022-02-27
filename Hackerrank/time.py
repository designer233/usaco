#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    lst = s.split(':')

    if lst[0] == '12':
        if lst[2][-2:] == 'AM':
            lst[0] = '00' 
    elif lst[2][-2:] == 'PM':
        lst[0] = str(int(lst[0]) + 12)


    lst[2] = lst[2][:-2]
    return ":".join(lst)




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
