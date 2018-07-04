#!/usr/bin/env python3

import sys
import math 
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    limit = 1000

    max_count = 0
    max_p = -1
    for p in range(4, limit+1, 2):

        count = 0
        for i in range(int(p/3), math.ceil(p/2)):
            for j in range(1, i):
                k = p - i - j
                if i**2 == j**2 + k**2:
                    count += 1
            
        if count > max_count:
            max_count = count
            max_p = p

    print(max_p)
