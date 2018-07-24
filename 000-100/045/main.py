#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

def is_pen(n):
    x = (math.sqrt(1 + 24 * n) + 1) / 6
    return x == int(x)

def is_tri(n):
    x = (math.sqrt(1 + 8 * n) - 1) / 2
    return x == int(x)

if __name__ == '__main__':

    cur = 144
    while True:

        hexag = cur * (2* cur - 1)
        if is_pen(hexag) and is_tri(hexag):
            print(hexag)
            break

        cur += 1
