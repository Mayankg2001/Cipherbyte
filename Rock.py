import random
while True:

    print("Enter your choice to play this game Made By: Mayank Gupta\n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user

    choice = int(input("Enter your choice :"))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

        
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

       
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

   
    comp_choice = random.randint(1, 3)

   
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
   # Check for draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins\n', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins \n', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins \n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins \n', end="")
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins\n ', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins \n', end="")
        result = 'Scissors'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("---- Its a tie ----")
    if result == choice_name:
        print("---- User wins ----")
    else:
        print("---- Computer wins ----")
    print("Do you want to play again? (Y/N)")
    
    output = input().lower()
    if output == 'n':
        break

print("Thanks for Playing the game!!")
