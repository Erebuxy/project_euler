#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    l = [0 for i in range(10001)]
    ans = 0

    for i in range(2, 10000):

        cur = 1
        cur_sum = 0
        while True:
            if i % cur == 0:
                if cur**2 == i:
                    cur_sum += cur
                else:
                    cur_sum += cur + int(i / cur)

            cur += 1
            if cur > i**0.5:
                break

        cur_sum -= i
        if cur_sum < i:
            if l[cur_sum] == i:
                ans += i + cur_sum

        else:
            l[i] = cur_sum

    print(ans)

