"""
Day 32: Automated Birthday Wisher

# https://docs.python.org/3/library/smtplib.html
"""
import smtplib

# Add email (split up so the bots can't find me)
dummy_username = 'ignorethistest2022'
dummy_domain = '@gmail.com'
dummy_email = dummy_username + dummy_domain

my_username = 'tomweinandy'
my_domain = '@gmail.com'
my_email = my_username + my_domain

# Add password (dummy account)
file_path = 'not_very_secure.txt'
with open(file_path) as file:
    dummy_password = file.read()

# Had to reduce security level detailed here:
# https://www.udemy.com/course/100-days-of-code/learn/lecture/21712834#questions/13766454

# Set up SMTP connection
# Gmail is smtp.gmail.com, Hotmail is smtp.live.com, Yahoo is smtp.mail.yahoo.com
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    # Start Transfer Layer Security encryption
    connection.starttls()
    connection.login(user=dummy_email, password=dummy_password)
    connection.sendmail(from_addr=dummy_email,
                        to_addrs=my_email,
                        msg='Subject: Subject line\n\nThis is the body of the email.'
                        )


