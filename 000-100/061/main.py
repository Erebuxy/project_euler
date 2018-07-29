#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, '../../')
import util

if __name__ == '__main__':
    
    nums = dict()

    n = 1
    while True:
        tria = n * (n + 1) // 2
        if tria >= 1000 and tria % 100 >= 10:
            pre = tria // 100

            if pre not in nums:
                nums[pre] = []

            nums[pre].append((3, tria))

        squa = n * n
        if squa >= 1000 and squa % 100 >= 10:
            pre = squa // 100

            if pre not in nums:
                nums[pre] = []

            nums[pre].append((4, squa))

        pent = n * (3*n - 1) // 2
        if pent >= 1000 and pent % 100 >= 10:
            pre = pent // 100

            if pre not in nums:
                nums[pre] = []

            nums[pre].append((5, pent))

        hexa = n * (2*n - 1)
        if hexa >= 1000 and hexa % 100 >= 10:
            pre = hexa // 100

            if pre not in nums:
                nums[pre] = []

            nums[pre].append((6, hexa))

        hept = n * (5*n - 3) // 2
        if hept >= 1000 and hept % 100 >= 10:
            pre = hept // 100

            if pre not in nums:
                nums[pre] = []

            nums[pre].append((7, hept))

        octa = n * (3*n - 2)
        if octa >= 1000 and octa % 100 >= 10:
            pre = octa // 100

            if pre not in nums:
                nums[pre] = []

            nums[pre].append((8, octa))

        n += 1

        if tria > 9999:
            break

    pre_nums = []
    for k in nums.keys():
        for ty, n in nums[k]:
            if n % 100 in nums:
                pre_nums.append(([ty], [n]))
    
    for _ in range(5):
        cur_nums = []
        for it in pre_nums:
            suf = it[1][-1] % 100
            for ty, n in nums[suf]:
                if n % 100 in nums and ty not in it[0]:
                    cur_nums.append((it[0] + [ty], it[1] + [n]))

        pre_nums = cur_nums 

    for _, num in cur_nums:
        if num[0] // 100 == num[-1] % 100:
            print(sum(num), num)
