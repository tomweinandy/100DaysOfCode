"""
Day 97: Personalized Sponsor Request Email

Documentation: https://docs.python.org/3/library/smtplib.html
"""
import smtplib
import datetime as dt
import random
import pandas as pd
import json

# Read in credentials and save as a dictionary
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day97Creds.json') as file:
    creds = json.loads(file.read())

EMAIL = creds['EMAIL']
EMAIL_KEY = creds['EMAIL_KEY']

# Read in list of potential sponsors
# df = pd.read_csv('../../../../Dropbox/Big Data Ignite/PotentialSponsors.csv')
df = pd.read_csv('TestSponsors.csv')


for idx, row in df.iterrows():
    print(row['Contact Name'])




# Add helper functions
# def write_letter(birthday_name):
#     """
#     Writes a customized letter to a person on their birthday.
#     :param birthday_name: The name of the birthday person
#     :return: A customized, heartfelt letter
#     """
#     # Select a random letter
#     random_number = random.randint(1, 3)
#     with open(f'letter_templates/letter_{random_number}.txt') as file:
#         new_letter = file.read()
#
#     # Personalize letter
#     new_letter = new_letter.replace('[NAME]', birthday_name)
#     new_letter = new_letter.replace('Angela', 'Thomas')
#
#     return new_letter
#
#
# def send_email(birthday_email, birthday_letter):
#     """
#     Sends an email to a person with their birthday letter.
#     Had to reduce security level detailed here:
#     https://www.udemy.com/course/100-days-of-code/learn/lecture/21712834#questions/13766454
#     :param birthday_email: The email address of the birthday person
#     :param birthday_letter: The customized letter addressed to the birthday person.
#     """
#
#     # Set up SMTP connection
#     # Gmail is smtp.gmail.com, Hotmail is smtp.live.com, Yahoo is smtp.mail.yahoo.com
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         # Start Transfer Layer Security encryption
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs=birthday_email,
#                             msg=f'Subject: Happy Birthday!\n\n{birthday_letter}')
#
#
# # Identify current date
# now = dt.datetime.now()
#
# # Read in csv of birthdays
# birthdays = pd.read_csv('birthdays.csv')
# for idx, person in birthdays.iterrows():
#
#     # Check if birthday is today
#     if person.day == now.day and person.month == now.month:
#         # Write a letter
#         letter = write_letter(person['name'])
#         print(letter)
#
#         # Email the birthday person
#         send_email(person.email, letter)
#
#     else:
#         print(f'Today is not {person["name"]}\'s birthday.')
