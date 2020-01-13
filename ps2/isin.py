# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:28:28 2020
Finger Exercise 4.1.1
@author: Morgan
"""
# Function that accepts two strings as args and returns True
# if either string occurs anywhere in the other, and false otherwise
def isIn(str1, str2):
    if str1 in str2:
        return True
    else:
        return False
print(isIn('Deed','WDeed'))
print(isIn('Deed','WDeed'))