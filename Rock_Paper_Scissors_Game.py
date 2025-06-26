import random

print("---Welcome to Rock-Paper-Scissors Game!---")

options = ("rock" , "paper" , "scissors")
running = True

while running:
    
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("\nEnter a choice (rock,paper,scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("Its a tie!!")
        elif player == "rock" and computer == "scissors":
            print("Rock smashes scissors! You win!!")
        elif player == "paper" and computer == "rock":
            print("Paper wraps rock! You win!!")
        elif player == "scissors" and computer == "paper":
            print("scissors cuts paper! You win!!")
        else:
            print("You lose...")

        if not input("\nPlay again? (y/n): ").lower() == "y":
            running = False

print("Thanks for playing!")
