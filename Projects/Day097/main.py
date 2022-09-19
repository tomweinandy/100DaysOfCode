"""
Day 97: Personalized Sponsor Request Email

Documentation: https://docs.python.org/3/library/smtplib.html
"""
import smtplib
import datetime as dt
import random
import pandas as pd
import json
import textract


def salutation(contact_series):
    """
    Converts a contact series into a proper salutation depending on the number of people.
    :param contact_series: Series taken from the subset of all contacts from the same organziation
    :return: A string salutation
    """
    # Convert to list
    contact_list = []
    for contact in contact_series:
        # Fill non-string names with "Colleague"
        if type(contact) != str:
            contact = 'Colleague'

        # Remove leading/trailing whitespace
        contact = contact.strip()

        # Fill in empty string names with "Colleague"
        if len(contact) == 0:
            contact = 'Colleague'
        contact_list.append(contact)

    # If there is only one contact
    if len(contact_list) == 1:
        contact_str = contact_list[0]

    # If two contacts
    elif len(contact_series) == 2:
        contact_str = contact_list[0] + ' and ' + contact_list[1]

    # If more than two contacts
    else:
        # Put first contact at the end
        contact_str = 'and ' + contact_list[0]
        # Add remaining contacts
        for contact in contact_list[1:]:
            contact_str = contact.strip() + ', ' + contact_str

    return contact_str


# Define folder path of project assets
folder_path = '../../../../Dropbox/Big Data Ignite/AutomatedEmail/'

# Read in credentials and save as a dictionary
with open(folder_path + 'Creds.json') as file:
    creds = json.loads(file.read())

EMAIL = creds['EMAIL']
EMAIL_KEY = creds['EMAIL_KEY']

# Read in list of potential sponsors
# df = pd.read_csv(folder_path + 'PotentialSponsors.csv')
df = pd.read_csv('TestSponsors.csv')

# Define list of all organizations in the csv
org_list = df['Organization'].unique()

# Read in message for email
text_byte = textract.process(folder_path + 'Sponsorship Invitation - Cold Email.docx')
text = text_byte.decode("utf-8")


for org in org_list:
    df_subset = df[df['Organization'] == org]
    df_subset = df_subset.reset_index(drop=True)

    print(df_subset['Organization'][0])
    print(salutation(df_subset['Contact Name']))




    #     print()
    #
    # new_text = text.replace('<Contact Name>', contacts)
    # new_text = new_text.replace('<Organization Name>', org)
    # print(new_text)





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
