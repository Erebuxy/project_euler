#!/usr/bin/env python3

def is_palindromic(n):
    return n == reverse(n)

def reverse(n):
    return int(str(n)[::-1])

if __name__ == '__main__':

    num = 10000
    limit = 50

    l = [False for _ in range(num)]
    count = 0

    for i in range(num - 1, 0, -1):
        
        cur = i
        for _ in range(limit):
            cur += reverse(cur)

            if is_palindromic(cur):
                l[i] = True
                count += 1
                break
            elif cur < num:
                if l[cur]:
                    l[i] = True
                    count += 1
                break
    print(num - 1 - count)
            
