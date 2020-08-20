#Print a NxN square of * characters. Prompt the user for N

#in case of error
try:
    #Prompting user for their number
    square = int(input('How big is this square? '))
    #error type and error message
except:
    print('Needs a number!')

#test variable
counter = 0
while counter < square:
    print('*' * square)
    counter += 1
