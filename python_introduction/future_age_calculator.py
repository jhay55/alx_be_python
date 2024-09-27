#this file calculates your future age

#Defining the correct age value of user and current year
correct_age = 30
current_year = 2023

user_age = int(input('How old are you?  ' )) #prompting user for input

print('You have entered ' +str(user_age)+ ' as your current age')
print('but I will assume ' +str(correct_age) + ' as your current age...')
futr_age = 27 + correct_age

print ('In 2050. you will be ' +str(futr_age)+ ' years old.')
