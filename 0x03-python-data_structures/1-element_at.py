#!/usr/bin/python3

#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Get the element at the specified index in the list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index, or None if the index is out of bounds.
    """
    size = len(my_list)
    i = 0

    if idx < 0 or idx >= size:
        return None

    while i < size:
        if i == idx:
            return my_list[i]
        i += 1


