#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of code 4
12/04/2022
"""
import numpy as np
with open('input_4.txt') as f:
    drawn = f.readlines()[0].split(',')
    drawn = list(map(int, drawn))
cards = np.genfromtxt('input_4.txt', dtype=float, skip_header=1)
cards_raw = np.array_split(cards, len(cards)/5)
cards_cut = np.array_split(cards, len(cards)/5)

def play_bingo(cards_raw, drawn):
    stamped_y = {} 
    stamped_x = {}
    for d in drawn:
        for index, card in enumerate(cards_raw):
            loc = np.argwhere(card == d)
            if loc.size:
                if index not in stamped_y:
                    stamped_y[index] = []
                    stamped_x[index] = []
                stamped_y[index].append(loc[0][0])
                stamped_x[index].append(loc[0][1])
                if stamped_y[index].count(loc[0][0]) > 4 or stamped_x[index].count(loc[0][1]) > 4:
                    print('BINGO')
                    return index, stamped_y[index], stamped_x[index], d

def calculate_score(card, y, x, final_number):
    for i in range(len(stamped_y)):
        card[y[i],x[i]] = 0
    card.flatten()
    unstamped = card.sum()
    return unstamped*final_number
    
# part 1
#card_num, stamped_y, stamped_x, final_number = play_bingo(cards_raw, drawn)
#card = cards_raw[card_num]
#score_win = calculate_score(card, stamped_y, stamped_x, final_number)

# part 2
for p in range(len(cards_cut)-1):    
    card_num, stamped_y, stamped_x, final_number = play_bingo(cards_cut, drawn)
    del cards_cut[card_num]
card_num, stamped_y, stamped_x, final_number = play_bingo(cards_cut, drawn)
card = cards_cut[0]
score_lose = calculate_score(card, stamped_y, stamped_x, final_number)        