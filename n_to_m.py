#same but you will prompt the user for the number
#to start on  and the number to end on

#prompt user on start and stop number

start_num = input('What number should I start on? ')
end_num = input('What number should I end on? ')
#converting to int
start_num = int(start_num)
end_num = int(end_num) 

#entering user input into loop
while start_num < end_num + 1:
    print(start_num)
    start_num += 1
