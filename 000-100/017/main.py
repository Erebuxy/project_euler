#!/usr/bin/env python3

if __name__ == '__main__':

    n_1_9 = len('onetwothreefourfivesixseveneightnine')
    n_10_19 = len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')
    n_20_90 = len('twentythirtyfortyfiftysixtyseventyeightyninety')
    n_100 = len('hundred')

    n_1_99 = n_1_9 + n_10_19 + (10 * n_20_90 + 8 * n_1_9)
    n_1_999 = n_1_99 + (100 * (n_1_9 + 9 * n_100) + 9 * 99 * len('and') + 9 * n_1_99)

    print(n_1_999 + len('onethousand'))
