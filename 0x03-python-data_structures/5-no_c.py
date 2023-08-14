#!/usr/bin/python3

def no_c(my_string):

    characters_to_remove = 'Cc'

    new_string = ''.join(char for char in my_string
                         if char not in characters_to_remove)
    return new_strig
