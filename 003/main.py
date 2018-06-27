#!/usr/bin/env python3
# O(sqrt(n))

if __name__ == '__main__':

    num = 600851475143

    s = set()
    cur = 2

    while True:

        if cur * cur > num:
            print(int(num))
            break

        while num % cur == 0:
            num /= cur

        if num == 1:
            print(cur)
            break

        if cur == 2:
            cur += 1
        else:
            cur += 2
