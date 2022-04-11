"""
Day 10: Nine-function calculator
"""

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print('\nWelcome to this calculator!', logo)

def calculator(n, operation, percent_sign):
    """
    A simple nine-function calculator.
    :param n: the first number (type = float)
    :param operation: the operation to perform (+, -, *, /, ^, sqrt, %, end, clear)
    :return: resulting calculation (or end/clear operation), and percent sign
    """

    # Percent operation
    if operation == '%':
        # Note: This percent sign will remain until the entry is cleared
        percent_sign = '%'
        result = round(n * 100, 2)
        print(f'{n} as a percent is {result}{percent_sign}')

    # Clear operation
    elif operation == 'clear':
        result = 'clear'
        print('Entry cleared.')

    # End operation
    elif operation == 'end':
        result = 'end'

    # All other operations
    elif operation in '+-*/^sqrt':
        m = float(input('What\'s the next number?: '))

        # Addition operation
        if operation == '+':
            result = n + m
            print(f'{n}{percent_sign} + {m} = {result}{percent_sign}')

        # Subtraction operation
        elif operation == '-':
            result = n - m
            print(f'{n}{percent_sign} - {m} = {result}{percent_sign}')

        # Multiplication operation
        elif operation == '*':
            result = n * m
            print(f'{n}{percent_sign} * {m} = {result}{percent_sign}')

        # Division operation
        elif operation == '/':
            result = n / m
            print(f'{n}{percent_sign} / {m} = {result}{percent_sign}')

        # Exponential operation
        elif operation == '^':
            result = n ** m
            print(f'{n}{percent_sign} ^ {m} = {result}{percent_sign}')

        # Square root operation
        elif operation == 'sqrt':
            result = n ** 1/m
            print(f'{m} sqrt({n}{percent_sign}) = {result}{percent_sign}')

    # Clear results if the operator is invalid
    else:
        result = 'clear'
        print('Invalid entry. Let\'s start afresh.')

    return result, percent_sign


# Set initial conditions
clear = True
end = False

while clear:
    # Executes end operation by breaking this loop
    if end:
        print('I\'ll CPU later!')
        break

    # Initially sets percent sign as blank
    percent_sign = ''

    # Requests first input and executes
    n = float(input('What\'s the first number?: '))
    operation = input('Pick an operation (+, -, *, /, ^, sqrt, %, clear, end): ').strip() #remove whitespace
    result, percent_sign = calculator(n, operation, percent_sign)

    # If clear is selected, skip next loop and restart this loop
    if result == 'clear':
        clear = True
    else:
        clear = False

    # If end is selected, skip next loop and restart this loop (where the end condition will break this loop)
    if result == 'end':
        end = True
        clear = True

    # Continues operation until user chooses to clear or end
    while not clear:
        operation = input('Pick an operation (+, -, *, /, ^, sqrt,  %, clear, end): ')
        result, percent_sign = calculator(result, operation, percent_sign)

        if result == 'clear':
            clear = True

        if result == 'end':
            end = True
            clear = True
