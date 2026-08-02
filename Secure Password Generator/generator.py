while True:
    question = input("Do yo want a secure password? Y/N:").upper()

    if question != "Y" and question != "YES" and question != "N" and question != "NO":
        print(f"That answer '{question}' isn't correct. Choose Y/yes or N/no")
    elif question == "N" or question == "NO":
        print("Ok, see you soon...") 
        break