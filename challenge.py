import random

def rps_game():
    rps_list = ['rock', 'paper', 'scissors']

    user_inp = input('Rock, Paper, Scissors? ')

    machine_choice = random.choice(rps_list)
    print(machine_choice)

    if user_inp.lower() in rps_list:
        if user_inp == machine_choice:
            print('Tie!')
        elif user_inp == 'rock' and machine_choice == 'scissors':
            print(f'{user_inp} beats {machine_choice} You won!')
        elif user_inp == 'paper' and machine_choice == 'rock':
            print(f'{user_inp} beats {machine_choice} You won!')
        elif user_inp == 'scissors' and machine_choice == 'paper':
            print(f'{user_inp} beats {machine_choice} You won!')
        else:
            print('You lost!')
        rps_game()
    else:
        print('Invalid input, try again!')
        rps_game()

rps_game()