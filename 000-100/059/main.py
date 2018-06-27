#!/usr/bin/env python3

if __name__ == '__main__':

    f_name = './p059_cipher.txt'
    cipher = open(f_name).readline()

    cipher = cipher.split(',')
    cipher = [int(i) for i in cipher]

    code = []
    # count statistic
    for i in range(3):
        d = dict()

        for j in range(0, len(cipher), 3):
            if i + j < len(cipher):
                cur = cipher[j+i]

                if cur not in d:
                    d[cur] = 0
                d[cur] += 1

        sort_list = list(d.items())
        sort_list.sort(key=lambda pair: pair[1], reverse=True)
        code.append(sort_list[0][0] ^ ord(' '))

    string = ''
    s = 0
    for i in range(len(cipher)):
        cur = cipher[i] ^ code[i % 3]
        string += chr(cur)
        s += cur

    print(s)
    print(string)
