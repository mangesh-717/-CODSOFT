import string
import random


# Define a custom exception for invalid password length
class InvalidPasswordLengthError(Exception):
    pass

length = 0


print("Codesoft Password Generator")


try:
    # Get the desired password length from the user
    length = int(input("Enter the desired password length: "))
except ValueError:
    # Raise a custom exception if the user enters a non-integer value
    raise InvalidPasswordLengthError()


# Define your character sets
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation


password =[]
temp=0
all_remain_chars=''



# Prompt the user to include uppercase letters
use_uppercase = input("Include uppercase letters? (y/n): ").lower()
if use_uppercase=='y':
    # Add a random uppercase character to the password
    password.append(random.choice(upper))
    all_remain_chars+=upper
    temp+=1

# Prompt the user to include lowercase letters
use_lowercase = input("Include lowercase letters? (y/n): ").lower()
if use_lowercase=='y':
    # Add a random lowercase character to the password
    password.append(random.choice(lower))
    all_remain_chars+=lower
    temp+=1


# Prompt the user to include digits
use_digits = input("Include digits (0-9)? (y/n): ").lower()
if use_digits=='y':
    # Add a random digit to the password
    password.append(random.choice(digits))
    all_remain_chars+=digits
    temp+=1


# Prompt the user to include special characters
use_special_chars = input("Include special characters? (y/n): ").lower()
if use_special_chars=='y':
    # Add a random special character to the password
    password.append(random.choice(punctuation))
    all_remain_chars+=punctuation
    temp+=1


# Check if the selected password length and character types are valid
if length<4 and temp >length:
    print("Password length is too long for the selected character types.\nTry again!...")
    exit()


# Generate the remaining password characters
for _ in range(length - temp):
    password.append(random.choice(all_remain_chars))


# Display the generated password
print("Generated password:-",''.join(password))
