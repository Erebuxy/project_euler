#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    cur = 3
    primes = {2 : True}
    while True:

        if not util.is_prime(cur):

            have_sum = False
            for i in range(int(math.sqrt(cur / 2))+1):
                if (cur - 2 * i**2) in primes:
                    have_sum = True

            if not have_sum:
                print(cur)
                break

        else:
            primes[cur] = True

        cur += 2
