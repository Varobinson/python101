#Write a program that will prompt you for how many coins you want.
# Initially you have no coins. It will ask you if you want a coin? 
# If you type "yes", it will give you one coin, and print out the current
# tally. If you type no, it will stop the program.

#initial coin pile
coins = 0
#prompting user to ask for coins
question = input('Do you want a coin? ')
#creating loop
while question == 'yes':
    #adding coins for every yes
    coins += 1
    #printing coin total for every yes
    print(coins)
    #re asking until i get a no
    question = input('Do you want a coin? ')
    

