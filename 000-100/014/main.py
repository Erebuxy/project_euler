#!/usr/bin/env python3

if __name__ == '__main__':

    limit = int(1e6)

    l = [0 for i in range(limit)]

    ans = (0, 0)
    for i in range(2, len(l)):
        stack = 0
        cur = i

        while cur != 1:
            if cur < i:
                stack += l[cur]
                break

            if cur % 2 == 0:
                cur = int(cur / 2)
            else:
                cur = 3 * cur + 1

            stack += 1
            
        l[i] = stack
        if stack > ans[1]:
            ans = (i , stack)

    print(ans[0])
