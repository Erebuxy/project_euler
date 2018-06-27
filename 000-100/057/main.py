#!/usr/bin/env python3

if __name__ == '__main__':

    limit = 1000

    cur_num = 1
    cur_den = 2

    count = 0

    for _ in range(1, 1001):

        if len(str(cur_den + cur_num)) > len(str(cur_den)):
            count += 1

        temp_num = cur_num
        cur_num = cur_den
        cur_den = 2 * cur_num + temp_num

    print(count)
