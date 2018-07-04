#!/usr/bin/env python3

if __name__ == "__main__":

    limit = 200

    l = [0 for i in range(limit+1)]
    l[0] = 1
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    for c in coins:
        for i in range(len(l)):
            if i + c > limit:
                break

            l[i+c] += l[i]

    print(l[-1])


