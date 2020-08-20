    
user_input = input('Enter a sentence! ')
user_input = user_input.upper()

translate = ''

for letter in user_input:
    if letter == 'A':
        translate += '4'
    elif letter == 'E':
        translate += '3'
    elif letter == 'G':
        translate += '6'
    elif letter == 'I':
        translate += '1'
    elif letter == 'O':
        translate += '0'
    elif letter == 'S':
        translate += '5'
    elif letter == 'T':
        translate += '7'
    else:
        translate += letter
print(letter)
    
