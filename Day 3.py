"""
Day 3: Choose your own adventure
"""

import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Begin my code

ready = input('Are you ready?! (Y/N)\n').lower()
if ready == 'yes' or ready == 'y':
    print('\"Arrrrrr, welcome aboard matey! You will be sharing a bunk with one-eyed Jane.\"')
else:
    print('\"Then we shall have to do some kidnapping. Into the barrel ye goes!\"')
    print('You are grabbed and thrown into an empty barrel labelled \"salted pork\".')

print('You accept your fate and try to get some sleep despite the smell.')
print('After some bad rest, you are woken up by a strong lurch that knocks you on the floor.')
print('You scuttle away and find that the ship had struck land. \"Is that how ships work?\" you think to yourself.')
print('From over your shoulder you hear the captain say, \"Welcome to Treasure Island!\" '
      'Everyone on the boat begins jumping overboard.')
time.sleep(5)

jump = input('Do you jump off the right or left side of the boat? (R/L)\n').lower()
if jump == 'l' or jump == 'left':
    print('Good choice! You safely swim ashore with your new pirate friends.')
    time.sleep(5)

    pond = input('Walk up the beach and into the jungle. There you come across a clear pond so clear you can see the'
                 'bottom. Do you wash off the sand on you? (Y/N)\n').lower()
    if pond == 'no' or pond == 'n':
        ('Gross.')

        print('After some more walking, a clearing appears. In the middle is what looks like an abandoned house.')
        print('Your party approaches and discovers three doors: red, yellow, and blue.')
        print('Someone yells, \"Let the new kid choose!\" You freeze and everyone turns to you.')
        print('\"Go on\", says the captain drawing his gun. You take a deep breath and step forward.')

        door = input('Which door do you choose? (R/Y/B)\n').lower()
        if door == 'blue' or door == 'b':
            print('A troupe of monkeys clamor out and devour you. Whoopsie.')
            print('Game Over.')
        elif door == 'red' or door == 'r':
            print('Tongues of fire leap out and consume you. This is not your day.')
            print('Game Over.')
        elif door == 'yellow' or door == 'y':
            print('Tada, you found the gold! You will be rewarded for your forced bravery.')
            print('You win!')
        else:
            print('That was not an option. The captain shoots you for not following directions. Pirates are very '
                  'particular about following directions.')
            print('Game Over.')


    else:
        print('Immediately, trout come out from all the rocks and attack you. "So that\'s why it is called \'Long John'
              'Silvers\'!", you yell before being overwhelmed and drown.')
        print('Game Over.')

else:
    print('You didn\'t look first and jumped right onto land, breaking both femurs. Ouch!')
    print('Game Over.')



