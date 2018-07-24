#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')

if __name__ == '__main__':

    l = [True for _ in range(5000)]
    l[0] = False
    primes = [2]
    prime_dict = dict()
    prime_dict[2] = set()

    for i in range(len(l)):
        if l[i]:
            cur = 2*i + 1
            for j in range(i + cur, len(l), cur):
                l[j] = False

            for j in primes:
                if util.is_prime(util.concatenate_digit(cur, j)) and\
                   util.is_prime(util.concatenate_digit(j, cur)):
                    prime_dict[j].add(cur)

            primes.append(cur)
            prime_dict[cur] = set()

    elim_set = set()
    for i in primes:
        if len(prime_dict[i]) < 4:
            prime_dict.pop(i)
            elim_set.add(i)

    for i in prime_dict.keys():
        prime_dict[i] -= elim_set

    min_ans = float('inf')
    ans = ()
    for p1 in prime_dict.keys():

        for p2 in prime_dict[p1]:

            for p3 in prime_dict[p2]:
                if p3 not in prime_dict[p1]:
                    continue

                for p4 in prime_dict[p3]:
                    if p4 not in prime_dict[p1] or p4 not in prime_dict[p2]:
                        continue

                    for p5 in prime_dict[p4]:
                        if p5 not in prime_dict[p1] or p5 not in prime_dict[p2] or\
                           p5 not in prime_dict[p3]:
                               continue

                        s = p1 + p2 + p3 + p4 + p5
                        if s < min_ans:
                            min_ans = s
                            ans = (p1, p2, p3, p4, p5)

    print(min_ans)
    print(ans)
