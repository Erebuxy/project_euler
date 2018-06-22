#!/usr/bin/env python3
# O(1)

if __name__ == '__main__':
    
    limit = 1000

    limit = limit - 1

    # sum of multiples of 3
    large3 = limit - limit % 3
    sum3   = (3 + large3) * ((large3 - 3)/3 + 1) / 2

    # sum of multiples of 5
    large5 = limit - limit % 5
    sum5   = (5 + large5) * ((large5 - 5)/5 + 1) / 2

    # sum of multiples of 15
    if limit < 15:
        sum15 = 0
    else:
       large15 = limit - limit % 15
       sum15 = (15 + large15) * ((large15 - 15)/15 + 1) /2

    ans = int(sum3 + sum5 - sum15)
    print(ans)


