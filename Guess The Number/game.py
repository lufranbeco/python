# Import module for random number generation
import random 

# Display game interface and mode selection options
print("¡WELCOME!\nWhat do you wanna play?\n1. You choose a random number and computer guess\n2. Computer choose a random number and you guess")

# Execution flag for the main game loop
game = True

# Capture selected game mode
question = int(input("Choose 1 or 2: "))

# Main game control loop
while game == True:

    # Mode 1: Computer guesses user's secret number
    if question == 1:

        # Display mode instructions
        print("\nOkay, now choose a random number and I will try to guess it")

        # Define boundary limits for target range
        min = int(input("\nWrite the minimun number: "))
        max = int(input("\nWrite the maximun number: "))

        # Round execution loop
        while True:

            # Generate random prediction within defined range
            computer = random.randint(min, max)

            # Prompt user to verify computer's guess
            snd_question = input(f"\nIs your number {computer}? y/n: ")

            # Handle incorrect guess
            if snd_question.upper() == "N" or snd_question.upper() == "NO":
                print("\nOk, another try..\n")

            # Handle correct guess and evaluate replay choice
            elif snd_question.upper() == "Y" or snd_question == "YES":
                print("\nYess! I won!\n")
                again = input("Do yo wanna play again? y/n: ")

                # Terminate loop if user declines replay
                if again.upper() == "N" or again.upper() == "NO":
                    print("\nIt's okay, see you soon...\n")
                    game = False
                    break

                # Continue execution for a new round
                else:
                    print("\nOkay, another round.")
                    break

    # Mode 2: User guesses computer's secret number
    elif question == 2:

        # Display mode instructions
        print("\nOkay, I will choose a number that you will try to guess")

        # Flag for mode 2 loop execution
        game = True

        # Mode 2 main loop
        while game == True:

            # Define boundary limits for target range
            min = int(input("\nWrite the minimun number: "))
            max = int(input("\nWrite the maximun number: "))

            # Generate secret target number within range
            number = random.randint(min, max)

            # Active guessing loop
            while True:

                # Capture user attempt
                user = int(input(f"\nGuess my number between {min} - {max}: "))

                # Validate attempt against defined range limits
                if user < min or user > max:
                    print(f"Mmm, it's between {min} and {max}")

                # Process successful match
                elif user == number:

                    # Display success message
                    print("\n¡You guessed the number, congratulations!")

                    # Prompt user for replay preference
                    opcion = str(input("\n¿Do you wanna play again? y/n: "))

                    # Terminate game loop if user declines
                    if opcion.upper() == "N":
                        print("\nIt's OK, see you soon...\n")
                        game=False
                        break

                    # Reset round for new game
                    else:
                        break

                # Handle incorrect guess attempt
                else:
                    print("\nWrong number.. try again.")