#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                element1 = my_list_1[i]
                element2 = my_list_2[i]
                if not isinstance(element1, (int, float)) or \
                   not isinstance(element2, (int, float)):
                    raise TypeError("wrong type")
                if element2 == 0:
                    raise ZeroDivisionError("division by 0")
                result = element1 / element2
            except IndexError:
                print("out of range")
                result = 0
            except (ZeroDivisionError, TypeError) as e:
                print(e)
                result = 0
            finally:
                result_list.append(result)
    finally:
        return result_list
