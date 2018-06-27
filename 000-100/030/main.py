#!/usr/bin/env python3

if __name__ == '__main__':

    power = 5
    l = []

    for i in range(10, 1000000):
        cur = i
        s = 0
        while cur > 0:
            s += (cur % 10)**5
            cur = int(cur / 10)

        if s == i:
            l.append(i)

    print(sum(l))
    print(l)

