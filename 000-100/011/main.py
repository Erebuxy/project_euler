#!/usr/bin/env python3

if __name__ == '__main__':

    f_name = './grid.txt'

    mtx = []
    for line in open(f_name):
        row = line.split()
        row = [int(i) for i in row]

        mtx.append(row)

    max_ans = 0

    # horizontal
    for row in mtx:
        p1, p2, p3 = 0, 0, 0

        for i in row:
            if i * p3 > max_ans:
                max_ans = i * p3

            p3 = p2 * i
            p2 = p1 * i
            p1 = i

    # vertical
    for x in range(len(mtx[0])):
        p1, p2, p3 = 0, 0, 0

        for y in range(len(mtx)):
            i = mtx[y][x]

            if i * p3 > max_ans:
                max_ans = i * p3

            p3 = p2 * i
            p2 = p1 * i
            p1 = i

    # diagonal
    for x in range(len(mtx[0]) - 3):
        for y in range(len(mtx) - 3):

            temp = mtx[y][x] * mtx[y+1][x+1] * mtx[y+2][x+2] * mtx[y+3][x+3]
            if temp > max_ans:
                max_ans = temp

            temp = mtx[y][x+3] * mtx[y+1][x+2] * mtx[y+2][x+1] * mtx[y+3][x]
            if temp > max_ans:
                max_ans = temp

    print(max_ans)
            
