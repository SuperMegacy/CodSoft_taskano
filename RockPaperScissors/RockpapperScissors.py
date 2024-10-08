import random

def user_menu():
    print('\t\tWelcome to Rock Paper Scissors!')
    print("")
    user_choice = input('Please choose rock, paper, or scissors: ').lower()
    return user_choice

def game(user_option):
    game_play = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {game_play}")

    if game_play == user_option:
        print("It is a tie!")
        return 0  # No score change on a tie
    elif (game_play == "rock" and user_option == "scissors") or \
         (game_play == "paper" and user_option == "rock") or \
         (game_play == "scissors" and user_option == "paper"):
        print("You have lost!")
        return 0  # No score change on a loss
    else:
        print("You have won!")
        return 1  # Increase score on a win

def main():
    score = 0  # Initialize score outside the loop
    while True:
        user_option = user_menu()
        if user_option not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue

        score += game(user_option)  # Accumulate the score
        print("Score: {}".format(score))

        another_round = input("Would you like to play again? (y/n): ").lower()
        if another_round == "y":
            continue
        elif another_round == "n":
            print("Your High Score is: {}".format(score))
            print("Thank you for playing!")
            break
        else:
            print("Invalid input, please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
