#!/usr/bin/python3

def uniq_add(my_list=[]):

    sum = 0
    unique_list = []

    for num in my_list:
        if num not in unique_list:
            unique_list.append(num)

    for unique in unique_list:
        sum += unique

    return sum
