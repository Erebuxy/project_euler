#!/usr/bin/env python3

if __name__ == '__main__':

    f_name = './p022_names.txt'

    line = open(f_name).readline()
    line = line.split(',')
    line = [i.strip('"') for i in line]

    line.sort()

    ans = 0
    for i in range(len(line)):
        cur = line[i]

        score = 0
        for j in cur:
            score += ord(j) - ord('A') + 1

        ans += score * (i + 1)

    print(ans)
