# Define number values to the presepctive roman numeral
def to_roman(num):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ] 
#input and get result
    result = ""
    for value, symbol in values:
        while num >= value:
            result += symbol
            num -= value

    return result

while True:
    user_input = input("Enter a year (1-3999) or 'q' to quit: ")
    
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    
    if user_input.isdigit():
        year = int(user_input)
        if 1 <= year <= 3999:
            print("Roman numeral:", to_roman(year))
        else:
            print("Please enter a number between 1 and 3999.")
    else:
        print("Invalid input. Please enter a number.")