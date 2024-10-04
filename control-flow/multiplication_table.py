# this is a multiplication table generator 
# this code will print the multiplication table for any number the user inputs for factors 1 - 10


number = int(input('Enter a number to see its multiplication table: ')) # prompts user for a number

# a for loop that iterates through a range and prints the product of the users number and factors from 1 - 10
for i in range(1,11):
    print(f'{number} * {i} = {i*number}',end='')
    print()
