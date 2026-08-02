import random
options = ['ROCK', 'PAPER', 'SCISSORS']
while True:
    question = int(input("\nHow many rows you wanna play?: "))

    compPoints = 0
    userPoints = 0
    
    for i in range(question):
        while True:
            user=input("\nChoose between rock, paper and scissors: ")
            if user.upper() != "ROCK" and user.upper() != "PAPER" and user.upper() != "SCISSORS":
                print(f"\n{user}? that's not rock, paper or scissors, choose again")
            else:
                break

        computer=random.choice(options)

        if computer == user.upper():
            print(f"\n(Computer) {computer} - {user.upper()} (You)")
            print("It's a tie!")
            print(f"{compPoints} - {userPoints}")
        elif computer != user.upper():
            if computer == 'ROCK' and user.upper() == "SCISSORS":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")
                compPoints += 1
                print(f"{compPoints} - {userPoints}")

            elif computer == 'SCISSORS' and user.upper() == "ROCK":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")
                userPoints += 1
                print(f"{compPoints} - {userPoints}")

            elif computer == 'ROCK' and user.upper() == "PAPER":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")
                userPoints += 1
                print(f"{compPoints} - {userPoints}")

            elif computer == 'PAPER' and user.upper() == "ROCK":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")
                compPoints += 1
                print(f"{compPoints} - {userPoints}")

            elif computer == 'PAPER' and user.upper() == "SCISSORS":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")
                userPoints += 1
                print(f"{compPoints} - {userPoints}")

            elif computer == 'SCISSORS' and user.upper() == "PAPER":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")
                compPoints += 1
                print(f"{compPoints} - {userPoints}")

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
    while True:
        question2=input("\nDo you wanna play again? Y/N: ")
        if question2.upper() != "Y" and question2.upper() != "N" and question2.upper() != "YES" and question2.upper() != "NO":
            print(f"\n{question2}? that's not y or n, choose again")
        else:
            break

    if question2.upper() == "N" or question2.upper() == "NO":
        print("\nSee you later...")
        break