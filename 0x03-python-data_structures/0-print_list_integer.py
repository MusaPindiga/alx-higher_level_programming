#!/usr/bin/python3

def print_list_integer(my_list):
    """Prints each integer element from the given list."""
    counter = len(my_list)
    i = 0
    
    while i < counter:
        print('%d'% my_list[i])
        i += 1

