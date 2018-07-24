#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__': 

    primes = dict()

    for i in range(1001, 10001, 2):

        if util.is_prime(i):
            perm = list(str(i))
            perm.sort()
            perm = int(''.join(perm))

            if perm not in primes:
                primes[perm] = []

            primes[perm].append(i)

    for k in primes.keys():

        if len(primes[k]) >= 3:
            for j in range(0, len(primes[k])-2):
                for i in range(j+1, len(primes[k])-1):
                    dif = primes[k][i] - primes[k][j]
    
                    if primes[k][i] + dif in primes[k]:
                        print(primes[k][j], primes[k][i], primes[k][i] + dif)


