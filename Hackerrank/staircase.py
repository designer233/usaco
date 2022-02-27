#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for x in range(n):

        for _ in range(n-x-1):
            print(" ", end="")

        for _ in range(x+1):
            print("#", end="")

        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
