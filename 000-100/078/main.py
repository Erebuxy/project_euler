#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Partition_(number_theory)
# https://en.wikipedia.org/wiki/Pentagonal_number

import sys
import math
sys.path.insert(0, '../../')
import util


def number_of_sum(n, p):
    i = 0
    qi = 0
    p[n] = 0

    while True:
        qi = int((3 * i**2 - i) / 2)

        if qi > n:
            break

        p[n] += int((-1)**(i-1) * p[n-qi])
        p[n] %= 1000000

        i = -i + 1 if i <= 0 else -i

    return p[n]





if __name__ == '__main__':

    div = 1000000

    ans = 1
    p = {0 : 1}

    while True:
        num = number_of_sum(ans, p)

        if num % div == 0:
            print(ans)
            break

        ans += 1
