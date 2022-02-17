#!/bin/python3

import sys

def lowestTriangle(base, area):
    height = 2 * area // base
    if 0.5 * base * height < area:
        return height + 1
    else:
        return height

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
