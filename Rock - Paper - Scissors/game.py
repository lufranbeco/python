# Import the random module to generate random choices for the computer
import random

# Define valid game choices in uppercase
options = ['ROCK', 'PAPER', 'SCISSORS']

# Main game loop allowing the player to replay as many rounds as he want
while True:
    # Ask the player how many rounds they want to play in this match
    question = int(input("\nHow many rounds you wanna play?: "))

    # Initialize scores for both computer and user at the start of the match
    compPoints = 0
    userPoints = 0
    
    # Loop through the agreed number of rounds
    for i in range(question):
        # Input validation loop to ensure a valid choice (Rock, Paper, or Scissors)
        while True:
            user = input("\nChoose between rock, paper and scissors: ")
            # Check if the converted uppercase input matches any valid option
            if user.upper() != "ROCK" and user.upper() != "PAPER" and user.upper() != "SCISSORS":
                print(f"\n{user}? that's not rock, paper or scissors, choose again")
            else:
                break  # Exit validation loop once valid input is given

        # Randomly select a choice for the computer from the options list
        computer = random.choice(options)

        # Game outcome evaluations:
        # Case 1: Tie game
        if computer == user.upper():
            print(f"\n(Computer) {computer} - {user.upper()} (You)")
            print("It's a tie!")
            print(f"{compPoints} - {userPoints}")
        
        # Case 2: Either player wins
        elif computer != user.upper():
            # Rock beats Scissors (Computer wins)
            if computer == 'ROCK' and user.upper() == "SCISSORS":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")
                compPoints += 1
                print(f"{compPoints} - {userPoints}")

            # Rock beats Scissors (User wins)
            elif computer == 'SCISSORS' and user.upper() == "ROCK":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")
                userPoints += 1
                print(f"{compPoints} - {userPoints}")

            # Paper beats Rock (User wins)
            elif computer == 'ROCK' and user.upper() == "PAPER":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")
                userPoints += 1
                print(f"{compPoints} - {userPoints}")

            # Paper beats Rock (Computer wins)
            elif computer == 'PAPER' and user.upper() == "ROCK":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")
                compPoints += 1
                print(f"{compPoints} - {userPoints}")

            # Scissors beats Paper (User wins)
            elif computer == 'PAPER' and user.upper() == "SCISSORS":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")
                userPoints += 1
                print(f"{compPoints} - {userPoints}")

            # Scissors beats Paper (Computer wins)
            elif computer == 'SCISSORS' and user.upper() == "PAPER":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")
                compPoints += 1
                print(f"{compPoints} - {userPoints}")

    # Display final match results after all rounds are completed
    print("\nThe end")
    if compPoints == userPoints:
        print("\nIt's a tie!")
        print(f"{compPoints} - {userPoints}")
    elif compPoints > userPoints:
        print("\nYou loose!")
        print(f"{compPoints} - {userPoints}")
    elif compPoints < userPoints:
        print("\nYou win!")
        print(f"{compPoints} - {userPoints}")

    # Input validation loop to check if the user wants to play another match
    while True:
        question2 = input("\nDo you wanna play again? Y/N: ")
        if question2.upper() != "Y" and question2.upper() != "N" and question2.upper() != "YES" and question2.upper() != "NO":
            print(f"\n{question2}? that's not y or n, choose again")
        else:
            break

    # Exit the main game loop if the player chooses 'N' or 'NO'
    if question2.upper() == "N" or question2.upper() == "NO":
        print("\nSee you later...")
        break