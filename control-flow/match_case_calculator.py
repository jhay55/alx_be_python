# This script is in three levels
# First receives input from users, then asks for arithmetic operation and returns the results
# match case block is implemented for the operation to avoid writing spaghetti if statements


# variables for prompting user for numbers and operator
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /): ')

# match case block for different operation scenarios
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num2 * num1
    case '/':
        if num2 == 0:  #this if statement is to prevent a zerodivision error in case denominator is zero
            print('Cannot divide by zero.')
            exit()
        result = num1/num2
        
print(f'The result is {int(result)}')
