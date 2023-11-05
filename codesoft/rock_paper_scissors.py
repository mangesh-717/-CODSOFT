import random
class Code_soft_game:
    def __init__(self):
        self.computer_score=0
        self.user_score=0

# displaying rules
    def display_rules(self):
        print("Welcome to Rock-Paper-Scissors Game!")
        print("You will play against the computer. Choose 'rock', 'paper', or 'scissors'.")
        print("The winning conditions are as follows:")
        print("1. Rock beats Scissors.")
        print("2. Scissors beats Paper.")
        print("3. Paper beats Rock.")
        print("Type 'quit' to end the game.")

        #implementation of game features 
    def play(self):
        temp=1
        l1=['rock','paper','scissors']
        iterations=0
        while iterations<5:
            user_choice = input("Choose 'rock', 'paper', or 'scissors' for end type quit : ").lower()
            print("______________________!!____________________________")

            computer_choice=random.choice(l1)
            if user_choice not in l1:
                print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
                continue
            elif user_choice == "quit":
                break
            elif user_choice==computer_choice:
                print("It's a tie!")
                temp=0
            elif ((user_choice == "rock" and computer_choice == "scissors") or 
                  (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")):
                self.user_score+=1
                iterations+=1

            else:
                self.computer_score+=1
                iterations+=1

            #if it's tie this thing will not be printed
            if temp==True:
                print('computer chosed :-',computer_choice)
                print('You choced :-',user_choice)
                print('your current score:-',self.user_score)


# final result with score
    def result(self):
        print("Game over!...")
        print("______________________!!____________________________")
        if self.user_score>self.computer_score:
            print('congratulations you win!...')
        else:
            print('computer win!...')
        print('your final score is:-',self.user_score)
        print('computer final score is:-',self.computer_score)


c=Code_soft_game()
c.display_rules()
c.play()
c.result()