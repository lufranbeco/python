import random 

number = random.randint(0, 10)

while True:
    user = int(input("\nGuess my number between 0 - 10: "))
    if user == number:
        print("\n¡You guessed the number, congratulations!")
        opcion = str(input("\n¿Do you wanna play again? y/n: "))
        if opcion.upper() == "N":
            print("\nIt's OK, see you soon...\n")
            break 
    else:
        print("\nWrong number.. try again.")