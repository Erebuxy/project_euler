#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')
import util

def circular(n):
    s = str(n)
    return int(s[-1] + s[:-1])

if __name__ == '__main__':

    limit = 1000000
    l = set()
    not_l = set()

    for i in range(limit):
        if i in l or i in not_l:
            continue
        if '0' in str(i):
            continue

        if util.is_prime(i):
            temp = set([i])
            cur = i
            valid = True
            for j in range(len(str(i))-1):
                cur = circular(cur)
                temp.add(cur)
                if not util.is_prime(cur):
                    valid = False

            if valid:
                l |= temp
            else:
                not_l |= temp

    print(len(l))
    print(list(l))



