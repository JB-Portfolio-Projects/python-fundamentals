#import random and string,  input to define legnth.
import random
import string

length = int(input("Enter password length : "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

#need random generation of password, so use random.choice to select random characters from the defined character set.
for _ in range(length):
    password += random.choice(characters)
    
print("Generated password : ", password)