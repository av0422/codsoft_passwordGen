#TASK 3 'PASSWORD GENERATOR'

import string 
import random

length = int(input("Enter desired length of the password: "))

def generate_password(length):
    
    # Defining character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '@#$%&?'

    # Combining character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensuring the length is at least 8 characters
    length = max(length, 8)

    # Generating password
    password = random.sample(all_characters, length)
    password = ''.join(password)

    return password

generated_password = generate_password(length)
print("Generated Password:", generated_password)
