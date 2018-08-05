#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Euler%27s_totient_function

import sys
import math
from fractions import gcd
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':
    
    limit = 1000000
    count = 0
    phi = [i for i in range(limit+1)]

    for i in range(2, limit+1):
        if phi[i] == i:
            for j in range(2*i, limit+1, i):
                phi[j] -= phi[j]//i
            phi[i] -= 1

        count += phi[i]

    print(count)

