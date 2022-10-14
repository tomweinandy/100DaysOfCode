"""
Day 97: Personalized Conference Email Blast

Documentation: https://docs.python.org/3/library/smtplib.html
Note: Some emails were not delivered citing security reasons. These had to be manually re-sent.
"""
# todo remove todos after prod run
# todo add/update test static
import pandas as pd
from os.path import basename
import json
import time
import datetime
import smtplib
import textract
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define folder path of project static
FOLDER_PATH = '../../../../Dropbox/Big Data Ignite/AutomatedEmail/'


# Define helper functions
def salutation(contact_series):
    """
    Converts a contact series into a proper salutation depending on the number of people.
    :param contact_series: Series taken from the subset of all contacts from the same organization
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
    elif len(contact_list) == 2:
        contact_str = contact_list[0] + ' and ' + contact_list[1]

    # If more than two contacts
    else:
        # Put first contact at the end
        contact_str = 'and ' + contact_list[0]
        # Add remaining contacts
        for contact in contact_list[1:]:
            contact_str = contact.strip() + ', ' + contact_str

    return contact_str


def get_emails(email_series):
    """
    Converts an email series into a string list of emails.
    :param email_series: Series taken from the subset of all contacts from the same organization
    :return: A string list of email addresses
    """
    # Convert to list
    email_list = []
    for email in email_series:
        # Cast non-string names as an empty string
        if type(email) != str:
            email = ''

        # Remove leading/trailing whitespace
        email = email.strip()

        email_list.append(email)

    email_string_list = ''
    # If there is only one contact
    if len(email_list) == 1:
        email_string_list = email_list[0]

    # If multiple contacts, combine into one string
    elif len(email_list) > 1:
        for email in email_list:
            email_string_list += email + ', '
            # Remove comma and whitespace from last email in list
            email_string_list = email_string_list[:-2]

    return email_list


def send_email(emails, subject_line, content):
    """
    Had to reduce security level detailed here:
    https://www.udemy.com/course/100-days-of-code/learn/lecture/21712834#questions/13766454
    """
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject_line
    msg['From'] = EMAIL
    msg['To'] = ', '.join(emails)
    # msg['Cc'] = ', '.join(cc_emails)

    # Include an attachment
    f = FOLDER_PATH + 'Sponsor Invitation 2022.docx'
    with open(f, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(f)
        )
    # After the file is closed.
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    msg.attach(part)

    # Record the MIME types of both parts - text/plain and text/html.
    body = MIMEText(content, 'plain')

    # Attach parts into message container.
    msg.attach(body)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.login(EMAIL, EMAIL_KEY)
    s.sendmail(EMAIL, emails, msg.as_string())
    s.quit()


# Read in credentials and save as a dictionary
with open(FOLDER_PATH + 'Creds.json') as file:
    creds = json.loads(file.read())
EMAIL = creds['EMAIL2']
EMAIL_KEY = creds['EMAIL_KEY2'] #todo change for production run

# Read in list of potential sponsors
# df = pd.read_csv(FOLDER_PATH + 'PotentialSponsors.csv') #todo change for production run
df = pd.read_csv('TestSponsors.csv')

# Define list of all organizations in the csv
org_list = df['Organization'].unique()

# Read in message for email
text_byte = textract.process(FOLDER_PATH + 'Sponsorship Invitation - Cold Email.docx')
text = text_byte.decode('utf-8')

# Only send one email per organization
counter = 0
for org in org_list:
    # Filter all contacts in the same organization
    df_subset = df[df['Organization'] == org]
    df_subset = df_subset.reset_index(drop=True)

    # Modify text to be used in message
    new_text = text.replace('<Contact Name>', salutation(df_subset['Contact Name']))
    new_text = new_text.replace('<Organization Name>', org)

    # Send email
    org_emails = get_emails(df_subset['Contact Email'])
    subject = 'Invitation to Join and Support Big Data Ignite 2022'
    send_email(org_emails, subject, new_text)

    # Print status
    counter += 1
    now = datetime.datetime.now()
    status = round(100*(counter/len(org_list)), 1)
    print(f'Sent email to {org_emails} at {now} ({status}% complete)')

    # Add a delay to prevent account flagging (unclear if this is necessary, but did not want to risk in production run)
    time.sleep(10) #todo change for production run
