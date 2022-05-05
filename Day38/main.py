"""
Day 38:
"""
import ast

APP_ID = '76070878'

# Read in credential string and save as a dictionary
with open('../../Dropbox/100DaysOfCodePRIVATE/Day38Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
API_KEY = creds['API_KEY']