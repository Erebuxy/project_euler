#!/usr/bin/env python3

if __name__ == '__main__':

    is_prime = [True for _ in range(int(5e5))]
    is_prime[0] = False
    for i in range(1, len(is_prime)):

        if is_prime[i]:

            cur = 2 * i + 1

            if cur > 5e4:
                str_cur = str(cur)
                replace_list = []

                for j in range(5):
                    if str_cur[:-1].count(str(j)) == 3:
                        replace_list.append(j)

                for j in replace_list:
                    count = 0
                    for k in range(10):
                        replace_str = str_cur.replace(str(j), str(k))
                        if replace_str[0] == '0':
                            continue
                        replace_indx = int((int(replace_str) - 1) / 2)
                        if is_prime[replace_indx]:
                            count += 1

                    if count >= 8:
                        print(cur)
                        exit()

            for j in range(i + cur, len(is_prime), cur):
                is_prime[j] = False


