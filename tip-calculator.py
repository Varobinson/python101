#Prompt the user for two things:

#The total bill amount
#The level of service, which can be one of the following:
# good, fair, or bad
#Calculate the tip amount and the total amount(bill amount + tip amount). 
# The tip percentage based on the level of service is based on:

#good -> 20%
#fair -> 15%
# bad -> 10%
try:
#Ask user for total bill amount 
  total_bill = int(input('What was your total? '))
#convert total to float

#prompt user for service quality
  service = input('What was the service bad, fair, or good? ')

#adding split feature
  #promt user for split amount
  split = input('How many people will be paying? ')
except:
  print('error')

  #convert split to int
split = int(split)
tip = ()
service = service.lower()    

if service == 'bad':
    tip = total_bill * 0.1
elif service == 'fair':
    tip = total_bill * 0.15
elif service == 'good':
    tip = total_bill * 0.2
else: 
    print("Cant't help you! ")
#added split to total
total = total_bill + tip / split

print(total)
