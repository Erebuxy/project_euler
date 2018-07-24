#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

def primes_num(n):
    cur = n
    cur_div = 2
    count = 0
    while True:
        if cur % cur_div == 0:
            count += 1
            while cur % cur_div == 0:
                cur = int(cur / cur_div)

        if cur == 1:
            break
        if cur_div > math.sqrt(cur):
            count += 1
            break

        if cur_div == 2:
            cur_div += 1
        else:
            cur_div += 2

    return count

if __name__ == '__main__':

    cur = 644

    count = 0
    while True:
        
        if util.is_prime(cur):
            count = 0

        else:
            if primes_num(cur) == 4:
                count += 1
            else:
                count = 0

            if count == 4:
                print(cur - 3)
                break

        cur += 1
