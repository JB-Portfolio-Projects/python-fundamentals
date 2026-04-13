for i in range(10):
    print("The value of i is currently", i)

    #The range() function invocation may be equipped with two arguments, not just one:
for i in range(2, 8):
    print("The value of i is currently", i)
    #In this case, the first argument determines the initial (first) value of the control variable.


#The last argument shows the first value the control variable will not be assigned.

#Note: the range() function accepts only integers as its arguments, and generates sequences of integers.

#Let's have a look at a short program whose task is to write some of the first powers of two:

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

#The expo variable is used as a control variable for the loop, and indicates the current value of the exponent.

#write a program that uses a for loop to "count mississippily" to five. Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"

import time
# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come")
# Write a print function with the final message.

#Collatz's hypothesis
n = int(input("Enter a natural number: "))

steps = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
        
    print(n)
    steps += 1
    
print("steps =", steps)