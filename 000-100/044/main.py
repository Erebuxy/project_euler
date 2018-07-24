#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../')
import util

def is_pen(n):
    x = (math.sqrt(1 + 24 * n) + 1) / 6
    return x == int(x)

if __name__ == '__main__':

    p = []

    ans_d = float('inf')

    cur = 1
    while True:
        cur_p = int(cur * (3 * cur - 1) / 2)

        for pre_p in p:
            if is_pen(cur_p - pre_p) and is_pen(cur_p + pre_p):
                if cur_p - pre_p < ans_d:
                    ans_d = cur_p - pre_p
                    print(ans_d)
                    break

        if ans_d != float('inf'):
            break

        cur += 1
        p.append(cur_p)

