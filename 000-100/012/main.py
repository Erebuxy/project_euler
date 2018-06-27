#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
import util

def num_of_divisor(n):
    d = dict()
    
    cur = 2
    while True:
        if util.is_prime(cur):
            d[cur] = 0

            while n % cur == 0:
                n /= cur
                d[cur] += 1

            n = int(n)

            if n == 1:
                break
            elif util.is_prime(n):
                d[n] = 1
                break
        
        if cur == 2:
            cur += 1
        else:
            cur += 2

    ans = 1
    for (_, v) in d.items():
        ans *= v + 1
    
    return ans

if __name__ == '__main__':

    limit = 500

    cur_num = 2
    cur_tri = 1

    while True:
        cur_tri += cur_num
        cur_num += 1

        nd = num_of_divisor(cur_tri)
        if nd > limit:
            print(cur_tri)
            break
