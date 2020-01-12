# -*- coding: utf-8 -*-
"""
(Modified) Finger Exercise for 3.1
Created on Wed Jan  8 23:50:55 2020

@author: Morgan
"""
# Finds two integers, root and power, such that 1 < pwr < 6 and root**pwr 
# is equal to an integer entered by the user

# This finds specifically the largest such pair

userInt = int(input("Enter an integer: "))
for pwr in range(5,1,-1):
    root = min(0,userInt)
    while (root**pwr != userInt):
        root = root+1
        if root > abs(userInt):
            break
    if root**pwr == userInt:
        break
if root**pwr == userInt:
    print(str(root) + " to the power of " + str(pwr) + " is equal to " \
          + str(userInt))
else:
    print("No pair of exponents between 2 and 6 and any integer \
          will result in "+ str(userInt))