import random
choices = ['rock','paper','scissor']
def play_games():
    while True:
        user_input = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_input == 'q':
            print("Thanks for playing")
            break

        if user_input not in choices:
            print("invalid choice. try again")
            continue

        pc_choice =random.choice(choices)
        print(f"pc chose:{pc_choice} ")

        if user_input == pc_choice:
            print("Its a tie")
        elif (user_input == "rock" and pc_choice == "scissors") or \
             (user_input == "scissors" and pc_choice == "paper") or \
             (user_input == "paper" and pc_choice == "rock"):
            print("YOu win")

        else:
            print("You lose")


if __name__ == "__main__":
    play_games()

