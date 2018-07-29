#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

def count_period(n):
    p = []
    num = (1, int(math.sqrt(n)))
    while True:
        
        p.append(num)
        den = (n - num[1]**2) // num[0]
        int_part = int((math.sqrt(n) + num[1]) / den)

        num = (den, int_part*den - num[1])

        if num in p:
            break

    return len(p)     

if __name__ == '__main__':

    count = 0
    for i in range(10001):
        if int(math.sqrt(i))**2 != i:
            if count_period(i) % 2 == 1:
                count += 1

    print(count)

