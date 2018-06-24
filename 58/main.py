#!/usr/bin/env python3

import random

# Source: https://inventwithpython.com/hacking/chapter23.html
def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num

    return True

if __name__ == '__main__':

    limit = 0.1

    cur = 9
    length = 5
    dia_count = 3
    dia_total = 9
    while True:
        for _ in range(4):
            cur += length - 1
            if rabinMiller(cur):
                dia_count += 1

        if (dia_count / dia_total) < limit:
            print(length)
            break

        length += 2
        dia_total += 4
