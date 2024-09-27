#this is a simple interest calculator Python Script Using Basic operations

principal = 1000 #This is the principal in Dollars
rate = 0.05 #This is the rate per annum at 5%
time = 3 #time of investment duration in years

interest = principal*rate*time #this calculates the simple interest of the investment.

r_interest = round(interest,1) #rounds the interest to one decimal place

# Onto the print commands
print('For an amount of $'+str(principal)+ ' dollars at a rate of 5% per annum for 3 years' )
print('The simple interest is: '+ str(r_interest) )
