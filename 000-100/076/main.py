#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

def number_of_sum(m, n, d):
    if m == 1 or n == 1 or n == 0:
        return 1

    if (m, n) in d:
        return d[(m, n)]

    ans = 0
    for i in range(1, min(m+1, n+1)):
        ans += number_of_sum(i, n-i, d)

    d[(m, n)] = ans
    return ans



if __name__ == '__main__':

    n = 100

    d = {}

    print(number_of_sum(n-1, n, d))

