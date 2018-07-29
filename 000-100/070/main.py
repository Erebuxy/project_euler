#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    limit = 10000000
    primes = util.prime_sieve(5000)

    min_frac = float('inf')
    min_phi = -1
    min_n = -1
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            n = primes[i] * primes[j]
            if n > limit:
                break

            phi = n - primes[i] - primes[j] + 1
            frac = n / phi

            if frac < min_frac and util.is_permutation(n, phi):
                min_frac = frac
                min_phi = phi
                min_n = n

    print(min_n)
    print(min_n, '/', min_phi, '=', min_frac)
