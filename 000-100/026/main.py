#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    limit = 1000
    max_length = 0
    max_indx = 0
    for i in range(2, limit):
        _, cur_length = util.get_cycle(1, i)
        if cur_length > max_length:
            max_length = cur_length
            max_indx = i

    print(max_indx)
    print(util.get_cycle(1, max_indx))
