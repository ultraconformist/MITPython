# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 02:02:18 2020
Problem Set 1: Part B
@author: Morgan
"""
# Calculates how long it will take to make a house down payment
# Uses inputs given by user
# This version also accounts for semi-annual raise

# Set assumption constants
current_savings = 0.0
portion_down_payment = 0.25
r = 0.04 # Annual rate of return

months_saved = 0 

# Ask user's salary, portion, and cost of home and cast to float
annual_salary = float(input('Please enter your annual salary: '))
portion_saved = float(input('Please enter portion to be saved of your salary\
                            each month as a decimal value: '))
total_cost = float(input('Please enter the total cost of your home\'s \
                         down payment: '))
semi_annual_raise = float(input('What decimal percentage raise do you get? '))

down_payment_cost = total_cost*portion_down_payment

while current_savings<=down_payment_cost:
        monthly_savings = (annual_salary/12)*portion_saved        
        current_savings=current_savings+monthly_savings
        # Add monthly return at end of month
        current_savings=current_savings+(current_savings*r/12)
        months_saved = months_saved + 1
        # Every six months, increase salary by raise
        if (months_saved % 6) == 0:
            annual_salary=annual_salary+(annual_salary*semi_annual_raise)
            
months_saved=str(months_saved) # cast months to string        
print('It will take ' + months_saved + ' months to save up.')