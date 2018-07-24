#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    limit = 1000000
    slot = [True for i in range(int(limit/10/2))]
    prime = [2]

    for i in range(1, len(slot)):
        if slot[i]:
            prime.append(2*i + 1)
            for j in range(i + 2*i + 1, len(slot), 2*i + 1):
                slot[j] = False

    ans = (953, 21)
    count = 22
    while count < len(prime):
        if count % 2 == 0:
            s = sum(prime[:count])
            
            if s > limit:
                break

            if util.is_prime(s):
                ans = (s, count)

        else:
            for i in range(len(prime) - count):
                s = sum(prime[i:i+count])

                if s > limit:
                    break
                
                if util.is_prime(s):
                    ans = (s, count)
                    break

        count += 1

    print(ans[0])
    print(ans[1])

