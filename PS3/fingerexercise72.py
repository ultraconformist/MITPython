# -*- coding: utf-8 -*-
"""
Finger Exercise 7.2
Created on Sun Jan 26 22:17:59 2020

@author: Morgan
"""

def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    try:
        assert isinstance(L, list)
        for val in L:
            if (val % 2) == 0:
                return val
            else:
                continue
        raise ValueError()
    except AssertionError:
        print(L, 'is not a list')
    except ValueError:
        print(L,'does not contain an even number')