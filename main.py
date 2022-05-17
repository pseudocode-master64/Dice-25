from random import randint
import prettytable 
from prettytable import PrettyTable

BOARD = [[0 for _ in range(5)] for _ in range(5)]

COUNT = 1

TOTAL_SCORE = 0

# Roll the dice
DICE = randint(1, 6)

def display_table():    
    """Configuration of the board's User Interface"""

    # Initialize Table
    x = PrettyTable()
    x.hrules = prettytable.ALL
    x.vrules = prettytable.ALL  

    # Print out the board

    #Insert r1-r9
    x.field_names = [f'c{i+1}'for i in range(5)]

    # Add 2D array to the table
    for i in range(5):
        x.add_row(BOARD[i])

    #Insert c1-c9
    fieldname = '--'
    x._field_names.insert(0, fieldname) 
    x._align[fieldname] = 'c' 
    x._valign[fieldname] = 't' 
    for i, _ in enumerate(x._rows): 
        x._rows[i].insert(0, f'r{i+1}')

    print(x)

    # Clear all rows
    x.clear()   


def register_position(row, column):  
    """Return dice roll number and the current board at terminal """

    # Count how many dice rolls made

    global COUNT
    global DICE

    row -= 1
    column -= 1

    index = (row*5)+column
    column_index = index % 5

    if BOARD[row][column_index] != 0:
        print("There's already a value in this position, choose another spot!")
        return
    elif row > 4 or column > 4:
        print('value out of range, try again')
        return
    else:
        BOARD[row][column_index] = DICE
        COUNT += 1
        DICE = randint(1,6)


def r_score_count(row: int) -> list:
    """Identify the patttern and the total score of each column"""

    global TOTAL_SCORE
    board_list = BOARD[row]
    board_set = set(BOARD[row])

    #Sequence
    if BOARD[row] == [1,2,3,4,5]:
        TOTAL_SCORE += 80
        return['Sequence', 80]

    #Five
    if len(board_set) == 1:
        TOTAL_SCORE += 70
        return['Five', 70]

    #Four 
    four = 0
    for num in board_set:
        if board_list.count(num) == 4:
            four += 1
    if four == 1:
        TOTAL_SCORE += 50
        return['Four', 50]

    #Three plus two
    triple = 0
    pairs = 0
    for num in board_set:
        if board_list.count(num) == 3:
            triple += 1
        if board_list.count(num) == 2:
            pairs += 1
    if triple == 1 and pairs == 1:
        TOTAL_SCORE += 30
        return['Three plus Two', 30]

    #Three
    triple = 0
    for num in board_set:
        if board_list.count(num) == 3:
            triple += 1
    if triple == 1:
        TOTAL_SCORE += 30
        return['Three', 20]

    #Two plus Two
    pairs = 0
    for num in board_set:
        if board_list.count(num) == 2:
            pairs += 1
    if pairs == 2:
        TOTAL_SCORE += 15
        return['Two plus Two', 15]
    
    #Two
    pairs = 0
    for num in board_set:
        if board_list.count(num) == 2:
            pairs += 1
    if pairs == 1:
        TOTAL_SCORE += 5
        return['Two', 5]
    
    #Nil
    if len(board_set) == 5 and BOARD[row] != [1,2,3,4,5]:
        return['Nil', 0]


def c_score_count(column:int) -> list:
    """Identify the patttern and the total score of each column"""

    global TOTAL_SCORE
    global BOARD

    column_list = [[BOARD[row][row_index] for row in range(5)] for row_index in range(5)]
    column_board_set = set(column_list[column])

    #Sequence
    if column_list[column] == [1,2,3,4,5]:
        TOTAL_SCORE += 80
        return['Sequence', 80]

    #Five
    if len(column_board_set) == 1:
        TOTAL_SCORE += 70
        return['Five', 70]

    #Four 
    four = 0
    for num in column_board_set:
        if column_list.count(num) == 4:
            four += 1
    if four == 1:
        TOTAL_SCORE += 50
        return['Four', 50]

    #Three plus two
    triple = 0
    pairs = 0
    for num in column_board_set:
        if column_list.count(num) == 3:
            triple += 1
        if column_list.count(num) == 2:
            pairs += 1
    if triple == 1 and pairs == 1:
        TOTAL_SCORE += 30
        return['Three plus Two', 30]

    #Three
    triple = 0
    for num in column_board_set:
        if column_list.count(num) == 3:
            triple += 1
    if triple == 1:
        TOTAL_SCORE += 30
        return['Three', 20]

    #Two plus Two
    pairs = 0
    for num in column_board_set:
        if column_list.count(num) == 2:
            pairs += 1
    if pairs == 2:
        TOTAL_SCORE += 15
        return['Two plus Two', 15]
    
    #Two
    pairs = 0
    for num in column_board_set:
        if column_list.count(num) == 2:
            pairs += 1
    if pairs == 1:
        TOTAL_SCORE += 5
        return['Two', 5]
    
    #Nil
    if len(column_board_set) == 5 and BOARD[column] != [1,2,3,4,5]:
        return['Nil', 0]


def scoreboard():
    """Checks each row and column and calculate the total score"""

    row_table = PrettyTable()
    row_table.field_names = ['Row', 'Result', 'Score']
    for i in range(5):
        row_data = r_score_count(i)
        row_table.add_row([f'r{i+1}', row_data[0], row_data[1]])
    
    column_table = PrettyTable()
    column_table.field_names = ['Column', 'Result', 'Score']
    for i in range(5):
        column_data = c_score_count(i)

        column_table.add_row([f'c{i+1}', column_data[0], column_data[1]])

    print(row_table)
    print(column_table)
    
    print(f'Final Score: {TOTAL_SCORE}')

def Simulation(dice_throw, board):

    dice_throw = DICE
    board = BOARD
    row = 0
    column = 0

    for _ in range (5):
        row += 1
        for _ in range (5):
            column += 1
            for index in board[row][column]:
                pass

    



while True:
    if COUNT < 3:
        print('\n'f'dice roll #{COUNT}')
        print(('\n'f'You have rolled a {DICE}''\n'))
        display_table()
        register_position(int(input('Which row? ')), int(input('Which column? ')))
    else:
        display_table()
        scoreboard()



