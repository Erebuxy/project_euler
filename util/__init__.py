#!/usr/bin/env python3

import math
import random

# Source: https://inventwithpython.com/hacking/chapter23.html
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

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

def is_palindromic(n):
    return n == reverse_digit(n)

def concatenate_digit(a, b):
    return int(str(a) + str(b))

def reverse_digit(n):
    return int(str(n)[::-1])

def c(n, r):
    return int(math.factorial(n) / (math.factorial(r)*math.factorial(n-r)))
