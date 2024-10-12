# This program converts the temparature from Farhenheit to Celcius and vice versa

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
degree_symbol = "\u00B0"

def user_prompt_func():
    """ This function interacts with the user and receives input that will
    be later used to calculate the new temperature value"""

    try: # this try and except block is for catching wrong input type error
        temperature_value = int(input('Enter the temperature to convert: '))
    except ValueError:
        print('Invalid temperature. Please enter a numeric value.')
        quit()

    temperature_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()
    if temperature_type != 'F' and temperature_type != 'C':
            print('Invalid Temperature: try C or F')
    else:
         pass
            #print(f'Converting {temperature_value} {degree_symbol}{temperature_type}' )
            
    
    return temperature_value, temperature_type
    

def convert_to_celsius(fahrenheit):
    """"Converts Fahrenheit to Celcius using the value from user input in user prompt function"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    """Converts Celcius to Fahrenheit using the value from user input in user prompt function"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """ This function describes the main logic of the program. From handling user input to printing out the results
    and assigning the correct variables to the right functions"""
    
    temperature_value, temperature_type = user_prompt_func()


    # if statement conditionals to handle which of the functions get executed based on the 
    # temperature type selected  
    if temperature_type == 'F':
          result = convert_to_celsius(temperature_value)
          print(f'{temperature_value}{degree_symbol}{temperature_type} is {result:.13f}{degree_symbol}C')
    elif temperature_type == 'C':
         result = convert_to_fahrenheit(temperature_value)
         print(f'{temperature_value}{degree_symbol}{temperature_type} is {result:.13f}{degree_symbol}F')
    else:
         print('Error: Selected Temperature does not match options. Try C for Celcius or F for Fahrenheit.')

if __name__ == '__main__':
     main()
