#!/usr/bin/env python3
# O(n^2)

from math import *

if __name__ == '__main__':

    limit = 1000

    for b in range(2, limit):
        for a in range(1, b):

            c = 1000 - a - b

            if a**2 + b**2 == c**2:
                print(a * b * c)
                print(a, b, c)

