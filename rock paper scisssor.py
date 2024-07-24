import random
def choice():
    you_score = 0
    computer_score = 0
    print("Rock-Paper-Scissors Game")
    print("Rock-R")
    print("Paper-p")
    print("Scissors-S")
    value = True
    while value == True:
        user_choice = input("Select choice for the above option to continue the game: ").lower()
        if user_choice in (['rock', 'paper', 'scissors']):
            value = False
        else:
            print("INVALID CHOICE!!")
        computer_choice=pc()
        print(f"you-{user_choice} computer-{computer_choice}")
        answer=winner(user_choice,computer_choice)
        if answer =="YOU WIN":
            you_score+=1
        else:
            computer_score+=1
        print(answer)
        print(f"{you_score}-{computer_score}")
        play_again = input("Do you want to play again?(yes/no)").lower()
        if play_again == "yes":
            value = True
        elif play_again == "no":
            print("THANK YOU !!")
            value = False

def pc():
    return random.choice(['rock','scissors','paper'])
def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        result="DRAW"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (
            user_choice == 'scissors' and computer_choice == 'paper') or (
            user_choice == 'paper' and computer_choice == 'rock'):
        result="YOU WIN"
    else:
        result="YOU LOST"
    return result




choice()