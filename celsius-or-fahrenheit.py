#Prompt the user for a number in degrees Celsius, 
#and convert the value to degrees in Fahrenheit and 
#display it to the user.

#prompt user
try:
    degrees_celsius = int(input('What is the degrees celcius? '))
except ValueError:
    print('Enter Valid Temp! ')
#convert celsius to fahrenheit
degrees_fahrenheit = (degrees_celsius * 9/5) + 32 
#return fahrenheit to user
print(f'{degrees_fahrenheit} F ')
