#!/usr/bin/env python3

if __name__ == '__main__':

    width = 1001

    cur = 1
    cur_w = 3
    ans = 1
    while cur_w <= width:

        ans += 4 * cur + 10 * (cur_w - 1)
        cur += 4 * (cur_w - 1)
        cur_w += 2

    print(ans)
