#!/usr/bin/env python3
# O(n)

if __name__ == '__main__':

    num = 100

    sum_of_squares = 0
    for i in range(1, num+1):
        sum_of_squares += i * i

    square_of_sum = int((1 + num) * num / 2)**2

    print(square_of_sum - sum_of_squares)


