#Print a NxN square of * characters. Prompt the user for N

#Prompting user for their number
square = input('How big is this square? ')
#converting number to int
square = int(square)
#test variable
counter = 0
while counter < square:
    print('*' * square)
    counter += 1
