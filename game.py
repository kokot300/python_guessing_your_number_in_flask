#!/usr/bin/python3

def game(where_we_are_flag=0, min=0, max=1000):
    '''

    :param where_we_are_flag:
    :param min: minimum number from range
    :param max: maximum number of the range
    :return: int which is number that the program is going to guess
    '''
    guess = int((max - min) / 2) + int(min)
    if where_we_are_flag == 0:
        guess = int((max - min) / 2) + int(min)
        return guess, min, max
    elif where_we_are_flag == 1:
        return 'wygrałem!'
    elif where_we_are_flag == 2:
        max = guess
        guess = int((max - min) / 2) + int(min)
        return guess, min, max
    elif where_we_are_flag == 3:
        min = guess
        guess = int((max - min) / 2) + int(min)
        return guess, min, max
    else:  # just messing up. sorry for that ;)
        raise BlockingIOError
