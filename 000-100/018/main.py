#!/usr/bin/env python3

if __name__ == '__main__':

    f_name = './triangle.txt'

    pre = []
    for line in open(f_name):

        line = line.split()
        line = [int(i) for i in line]

        cur = [i for i in line]
        for i in range(len(pre)):
            cur[i] = max(cur[i], line[i] + pre[i])
            cur[i+1] = max(cur[i+1], line[i+1] + pre[i])

        pre= cur

    print(max(pre))
