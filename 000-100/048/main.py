#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../')
import util

if __name__ == '__main__':

    ans = 0

    for i in range(1, 1001):
        ans += i ** i

    print(str(ans)[-10:])
