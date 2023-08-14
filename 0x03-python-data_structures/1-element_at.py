#!/usr/bin/python3

def element_at(my_list, idx):

    size = len(my_list)
    i = 0

    if idx < 0 or idx > size:
        return

    while i < size:

        if i == idx:
            return my_list[i]

        i += 1

