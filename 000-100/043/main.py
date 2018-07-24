#!/usr/bin/env python3

import sys
import math
import itertools
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    lex = [str(i) for i in range(10)]
    l = []
    for i in itertools.permutations(lex):
        if i[0] == '0':
            continue

        if int(''.join(i[1:4])) % 2 == 0 and \
           int(''.join(i[2:5])) % 3 == 0 and \
           int(''.join(i[3:6])) % 5 == 0 and \
           int(''.join(i[4:7])) % 7 == 0 and \
           int(''.join(i[5:8])) % 11 == 0 and \
           int(''.join(i[6:9])) % 13 == 0 and \
           int(''.join(i[7:10])) % 17 == 0:
            l.append(int(''.join(i)))

    print(sum(l))
    print(l)

