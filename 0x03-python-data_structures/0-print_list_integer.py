#!/usr/bin/python3

def print_list_integer(my_list):
    """Prints each integer element from the given list.

    This function takes a list of integers as input and prints each
    element of the list on a separate line.

    Arguments:
        my_list (list): A list of integer elements.

    Returns:
        Nothing
    """
    counter = len(my_list)
    i = 0
    
    while i < counter:
        print("{}".format(my_list[i]))
        i += 1

