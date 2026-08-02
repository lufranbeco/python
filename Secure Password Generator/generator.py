# Import modules for random length selection, cryptographically secure randomness, and string constants
import random
import secrets
import string

# Loop continuously until the user provides a valid response
while True:
    # Prompt the user for input and convert it to uppercase for easy comparison
    question = input("Do yo want a secure password? Y/N:").upper()

    # Check if the input is anything other than Y, YES, N, or NO
    if question != "Y" and question != "YES" and question != "N" and question != "NO":
        print(f"That answer '{question}' isn't correct. Choose Y/yes or N/no")
    # If the user declines, print a goodbye message and exit the loop
    elif question == "N" or question == "NO":
        print("Ok, see you soon...") 
        break
    # If the user accepts, exit the loop to proceed with password generation
    else:
        break

# Randomly select a password length between 12 and 16 characters
length = random.choice([12, 13, 14, 15, 16])

# Combine letters (lowercase and uppercase), digits, and punctuation marks into a single string
characters = string.ascii_letters + string.digits + string.punctuation
    
# Generate a secure password of the chosen length using cryptographically secure random selection with 'secrets'
password = ''.join(secrets.choice(characters) for _ in range(length))

# Display the generated password along with its character length
print("\nHere is your password:")
print(f"    {password} --> {length} characters\n")