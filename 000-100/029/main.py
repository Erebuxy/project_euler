#!/usr/bin/env python3

if __name__ == '__main__':

    limit = 100

    s = set()
    for a in range(2, limit+1):
        for b in range(2, limit+1):
            s.add(a**b)

    print(len(s))
