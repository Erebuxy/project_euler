#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    cub = dict()

    cur = 1

    while True:

        c = cur ** 3
        c_str = list(str(c))
        c_str.sort()
        c_str = ''.join(c_str)

        if c_str not in cub:
            cub[c_str] = (0, [])

        cub[c_str] = (cub[c_str][0] + 1, cub[c_str][1] + [c])

        if cub[c_str][0] == 5:
            print(' '.join([str(i) for i in cub[c_str][1]]))
            break

        cur += 1
