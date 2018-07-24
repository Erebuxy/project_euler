#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    l = []

    for i in range(1000, 80000):

        for j in range(1, 100):
            if i % j == 0:
                k = int(i / j)

                if util.is_pandigital(util.conca_digit(i, j, k)):
                    l.append(i)
                    break

    print(sum(l))
    print(l)
