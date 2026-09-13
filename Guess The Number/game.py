import random 

min = int(input("\nWrite the minimun number: "))
max = int(input("\nWrite the maximun number: "))

number = random.randint(min, max)

while True:
    user = int(input(f"\nGuess my number between {min} - {max}: "))
    if user < min or user > max:
        print(f"Mmm, it's between {min} and {max}")
    elif user == number:
        print("\n¡You guessed the number, congratulations!")
        opcion = str(input("\n¿Do you wanna play again? y/n: "))
        if opcion.upper() == "N":
            print("\nIt's OK, see you soon...\n")
            break 
    else:
        print("\nWrong number.. try again.")