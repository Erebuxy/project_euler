#!/usr/bin/env python3

if __name__ == '__main__':

    limit = 100

    max_sum = 0

    for a in range(10, 100):
        if a % 10 == 0:
            continue

        for b in range(1, 100):
            cur = a**b
            cur_sum = sum([int(i) for i in str(cur)])

            if cur_sum > max_sum:
                max_sum = cur_sum

    print(max_sum)
