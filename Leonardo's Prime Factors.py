#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    p_list = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53, 59]
    num_prime_fact = 0
    check_prime = 2
    for i in range(len(p_list)):
        if check_prime <= n:
            num_prime_fact += 1
            check_prime *= p_list[i]
        else:
            return num_prime_fact

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
