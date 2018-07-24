#!/usr/bin/env python3

import sys
import math
import itertools
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    max_ans = 0

    for n in range(9, 0, -1):
        lex = [str(i) for i in range(1, n+1)]
        for i in itertools.permutations(lex):
            num = int(''.join(i))
            if util.is_prime(num) and num > max_ans:
                max_ans = num

        if max_ans > 0:
            break

    print(max_ans)


