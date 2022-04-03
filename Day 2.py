"""
Day 2: Tip Calculator
"""
import re

print('Welcome to the tip calculator.')

bill = input('What was the total bill? ')

# Remove all non-numeric characters (except period)
clean_bill = float(re.sub('[^0-9.]','', bill))

tip = input('What percentage tip would you like to give? ')

# Remove all non-numeric characters (except period)
clean_tip = float(re.sub('[^0-9.]','', tip))

people = int(input('How many people will split the bill? '))

total_payment = clean_bill * ((100 + clean_tip) / 100)
payment_pp = round(total_payment/people, 2)

print(f'Each person should pay: ${payment_pp}')



