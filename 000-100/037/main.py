#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    count = 11
    l = set()

    cur = 11
    while count > 0:
        if util.is_prime(cur):
            leng = len(str(cur))

            valid = True
            cur_left = cur
            cur_right = cur 
            for i in range(leng-1):
                cur_left = int(str(cur_left)[1:])
                cur_right = int(str(cur_right)[:-1])

                if util.is_prime(cur_left) and util.is_prime(cur_right):
                    pass
                else:
                    valid = False
                    break

            if valid:
                l.add(cur)
                count -= 1

        cur += 2

    print(sum(l))
    print(list(l))
