#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random


# Body

def num_guess():
    answer = random.randint(1, 25)
    count = 0
    input_num = ''
    while count < 5:
        try:
            input_num = int(input("Guess an integer from 1 - 25: "))
        except:
            print("Your number is not an integer. Try again!")
        if input_num not in range(1, 26):
            print("Your number is not in the range. Try again!")
        elif input_num  == answer:
            print('You won! The guess number is ' + str(answer)) 
            break
        elif input_num > answer:
            print('Your number is too high. Try again!')
            count += 1
            print('you can try ' + str(5 - count) + ' times.')
            continue
        elif input_num < answer:
            print('Your number is too low. Try again!')
            count += 1
            print('you can try ' + str(5 - count) + ' times.')
            continue
    else:
        print('Game is over. Try again.')        
               

################################################################################
def main():
    num_guess()


    
if __name__ == '__main__':
    main()