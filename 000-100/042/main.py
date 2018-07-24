#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    f_name = './p042_words.txt'
    count = 0

    t_set = set()
    for i in range(1,100):
        t_set.add(int(0.5*i*(i+1)))

    line = open(f_name).readline()
    line = line.split(',')
    line = [word.strip('"') for word in line]
    for word in line:
        s = 0
        for i in word:
            s += ord(i) - ord('A') + 1

        if s in t_set:
            count += 1

    print(count)

