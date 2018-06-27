#!/usr/bin/env python3

import math

if __name__ == '__main__':

    num = math.factorial(100)
    l = list(str(num))
    print(sum([int(i) for i in l]))
