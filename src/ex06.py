"""
Execise 6
"""


def ordinal_suffix(param):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # Fix : complete this
    if param == 0:
        return "0th"
    if param == 1:
        return "1st"
    if param == 2:
        return "2nd"
    if param == 3:
        return "3rd"
    if param == 4:
        return "4th"
    if param >=10 and param<=100:
        return str(param)+"th"
    if param >=100:
        return str(param)+"st"
