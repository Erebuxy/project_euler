#!/usr/bin/env python3

import math

def c(n, r):
    return int(math.factorial(n) / (math.factorial(r)*math.factorial(n-r)))

if __name__ == '__main__':

    total = 0
    cur = 9

    for i in range(23, 101):

        while cur > 1:
            if c(i, cur) > 1e6:
                cur -= 1
            else:
                break

        total += i - 2 * cur - 1

    print(total)
