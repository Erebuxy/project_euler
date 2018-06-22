#!/usr/bin/env python3

if __name__ == '__main__':

    limit = 2000000
    
    is_primes = [True for _ in range(limit + 1)]

    ans = 0
    for i in range(2, limit+1):
        if is_primes[i]:
            ans += i

            for j in range(2*i, limit+1, i):
                is_primes[j] = False

    print(ans)
