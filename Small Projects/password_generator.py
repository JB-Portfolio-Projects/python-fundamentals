#import modules for random password generation.
import random
import string
#adding version 1.2, imporove customization, add character type selections
while True:
    user_input  = input("Enter password length or 'q' to quit: ")
    
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    
    if user_input.isdigit():
        length = int(user_input)
        
        if length <= 0:
            print("Please enter a number greater than 0.")
            continue
        
        include_upper = input("Include uppercase letters? (y/n): ").lower()
        include_numbers = input("Include numbers? (y/n): ").lower()
        include_symbols = input("Include symbols? (y/n): ").lower()
        
        characters = string.ascii_lowercase
        
        if include_upper == 'y':
            characters += string.ascii_uppercase
            
        if include_numbers == 'y':
            characters += string.digits
            
        if include_symbols == 'y':
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        print("Generated password:", password) 
    else:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
            