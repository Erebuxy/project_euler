#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Pythagorean_triple
import sys
import math
import fractions
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':
    limit = 1500000

    upper = int(math.sqrt(limit / 2))
    d = {}

    ans = 0
    for i in range(2, upper):
        for j in range(1, i):
            if ((i + j) % 2) == 1 and fractions.gcd(i, j) == 1:
                p = 2 * i**2 + 2 * i * j
                p0 = p
                while p <= limit:
                    if p in d and d[p] == True:
                        ans -= 1
                        d[p] = False
                    elif p not in d:
                        ans += 1
                        d[p] = True

                    p += p0

    print(ans)
