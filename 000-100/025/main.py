#!/usr/bin/env python3

import math

if __name__ == '__main__':

    digit = 1000

    cur = 1
    pre = 1
    indx = 2
    while True:
        
        if math.log10(cur) >= digit - 1:
            print(indx)
            break

        cur = cur + pre
        pre = cur - pre
        indx += 1
