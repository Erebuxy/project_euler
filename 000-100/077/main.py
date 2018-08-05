#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

def number_of_sum(m, n, d):
    if n == 0:
        return 1
    elif m == 1:
        return 0
    elif m == 2 and (n % 2) != 0:
        return 0

    if (m, n) in d:
        return d[(m, n)]

    ans = 0
    ans += number_of_sum(2, n-2, d)
    for i in range(3, min(m+1, n+1), 2):
        if util.is_prime(i):
            ans += number_of_sum(i, n-i, d)

    d[(m, n)] = ans
    return ans



if __name__ == '__main__':

    limit = 5000

    cur = 16
    pre = 8

    d = {}

    while True:

        num = number_of_sum(cur-1, cur, d)

        if num < limit:
            if cur / pre == 2:
                cur *= 2
                pre *= 2
            elif pre < cur:
                cur, pre = int(cur + (cur - pre)/2), cur
            else:
                cur, pre = int((cur + pre) / 2), cur

        else:
            if pre < cur:
                cur, pre = int((cur + pre) / 2), cur
            else:
                cur, pre = int(cur + (cur - pre)/2), cur

        if abs(pre - cur) <= 1:
            ans = max(pre, cur)
            print(ans, number_of_sum(ans-1, ans, d))
            break


