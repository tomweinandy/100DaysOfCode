"""
Day 24: Mail Merge
"""
import os

# Show current working directory
print(os.getcwd())

# Read in the list of names from file
with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.read()
    names_list = names.split('\n')

# Read in format letter
with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

# Replace placeholder with new name
for name in names_list:
    new_letter = letter.replace('[name]', name)
    new_letter = new_letter.replace('Angela', 'Thomas')

    # Save new custom letter
    filename = f'{name}Letter'.strip(' ')
    with open(f'Output/ReadyToSend/{filename}.txt', 'w') as output_file:
        output_file.write(new_letter)
