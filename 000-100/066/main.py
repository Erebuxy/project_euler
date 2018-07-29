#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Pell%27s_equation
# https://en.wikipedia.org/wiki/Chakravala_method

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    limit = 1000
    max_d = 2
    max_num = 3

    for d in range(2, limit+1):

        if int(math.sqrt(d))**2 == d:
            continue
        
        m = m0 = int(round(math.sqrt(d)))
        a, b, k = m, 1, m**2 - d

        while k != 1:

            dif = (m + m0) % abs(k)
            m = m0 - dif
            if abs((m + abs(k))**2 - d) < abs(m**2 - d):
                m += abs(k)

            a, b, k = (a*m + d*b) // abs(k), (a + b*m) // abs(k), (m**2 - d) // k

        if a > max_num:
            max_d = d
            max_num = a

    print(max_d)
    print(max_num)

