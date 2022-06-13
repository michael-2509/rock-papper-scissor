import random
computer_list = ['R', 'P','S']

def start_game():
    computer = random.choice(computer_list)
    # print(computer)
    user = input('''\nEnter R FOR ROCK, S FOR SCISSOP AND P FOR PAPER: ''').upper()
    
    while user not in computer_list:
        print("invalid response\n")
        start_game()
        
    def store_game():
        print(f'PLAYER {user}: CPU {computer}')

    if user == computer:
        store_game()
        print("it's a tie \n Play Again")
        start_game()

    elif user == 'R' and computer == 'P':
        store_game()
        print("you lost")
        repeat()

    elif user == 'R' and computer == 'S':
        store_game()
        print("you win")
        repeat()

    elif user == 'P' and computer == 'R':
        store_game()
        print("you won")
        repeat()

    elif user == 'P' and computer == 'S':
        store_game()
        print("you lost")
        repeat()

    elif user == 'S' and computer == 'R':
        store_game()
        print("you lost")
        repeat()

    elif user == 'S' and computer == 'P':
        store_game()
        print("you lost")
        repeat()

    else:
        print("invalid response\n")
        start_game()

def repeat():
    user_input = input('''\nwould you like to continue?
    Enter Y for yes and N for No: \n''')
    
    if user_input.upper() == 'Y':
        start_game()
        
    elif user_input.upper() == 'N':
        print('\nGame Over ')
    
    else:
        repeat()


    
start_game()