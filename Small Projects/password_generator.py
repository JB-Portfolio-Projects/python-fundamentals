#import modules for random password generation.
import random
import string

while True:
    user_input  = input("Enter password length or 'q' to quit: ")
    
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    
    if user_input.isdigit():
        length = int(user_input)
        
        if length > 0:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ""
            
            for _ in range(length):
                password += random.choice(characters)
                
            print("Generated password:", password)
        else:
            print("please enter a number greater than 0.")
    else:
        print("Invalid input. Please enter a number.")