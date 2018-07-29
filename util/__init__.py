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

def prime_sieve(n):
    if n < 2:
        return []

    p = [2]
    l = [True for _ in range(int((n-1)/2))]
    for i in range(len(l)):
        if l[i]:
            num = 2 * i + 3
            p.append(num)
            for j in range(i + num, len(l), num):
                l[j] = False

    return p

def is_palindromic(n):
    return n == reverse_digit(n)

def is_pandigital(n):
    s = str(n)
    if len(s) != 9:
        return False

    for i in range(1, 10):
        if str(i) not in s:
            return False

    return True

def conca_digit(*nums):
    return concatenate_digit(*nums)

def concatenate_digit(*nums):
    return int(''.join([str(i) for i in nums]))

def reverse_digit(n):
    return int(str(n)[::-1])

def c(n, r):
    return int(math.factorial(n) / (math.factorial(r)*math.factorial(n-r)))

def sum_of_divisors(n):
    if n <= 1:
        return 0

    ans = 1
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            ans += i + n / i

    if math.sqrt(n) == int(math.sqrt(n)):
        ans += math.sqrt(n)

    return int(ans)

def get_cycle(num, dem):
    intg = int(num / dem)
    num -= intg * dem

    digit = []
    num_history = []
    recurring_start = -1
    while num != 0:
        num_history.append(num)
        num *= 10
        cur_digit = int(num / dem)
        digit.append(str(cur_digit))

        num = num - cur_digit * dem
        if num in num_history:
            recurring_start = num_history.index(num)
            break

    if recurring_start == -1:
        return str(intg) + '.' + ''.join(digit), 0
    else:
        ans_str = str(intg) + '.' + ''.join(digit[:recurring_start]) +\
                  '(' + ''.join(digit[recurring_start:]) + ')'
        return ans_str, len(digit) - recurring_start

def sorted_char_list(n):
    l = list(str(n))
    l.sort()
    return ''.join(l)

def is_permutation(a, b):
    return sorted_char_list(a) == sorted_char_list(b)


