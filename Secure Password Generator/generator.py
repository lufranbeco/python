import secrets
import string
while True:
    question = input("Do yo want a secure password? Y/N:").upper()

    if question != "Y" and question != "YES" and question != "N" and question != "NO":
        print(f"That answer '{question}' isn't correct. Choose Y/yes or N/no")
    elif question == "N" or question == "NO":
        print("Ok, see you soon...") 
        break
    else:
        break

characters = string.ascii_letters + string.digits + string.punctuation
    
password = ''.join(secrets.choice(characters) for _ in range(16))
print(password)