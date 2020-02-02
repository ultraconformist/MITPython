# -*- coding: utf-8 -*-
"""
Finger Exercise 7.1
Created on Sun Jan 26 21:52:36 2020

@author: Morgan
"""

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    sum = 0
    try:
        for char in s:
            if char.isdigit():
               sum += int(char)
            else:
                pass
        return sum
    except NameError:
        print(s, 'is not defined as a string')
    except TypeError:
        print(s, 'is not a string')