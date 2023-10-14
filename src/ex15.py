"""
Exercise 15
"""

import statistics
def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """

    if num_list.__len__() == 0:
        return None
    else:
        median_num = statistics.median(num_list)
        return median_num
