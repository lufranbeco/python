import random
options = ['ROCK', 'PAPER', 'SCISSORS']
while True:
    question = int(input("\nHow many rows you wanna play?: "))

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
        elif computer != user.upper():
            if computer == 'ROCK' and user.upper() == "SCISSORS":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")

            elif computer == 'SCISSORS' and user.upper() == "ROCK":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")

            elif computer == 'ROCK' and user.upper() == "PAPER":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")

            elif computer == 'PAPER' and user.upper() == "ROCK":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")

            elif computer == 'PAPER' and user.upper() == "SCISSORS":
                print(f"\n(Computer) {computer} <- {user.upper()} (You)")
                print("You win!")

            elif computer == 'SCISSORS' and user.upper() == "PAPER":
                print(f"\n(Computer) {computer} -> {user.upper()} (You)")
                print("You loose!")