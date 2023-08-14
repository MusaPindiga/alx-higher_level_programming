#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    size = len(my_list)
    i = 0

    if idx < 0 or idx >= size:
        return my_list

    while i < size:
        if i == idx:
            my_list[i] = element
            return my_list
        i += 1
