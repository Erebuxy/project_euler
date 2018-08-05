#!/usr/bin/env python3

import sys
import math
from fractions import gcd
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    limit = 12000
    count = 0

    sieve = [[True for _ in range(math.ceil(i/2))] for i in range(limit+1)]
    
    for num in range(1, math.ceil(limit/2)):
        for den in range(2*num+1, min(limit+1, num*3)):
            
            if sieve[den][num]:
                count += 1

                for k in range(2, limit//den + 1):
                    sieve[den*k][num*k] = False

    print(count)
