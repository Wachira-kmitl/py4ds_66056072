"""
Exercise 18 : Buy 8 get 1 free
"""

def get_cost_of_coffee(glass, price):
    free = glass // 9
    paid = glass - free
    return paid * price


def get_cost_of_coffee_2(x, price):
    free = x // 9
    paid = x - free
    return paid * price
