import random 

print("¡WELCOME!\nWhat do you wanna play?\n1. You choose a random number and computer guess\n2. Computer choose a random number and you guess")

game = True
question = int(input("Choose 1 or 2: "))

while game == True:

    if question == 1:
        print("\nOkay, now choose a random number and I will try to guess it")
        min = int(input("\nWrite the minimun number: "))
        max = int(input("\nWrite the maximun number: "))

        while True:
            computer = random.randint(min, max)
            snd_question = input(f"\nIs your number {computer}? y/n: ")

            if snd_question.upper() == "N" or snd_question.upper() == "NO":
                print("\nOk, another try..\n")

            elif snd_question.upper() == "Y" or snd_question == "YES":
                print("\nYess! I won!\n")
                again = input("Do yo wanna play again? y/n: ")

                if again.upper() == "N" or again.upper() == "NO":
                    print("\nIt's okay, see you soon...\n")
                    game = False
                    break

                else:
                    print("\nOkay, another round.")
                    break

# game = True
# while game == True:
#     min = int(input("\nWrite the minimun number: "))
#     max = int(input("\nWrite the maximun number: "))
#     number = random.randint(min, max)

#     while True:
#         user = int(input(f"\nGuess my number between {min} - {max}: "))

#         if user < min or user > max:
#             print(f"Mmm, it's between {min} and {max}")

#         elif user == number:
#             print("\n¡You guessed the number, congratulations!")
#             opcion = str(input("\n¿Do you wanna play again? y/n: "))

#             if opcion.upper() == "N":
#                 print("\nIt's OK, see you soon...\n")
#                 game=False
#                 break

#             else:
#                 break

#         else:
#             print("\nWrong number.. try again.")