import random as r
from timer import Timer

timerObj = Timer()
timerObj.start()

print('\n\n\t\t==+-+-== GUESS THE NUMBER ==-+-+-+==\n\n\nGameplay:\n1. Enter the max guess limit\n2. Now you will have three chances to guess the number\nAs simple as that ;)')

while True:
    opt = int(input('Enter 1 to start game\n----- 2 to look at stats\n----- 0 to exit:\t'))
    if opt not in range(3): 
        print('\nChoose a correct option\n')
        continue
    if opt == 1:
        maxL = int(input('\nEnter the max number: '))
        num = r.randint(1, maxL)
        chance = 3
        accuracy = 1.0
        while chance != 0 :
            guess = int(input('\nGuess the number: '))
            if num != guess:
                print('\nOopsyyy :-/ Wrong guess')
                chance -= 1
                if chance == 0:
                    accuracy = 0.0
                    print(f'\nOut of chances :( \n\nThe correct number is: {num}\nYour accuracy is: {accuracy}\n')
                    break
                print(f'You have {chance} chance(s) left.')
                continue
            accuracy = round(chance/3.0, 2)
            print(f'\n\tYay!  Correct guess :) the number is {num}\nYour accuracy is: {accuracy}\n')
            break
    else: 
        print('\n\t\tSee ya ')
        break

exe_time = timerObj.stop()
print(f'Total elapsed time is: {exe_time:0.4f} secs')