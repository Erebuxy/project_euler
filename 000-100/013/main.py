#!/usr/bin/env python3 

if __name__ == '__main__':

    f_name = './num.txt'

    s = 0
    for line in open(f_name):
        s += int(line)

    print(str(s)[:10])
