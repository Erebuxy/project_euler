#!/usr/bin/env python3

def is_palindromic(a):

    if int(a / 1e5) != a % 10:
        return False 
    if int(a / 1e4) % 10 != int(a / 10) % 10:
        return False 
    if int(a / 1e3) % 10 != int(a/ 100) % 10:
        return False

    return True

if __name__ == '__main__':

    max_pad = 0

    for i in range(999, 101, -1):
        for j in range(999, 101, -1):

            product = i * j

            if product < max_pad:
                break

            if is_palindromic(product):
                max_pad = product

    print(max_pad)
