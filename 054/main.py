#!/usr/bin/env python3

card2int_num = {'2' : 0, '3' : 1, '4' : 2, '5' : 3, '6': 4, '7' : 5,
                '8' : 6, '9' : 7, 'T' : 8, 'J' : 9, 'Q': 10, 'K': 11,
                'A' : 12}
card2int_suit = {'C' : 0, 'D' : 1, 'H' : 2, 'S' : 3}

def calculate_score(hand):
    num = [0 for _ in range(13)]
    suit = [0 for _ in range(4)]
    
    for i in range(5):
        cur = hand[i]
        num[card2int_num[cur[0]]] += 1
        suit[card2int_suit[cur[1]]] += 1

    four = -1
    three = -1
    pair = -1
    double_pair = -1
    flush = -1
    straight = -1
    single = []

    straight_count = 0
    for i in range(13):
        if num[i] == 1:
            straight_count += 1
            single.append(i)
            if straight_count == 5:
                straight = i
                break
        else:
            straight_count = 0

            if num[i] == 4:
                four = i
            elif num[i] == 3:
                three = i
            elif num[i] == 2:
                if pair == -1:
                    pair = i
                else:
                    double_pair = i

    single.sort()
    single_score = 0
    for i in range(len(single)):
        single_score += single[i] * 13**i

    for i in range(4):
        if suit[i] == 5:
            flush = i
            break
    
    if straight >= 0 and flush >= 0:
        return 8 * 13**5 + straight * 13**4
    elif four >= 0:
        return 7 * 13**5 + four * 13**4 + single_score
    elif three >= 0 and pair >= 0:
        return 6 * 13**5 + three * 13**4 + pair * 13**3
    elif flush >= 0:
        return 5 * 13**5 + single_score
    elif straight >= 0:
        return 4 * 13**5 + straight * 13**4
    elif three >= 0:
        return 3 * 13**5 + three * 13**4 + single_score 
    elif double_pair >= 0:
        return 2 * 13**5 + max(pair, double_pair) * 13**4 +\
               min(pair, double_pair) * 13**3 + single_score 
    elif pair >= 0:
        return 1 * 13**5 + pair * 13**4 + single_score 
    else:
        return single_score  

if __name__ == '__main__':

    f = open('./p054_poker.txt')

    p1_win = 0
    for line in f:
        cards = line.split()
        
        p1_s = calculate_score(cards[:5])
        p2_s = calculate_score(cards[5:])

        if p1_s > p2_s:
            p1_win += 1

    print(p1_win)
