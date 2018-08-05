#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util


plog = lambda *args: print(args) if False else None

def digit_fac(n):
    ans = 0
    for d in str(n):
        ans += math.factorial(int(d))
    return ans

def find_chain(number, d, l=[]):
    if number in d:
        if len(l) == 0:
            return
        else:
            # Check for repeat
            for i in range(len(l)):
                if l[i] in d[number]:
                    indx = d[number].index(l[i])
                    for j in range(i+1):
                        d[l[j]] = l[j:] + d[number][:indx]
                        plog("add", l[j])
                    return
            # No repeat from previous results
            for i in range(len(l)):
                d[l[i]] = l[i:] + d[number]
                plog("add", l[i])


    else:
        next_n = digit_fac(number)
        next_l = l + [number]
        if next_n in next_l:
            indx = next_l.index(next_n)
            for i in range(indx+1):
                d[next_l[i]] = next_l[i:]
                plog("add", next_l[i])

        else:
            find_chain(next_n, d, next_l)



if __name__ == '__main__':

    limit = 1000000

    d = {}
    ans = 0

    for i in range(limit):
        plog(i, '='*10)
        find_chain(i, d)
        if len(d[i]) == 60:
            ans += 1

    print(ans)

