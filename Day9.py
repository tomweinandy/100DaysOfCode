"""
Day 9: First Price, Sealed Bid Auction
"""

logo = logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print('\nWelcome to a First Price, Sealed Bid Auction!', logo, 'Let\'s begin.\n')

proceed = 'y'
auction = {}

# Loop through the prompt for as many bidders there are
while proceed == 'y':
    name = input('What is your name?: ')

    # Try statement ensure a correct input is added into the bid
    try:
        bid = float(input('What is your bid?: $'))
        bid = round(bid, 2)
        auction[name] = bid
        proceed = input('Is there another bidder? (y/n): ')

        # Clears screen so the next bidder cannot see the previous bids
        print('\n'*150)
    except:
        print('Please make sure your bid is a number, such as "9999.99". Let\'s try that again.')

max_bid = 0
max_bidder = ''
for key, value in auction.items():
    if value > max_bid:
        max_bid = value
        max_bidder = key

# There must be a positive bid for an item to be sold
if max_bid == 0:
    print('The item has not been sold.')
else:
    print(f'The winning bidder is {max_bidder} at ${max_bid}')
