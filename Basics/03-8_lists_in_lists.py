#builds a list containing eight elements representing the second row of the chessboard 
# - the one filled with pawns (assume that WHITE_PAWN is a predefined symbol representing a white pawn).

row = []

for i in range(8):
    row.append(WHITE_PAWN)

#A list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.
row = [WHITE_PAWN for i in range(8)]

#other examples
squares = [x ** 2 for x in range(10)]

#The snippet produces a ten-element list filled
# with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
twos = [2 ** i for i in range(8)]

#The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)
odds = [x for x in squares if x % 2 != 0 ]

#Let's also assume that a predefined symbol named EMPTY designates an empty field on the chessboard.
#So, if we want to create a list of lists representing the whole chessboard, it may be done in the following way:

board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

#As list comprehensions can be nested, we can shorten the board creation in the following way:
board = [[EMPTY for i in range(8)] for j in range(8)]

#chess board with indices example
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

#If you want to add a knight to C4, you do it as follows:
board[4][2] = KNIGHT
#And now a pawn to E5:
board[3][4] = PAWN

#Imagine that you develop a piece of software for an automatic weather station. 
# The device records the air temperature on an hourly basis and does it throughout the month. 
# This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.
temps = [[0.0 for h in range(24)] for d in range(31)]

#Now it's time to determine the monthly average noon temperature. 
# Add up all 31 readings recorded at noon and divide the sum by 31. 
# You can assume that the midnight temperature is stored first. Here's the relevant code:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#Now find the highest temperature during the whole month - see the code:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

#Now count the days when the temperature at noon was at least 20 ℃:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

#three-dimensional arrays
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#The first index (0 through 2) selects one of the buildings; 
# the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.
#Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
rooms[1][9][13] = True
#and release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False
#Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

#[expression for element in list if conditional]
#for element in list:
    #if conditional:
        #expression

#Here's an example of a list comprehension ‒ 
# the code creates a five-element list filled with the first five natural numbers raised to the power of 3:
cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]
#You can use nested lists in Python to create matrices (i.e., two-dimensional lists). For example:
# A four-column/four-row table ‒ a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

#You can nest as many lists in lists as you want, thereby creating n-dimensional lists, 
# e.g., three-, four- or even sixty-four-dimensional arrays. For example:
# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'