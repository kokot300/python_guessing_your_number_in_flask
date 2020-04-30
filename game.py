#!/usr/bin/python3

def game(where_we_are_flag=0, min=0, max=1000):
    guess = int((max - min) / 2) + int(min)
    if where_we_are_flag == 0:
        guess = int((max - min) / 2) + int(min)
        return guess, min, max
    if where_we_are_flag == 1:
        return 'wygrałem!'
    elif where_we_are_flag == 2:
        max = guess
        guess = int((max - min) / 2) + int(min)
        return guess, min, max
    elif where_we_are_flag == 3:
        min = guess
        guess = int((max - min) / 2) + int(min)
        return guess, min, max
    else:
        raise BlockingIOError
