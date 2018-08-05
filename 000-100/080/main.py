#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

import decimal

decimal.getcontext().prec = 102

def digit_sum(n):
    if math.sqrt(n) % 1 == 0:
        return 0

    s = str(decimal.Decimal(n).sqrt())
    return sum([int(i) for i in s[:101] if i != '.'])


if __name__ == '__main__':

    ans = 0
    for i in range(100):
        ans += digit_sum(i)

    print(ans)
