# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 01:43:48 2020
Problem Set 1: Part A
@author: Morgan
"""
# Calculates how long it will take to make a house down payment
# Uses inputs given by user

# Set assumption constants
current_savings = 0.0
portion_down_payment = 0.25
r = 0.04 # Annual rate of return

months_saved = 0

# Ask user's salary, portion, and cost of home and cast to float
annual_salary = float(input('Please enter your annual salary: '))
portion_saved = float(input('Please enter portion to be saved of your salary\
                            each month as a decimal value: '))
total_cost = float(input('Please enter the total cost of your home\'s\
                         down payment: '))

down_payment_cost = total_cost*portion_down_payment

monthly_savings = (annual_salary/12)*portion_saved

while current_savings<=down_payment_cost:
        current_savings=current_savings+monthly_savings
        # Add monthly return at end of month
        current_savings=current_savings+(current_savings*r/12)
        months_saved = months_saved + 1 # Increment month counter
months_saved=str(months_saved) # cast months to string        
print('It will take ' + months_saved + ' months to save up.')