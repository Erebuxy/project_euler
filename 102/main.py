#!/usr/bin/env python3

import numpy as np

if __name__ == '__main__':

    f_name = './102/p102_triangles.txt'
    f = open(f_name)

    count = 0
    for line in f:
        line = line.split(',')
        line = [int(i) for i in line]

        a1 = np.arctan2(line[0], line[1])
        a2 = np.arctan2(line[2], line[3])
        a3 = np.arctan2(line[4], line[5])
        
        a_list = [a1, a2, a3]
        a_list.sort()

        a1 = a_list[0]
        a2 = a_list[1]
        a3 = a_list[2]

        if a2 - a1 > np.pi or a3 - a2 > np.pi or 2 * np.pi - (a3 - a1) > np.pi:
            continue
        count += 1

    print(count)

        

