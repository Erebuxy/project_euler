#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    l = []

    for dem in range(10, 100):
        for num in range(10, dem):
            if dem % 10 == 0:
                continue
            if num % 11 == 0 and dem % 11 == 0:
                continue
            if num % 10 != int(dem / 10):
                continue

            n = int(num / 10)
            d = dem % 10
            if num / dem == n / d:
                l.append((num, dem))

    print(l)
