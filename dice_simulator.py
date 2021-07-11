import random as r

while True:
    i = int(input(' Press 1 to roll the dice \t 0 to exit:  '))
    if i == 1: 
        num = r.randint(1,6)
        print(num)
    else :
        break
