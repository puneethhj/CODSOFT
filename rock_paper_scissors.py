import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    print("Rock-Paper-Scissors Game")
    print("========================")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("You win this round!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Exiting the game. Final Score:")
            print(f"You {user_score} - {computer_score} Computer")
            break

if __name__ == "__main__":
    main()
