g.# -*- coding: utf-8 -*-
"""
Finger Exercise 3.3
Approximate cube root of any integer with bisection search
Created on Thu Jan  9 01:03:30 2020

@author: Morgan
"""
x = int(input("Enter any integer: "))
epsilon = 0.01
numGuesses = 0
low = min(0.0,x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to the cube root of', x)