"""
Day 81: String to Morse Code Converter
"""
import re

# Define Morse Code dictionary
code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        ' ': '  '}

# Add input text
input_text = input('Type what you would like to convert to Morse Code: ').upper()
# input_text = 'HELLO WORLD!'

# Remove non-alphanumeric characters
input_text = re.sub(r'[^A-Z0-9\s]', '', input_text)

# Convert text to Morse Code
output = ''
for i in input_text:
    output += code[i] + ' '

# Remove the last space
output = output[:-1]

print(f'{input_text} in Morse Code: {output}')
