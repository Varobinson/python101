
try:
    day = int(input('Day (0-6)? '))
except: 
    print('Needs a number 0 -6! ')

# Fill in your code here


if day == 0:
    print('Sunday')
    if True:
        print('Sleep in')

elif day == 1:
    print('Monday')
    if True:
        print('Go to work')

elif day == 2:
    print('Tuesday')
    if True:
        print('Go to work')

elif day == 3:
    print('Wednesday')
    if True:
        print('Go to work')

elif day == 4:
    print('Thursday')
    if True:
        print('Go to work')

elif day == 5:
    print('Friday')
    if True:
        print('Go to work')

elif day == 6:
    print('Saturday')
    if True:
        print('Sleep in')

else:
    print('Wrong Planet!')
