#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    max_len = 0
    ans = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            cur = 0
            while True:
                f = cur**2 + a * cur + b
                if util.is_prime(f):
                    cur += 1
                else:
                    if cur > max_len:
                        max_len = cur
                        ans = a * b
                    break

    print(ans)
