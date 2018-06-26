#!/usr/bin/env python3

import numpy as np

def function(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 -\
           n**9 + n**10

if __name__ == '__main__':

    un = [function(i) for i in range(1, 11)]

    ans = 0
    for i in range(1, 11):
        if i == 1:
            ans += 1
        else:
            a = []
            b = []
            for j in range(i):
                a.append([(j+1)**k for k in range(i)])
                b.append(un[j])

            fn = np.linalg.solve(a, b)
            fit = sum([fn[j] * (i+1)**j for j in range(i)])
            ans += fit

    print(int(ans))
