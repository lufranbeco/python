import random
options = ['ROCK', 'PAPER', 'SCISSORS']
user=input("\nChoose between rock, paper and scissors: ")

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