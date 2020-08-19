#Prompt the user for a number in degrees Celsius, 
#and convert the value to degrees in Fahrenheit and 
#display it to the user.

#prompt user
degrees_celsius = input('What is the degrees celcius? ')

#take user input and convert it to integer
degrees_celsius = int(degrees_celsius)
#convert celsius to fahrenheit
degrees_fahrenheit = (degrees_celsius * 9/5) + 32 
#return fahrenheit to user
print(f'{degrees_fahrenheit} F ')
