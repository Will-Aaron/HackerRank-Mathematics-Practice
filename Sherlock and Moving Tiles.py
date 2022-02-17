#!/bin/python3

import os
import sys
import math

#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    time_results = []
    for i in range(len(queries)):
        time_results.append(math.sqrt(2)*(l-math.sqrt(queries[i])) / abs(s1-s2))
    return time_results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
