"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    x=0
    try:
        for i in num_list:
            x+=i
        return x
    except: 0



def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    x=1
    try:
        for i in num_list:
            x*=i
        return x
    except: 1
