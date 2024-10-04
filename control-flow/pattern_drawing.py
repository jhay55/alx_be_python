# This code generates a pattern in square shape with the length specified by the user
# Applies the concept of nested loops.

user_input = int(input('Enter the size of the pattern: ')) # prompts the user for a number 

i = 0
while i < user_input:  # outer loop for iterating through the rows
    for j in range(user_input): # inner loop for iterating through the columns 
        print('*', end="") 
    i += 1
    print()
