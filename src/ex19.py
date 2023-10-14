"""
Exercise 19 : Password Generator
"""

import random


LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(x):
    # Fix : complete this
    if x < 12:
         x=12
    pw = []
    pw.append(LOWER_LETTERS[random.randint(0,25)])
    pw.append(UPPER_LETTERS[random.randint(0,25)])
    pw.append(NUMBERS[random.randint(0,10)])
    pw.append(SPECIAL[random.randint(0,13)])
    print(pw)
    while len(pw) < x:
        pw.append(ALL_CHARS[random.randint(0,74)])
        random.shuffle(pw)
    return ''.join(pw)
#%%
