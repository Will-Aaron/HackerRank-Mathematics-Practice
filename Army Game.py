#!/bin/python3

import os
import sys

#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    bases = (n//2) * (m//2)
    if m % 2 == 1:
        bases += n//2
    if n % 2 == 1:
        bases += m//2
    if (m % 2 == 1) and (n % 2 == 1):
        bases += 1
    return bases

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
