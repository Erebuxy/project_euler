#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':

    d = {}

    with open('p079_keylog.txt') as f:
        for line in f.readlines():
            l = line.strip()

            if l[0] not in d:
                d[l[0]] = set()
            if l[1] not in d:
                d[l[1]] = set()
            if l[2] not in d:
                d[l[2]] = set()

            d[l[1]].add(l[0])
            d[l[2]].add(l[0])
            d[l[2]].add(l[1])

    ans = ''
    while len(d) != 0:
        for (key, item) in d.items():
            if len(item) == 0:
                ans += key
                for k in d.keys():
                    d[k].discard(key)

                d.pop(key)
                break
    print(ans)

