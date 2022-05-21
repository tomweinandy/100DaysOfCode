"""
Day 8: Caesar Cipher
"""

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print('Welcome to...\n', logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Allow user to rerun the program (auto-runs on first time)
rerun = 'y'
while rerun == 'y':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        """
        :param text: input text to encrypt
        :param shift: the number of spaces in the alphabet each letter moves (any integer)
        :return: an new_text word
        """

        # This allows for shifts > 26
        shift = shift % 26

        # Reverse the direction if decrypting
        if direction == 'encode':
            print('I came. I saw. I encoded.\n')
        elif direction == 'decode':
            shift = -shift
            print('I came. I saw. I decoded.\n')
        else:
            print('Encode/decode not specified. Et tu, Brute?\n')

        new_text = ''
        for character in text:
            # Allows for non-letter inputs
            try:
                idx = alphabet.index(character)

                # If shift goes beyond the length of the alphabet, then circle back to the beginning
                idx_shift = idx + shift
                if idx_shift > 25:
                        idx_shift = idx_shift - 26   #circle back to beginning

                # Excrypts the letter
                new_character = alphabet[idx_shift]

            # Return character as self if it can't be encrypted
            except:
                new_character = character

            # Add new letter to string
            new_text += new_character
        print(new_text)

    # Test it out
    caesar(text, shift, direction)
    rerun = input('\nDo you wish to rerun the program? (y/n)\n').lower()

else:
    print('The die is cast. Goodbye.')
