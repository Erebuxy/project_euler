#!/usr/bin/env python3

import math

if __name__ == '__main__':
    
    num = 1000000
    lex = [str(i) for i in range(10)]

    num_away = num
    ans = ''
    for cur_pos in range(9, -1, -1):
        cur_fc = math.factorial(cur_pos)
        cur_dig = int(num_away / cur_fc)
        if num_away % cur_fc == 0:
            cur_dig -= 1

        num_away -= cur_dig * cur_fc 
        ans += lex.pop(cur_dig)

    print(ans)
