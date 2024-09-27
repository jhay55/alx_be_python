#This file helps users calculate their monthly savings

#defining variables from user inputs
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your monthly expenses: '))

#new variables
monthly_savings = monthly_income - monthly_expenses
rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #calculates the projected savings at 5% interest rate

r_projected_save = int(projected_savings)

print('Your monthly savings are $' +str(monthly_savings)+ '.')
print('Projected savings after one year, with interest, is: $'+str(r_projected_save)+'.')
