user_inp = int(input('enter your fib number ' ))

fib1 = 0
fib2 = 1
counter = 0

while counter < user_inp:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    print(fib3)
    counter += 1



