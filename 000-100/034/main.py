#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    ft = [math.factorial(i) for i in range(10)]

    l = []
    for i in range(11, 2600000):
        cur = list(str(i))
        cur = [ft[int(j)] for j in cur]
        if sum(cur) == i:
            l.append(i)

    print(sum(l))
    print(l)
