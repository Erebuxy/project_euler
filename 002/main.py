#!/usr/bin/env python3
# O(n), n is # of fibonacci number below limit

if __name__ == '__main__':

    limit = 4e6

    cur = 2
    pre = 1

    ans = 0

    while True:

        if cur > limit:
            print(ans)
            break

        if cur % 2 == 0:
            ans += cur

        cur = cur + pre
        pre = cur - pre
