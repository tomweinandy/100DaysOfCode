"""
Day 5: Password Generator
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Begin my code

password = ''

# Add random letters to the password
for l in range(nr_letters):
    random.shuffle(letters)
    password += letters[0]

# Add random numbers to the password
for n in range(nr_numbers):
    random.shuffle(numbers)
    password += numbers[0]

# Add random symbols to the password
for s in range(nr_symbols):
    random.shuffle(symbols)
    password += symbols[0]

# Convert string to list
password_list = []
for p in password:
    password_list.append(p)

# Shuffle that list
random.shuffle(password_list)

# Stitch it back together (as good as new!)
new_password = ''
for p in password_list:
    new_password += p

print('Your new password is:', new_password)

