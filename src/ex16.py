"""
Exercise 16
"""

import statistics
def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if num_list.__len__() == 0:
        return None
    else:
        mode_num = statistics.mode(num_list)
        return mode_num
