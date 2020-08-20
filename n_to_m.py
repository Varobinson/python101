#same but you will prompt the user for the number
#to start on  and the number to end on

#prompt user on start and stop number
try:
    start_num = int(input('What number should I start on? '))
    end_num = int(input('What number should I end on? '))
except:
    print('Enter a number')

#entering user input into loop
while start_num < end_num + 1:
    print(start_num)
    start_num += 1
