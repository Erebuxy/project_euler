#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':
    
    count = 0

    cur = 1
    start = 1

    while True:

        pre_c = count

        for i in range(start, 10):
            dig = int(math.log10(i**cur)) + 1
            if dig == cur:
                count += 1
            else:
                start = i

        if pre_c == count:
            print(count)
            break

        cur += 1
