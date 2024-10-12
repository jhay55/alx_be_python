# This file ....


def perform_operation(num1, num2, operation):
    """This is a function that performs basic arithmetic 
    operations on two numbers"""
    match operation:
        case 'add':
           return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return f'Division by Zero not allowed'
            elif:
                return num1/num2
        case _:
            return f'Invalid Input, Try Strings like add ...'
