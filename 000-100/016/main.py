#!/usr/bin/env python3

if __name__ == '__main__':

    num = 2**1000
    l = list(str(num))
    l = [int(i) for i in l]
    print(sum(l))
