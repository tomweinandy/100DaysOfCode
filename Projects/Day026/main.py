"""
Day 26: NATO Phonetic Alphabet Converter
"""
import pandas as pd

# Read dataframe and create dictionary
df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Continue the program until stopped
proceed = True
while proceed:
    input_word = input('Type a word to convert to the NATO phonetic alphabet: ').upper()

    # Break loop with 'quit'
    if input_word == 'QUIT':
        proceed = False

    try:
        # Create a list of the phonetic code words from a word that the user inputs.
        input_list = [letter for letter in input_word]
        output = [nato_dict[letter] for letter in input_list]
        print(output)
    except KeyError:
        print('Sorry, input may only include letters in the English alphabet.')
