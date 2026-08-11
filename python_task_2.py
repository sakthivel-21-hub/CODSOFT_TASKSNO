import random

def play_game():
    """Main function to run the Rock-Paper-Scissors game."""
    print("=========================================")
    print("       ROCK-PAPER-SCISSORS GAME          ")
    print("=========================================")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    
    # Score Tracking 
    user_score = 0
    computer_score = 0
    
    # Valid options
    choices = ['rock', 'paper', 'scissors']

    while True:
        # 1. User Input
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower().strip()
        
        if user_choice not in choices:
            print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # 2. Computer Selection
        computer_choice = random.choice(choices)

        # 3. Display Choices
        print(f"\n> You chose: {user_choice.capitalize()}")
        print(f"> Computer chose: {computer_choice.capitalize()}")

        # 4. Game Logic & Result
        if user_choice == computer_choice:
            print("=> It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("=> You win this round!")
            user_score += 1
        else:
            print("=> Computer wins this round!")
            computer_score += 1

        # Display Current Score
        print("-" * 41)
        print(f"SCORE: You [{user_score}] - Computer [{computer_score}]")
        print("-" * 41)

        # 5. Play Again
        play_again = input("Do you want to play another round? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_game()