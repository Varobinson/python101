
user_input = int(input('enter a number '))




while user_input > 0:
    if user_input % 5 == 0 and user_input % 3 == 0:
        print('fizzbuzz')
    elif user_input % 5 == 0:
        print('buzz')
    elif user_input % 3 == 0:
       print('fizz')
    else:
        print(user_input)
    user_input -= 1
