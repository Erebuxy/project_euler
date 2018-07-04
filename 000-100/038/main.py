#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    ans = -1
    for i in range(10000, 20000, 2):
        org = int(i / 2)
        if util.is_pandigital(util.conca_digit(i, org)):
            ans = org

    print(util.conca_digit(ans, ans*2))
