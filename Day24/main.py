"""
Day 24: Mail Merge
"""
import os

#TODO: document and clean up

print(os.getcwd())

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.read()
    names_list = names.split('\n')

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

for name in names_list:
    new_letter = letter.replace('[name]', name)
    new_letter = new_letter.replace('Angela', 'Thomas')

    filename = f'{name}Letter'.strip(' ')
    with open(f'Output/ReadyToSend/{filename}.txt', 'w') as output_file:
        output_file.write(new_letter)