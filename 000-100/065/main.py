#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    limit = 100

    num = 1
    den = 0
    for i in range(limit - 1, -1, -1):
        if i == 0:
            cf = 2
        elif i % 3 == 2:
            cf = i // 3 * 2 + 2
        else: 
            cf = 1
        num, den = den, num

        num = cf * den + num

    print(sum([int(i) for i in str(num)]))
    print(num, '/', den, '=', num / den)
    print('e = ', math.e)
