import random

def rock_paper_scrissors(my_score, computer_score):
    print("Press 1 for rock\nPress 2 for scissors\nPress 3 for paper")
    player_choice = input("Enter your choice: ")
    if player_choice in ["1","2","3"]:
        choices={"1":"rock", "2":"scissors","3":"paper"}
        choice=choices[player_choice]
        computer_choice=random.choice(["rock", "scissors", "paper"])
        print(f"\nComputer chose {computer_choice}")
        if choice == computer_choice:
            print("It's a tie!")
        elif ((choice=="rock") and (computer_choice=="scissors")) or ((choice=="scissors") and (computer_choice=="paper")) or (choice=="paper") and (computer_choice=="rock"):
            print("You Win!")
            my_score+=1
        else:
            print("Computer Wins!")
            computer_score+=1
        
        print(f"Your score: {my_score}")
        print(f"Computer score: {computer_score}")
        print("Do you want to play again? ")
        play_again = input("Enter yes or no: ")
        if play_again=="yes":
            rock_paper_scrissors(my_score, computer_score)
        elif play_again=="no":
            print("Thanks for playing!!")
            print(f"Your score: {my_score}")
            print(f"Computer score: {computer_score}")
        else:
            print("Invalid input!!")
    else:
        print("Invalid choice!!")
        

my_score=0
computer_score=0
rock_paper_scrissors(my_score, computer_score)
