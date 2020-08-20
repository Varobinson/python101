    
user_input = input('Enter a sentence! ')
user_input = user_input.upper()

for letter in user_input:
    if letter == 'A':
        print(4)
    elif letter == 'E':
        print(3)
    elif letter == 'G':
        print(6)
    elif letter == 'I':
        print(1)
    elif letter == 'O':
        print(0)
    elif letter == 'S':
        print(5)
    elif letter == 'T':
        print(7)
    else:
        print(letter)
    
