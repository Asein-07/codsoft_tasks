import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

while True:
    user = input("\nEnter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")
    else:
        print("Computer Wins!")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing!")
        break