# Optional: Build out flight club detailed in Day 40

# Ask user to input information
first_name = input('What is your first name?: ')
last_name = input('\nWhat is your last name?: ')
email1 = input('\nWhat is your email?: ')
email2 = input('\nPlease confirm your email: ')

# Check that emails match
while email1 != email2:
    print('The emails did not match.')
    email1 = input('\nWhat is your email?: ')
    email2 = input('\nPlease confirm your email: ')

print('\nYour account has been created. Welcome to the club!')
