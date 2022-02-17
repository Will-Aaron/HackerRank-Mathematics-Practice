#!/bin/python3

import math
import os
import random
import re
import sys

def findDivisors(n):
    #Creates a list of divisors of n by testing all numbers leading up to n
    div_list = []
    i = 1
    while i <= n:
        if n % i == 0:
            div_list.append(i)
        i += 1
    return div_list
def bestDivisor(div_list):
    bestDiv = 1
    bestDiv_sum = 1
    for i in range(len(div_list)):
        #permutes across each divisor
        element_to_sum = div_list[i]
        element_sum = 0
        for digit in str(element_to_sum):
            #permutes across each element to find sum of digits
            element_sum += int(digit)
        if element_sum > bestDiv_sum:
            bestDiv = element_to_sum
            bestDiv_sum = element_sum
        elif element_sum == bestDiv_sum:
            bestDiv = min(bestDiv, element_to_sum)
    return bestDiv
            

if __name__ == '__main__':
    n = int(input())
    result = findDivisors(n)
    result2 = bestDivisor(result)
    print(result2)
