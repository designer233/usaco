#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max_value = -math.inf
    min_value = math.inf

    for a in range(len(arr)):
        for b in range(a+1, len(arr)):
            for c in range(b+1, len(arr)):
                for d in range(c+1, len(arr)):
                    #print(arr[a], arr[b], arr[c], arr[d])
                    total = arr[a] + arr[b] + arr[c] + arr[d]

                    max_value = max(max_value, total)
                    min_value = min(min_value, total)
                    
    print(min_value, max_value)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
