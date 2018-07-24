#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    limit = 1000000

    l = []
    for i in range(1, limit+1):
        if util.is_palindromic(i):
            b = int('{0:b}'.format(i))
            if util.is_palindromic(b):
                l.append(i)

    print(sum(l))
    print(l)
