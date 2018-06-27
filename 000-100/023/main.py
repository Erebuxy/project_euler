#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
import util 

if __name__ == '__main__':

    limit = 28123

    is_sum = [False for _ in range(limit+1)]
    abd_num = []

    ans = 0
    for i in range(1, limit+1):
        if not is_sum[i]:
            ans += i

        if util.sum_of_divisors(i) > i:
            abd_num.append(i)
            for abd in abd_num:
                if abd + i <= limit:
                    is_sum[abd+i] = True
                else:
                    break

    print(ans)


