# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 01:37:56 2020
Problem Set 1: Part C
@author: Morgan
"""

# Calculates the best rate of savings in order to achieve 
# a down payment on a $1 million house within 36 months.
# Needs only be within $100.
# Uses bisection search.

# Savings constants
portion_down_payment = 0.25
current_savings = 0.0
semi_annual_raise = 0.07
r = 0.04 # Annual rate of return
total_cost = 1000000

# Calculate down payment
down_payment = total_cost*portion_down_payment

annual_salary = float(input('Please enter your annual salary: '))

# Bisection search constants
numGuesses = 0
low = 0
high = 10000
epsilon = 100 # Upper and lower bound of approximate savings
outOfRange = False # Flag to check if full range has been searched

salary = annual_salary # Store user inputted value

while abs(current_savings - down_payment)>epsilon:
    # Make guess
    ans = int((high + low)/2)
    numGuesses += 1
    
    # Reset values for new guess
    monthly_savings = 0.0
    current_savings = 0.0
    salary = annual_salary
    portion_saved = (ans/10000)
    
    # Save over 36 months with current guess
    for months_saved in range(1,37):
            monthly_savings = (salary/12)*portion_saved        
            current_savings=current_savings+monthly_savings
            # Add monthly return at end of month
            current_savings=current_savings+(current_savings*r/12)
            # Every six months, increase salary by raise
            if (months_saved % 6) == 0:
                salary=salary+(salary*semi_annual_raise)
    
    # Narrow range of search
    if current_savings < down_payment:
        low = ans
    else:
        high = ans
    
    # Check if full range has been searched
    if ans >= 9999:
        outOfRange = True
        break

if outOfRange == False:
    print('Best savings rate: ', portion_saved)
    print('Steps in bisection search: ', numGuesses)
else: 
    print('It is not possible to pay the down payment in three years.')