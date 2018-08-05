#!/usr/bin/env python3

import sys
import math
from fractions import gcd
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':
    
    num = 3
    den = 7
    limit = 1000000

    fra = num / den
    ans = [-1, -1, -1]

    for i in range(1, limit + 1):

        cur = int(i * num / den)
        cur_num = cur / i
        if cur_num > ans[0] and cur_num != 3 / 7 and gcd(cur, i) == 1:
            ans = [cur / i, cur, i]

    print(ans[1])
    print(ans[1], '/', ans[2], '=', ans[0])

