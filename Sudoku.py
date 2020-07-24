# Sudoku game and solver using python
# solver uses backtracking algorithm

import pprint
from random import shuffle, randint
from copy import deepcopy
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]

empty_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

counter = 0 

# Make a new game with new board
def generate_filled_board(bo):
    empty_slot = find_empty_slot(empty_board)
    if not empty_slot:
        return True
    row, col = empty_slot
    number_list = list(range(1,10))
    shuffle(number_list)
    for value in number_list:
        if (valid_input(bo, value, empty_slot)):
            bo[row][col] = value
            if generate_filled_board(bo):
                return True
            bo[row][col] = 0

    print("unable to solve")
    return False

# Solve the game
def solver(bo):
    global counter
    empty_slot = find_empty_slot(bo)

    if not empty_slot:
        # Finish solving Sudoku
        return True

    row, col = empty_slot

    for i in range(1, 10):
        if valid_input(bo, i, empty_slot):
            bo[row][col] = i
            if solver(bo):
                return True
            
            bo[row][col] = 0

    return False


def find_empty_slot(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

def valid_input(bo, input, pos):
    row_pos = pos[0]
    col_pos = pos[1]

    for i in range(len(bo[0])):
        if col_pos != i and bo[row_pos][i] == input:
            return False   
        if row_pos != i and bo[i][col_pos] == input:
            return False    

    box_row_pos = pos[0] // 3
    box_col_pos = pos[1] // 3

    for i in range(box_row_pos * 3, box_row_pos * 3 + 3):
        for j in range(box_col_pos * 3, box_col_pos * 3 + 3):
            if input == bo[i][j] and (i, j) != pos:
                return False
    return True

def print_board(bo): 
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def insert_number(bo, input, pos):
    row = pos[0]
    col = pos[1]
    if bo[row][col] != 0:
        print("Position filled, try another position")
    else:
        if valid_input(bo, input, pos):
            bo[row][col] = input
        else:
            print("Invalid input, try another number")

def remove_number(bo, pos):
    row = pos[0]
    col = pos[1]
    number_being_removed = bo[row][col]
    bo[row][col] = 0
    return number_being_removed

# Try to make an empty half-filled board

def generate_playable_board(bo):
    attempts = 5
    global counter
    while attempts > 0:
        row, col = (randint(0,8), randint(0,8))
        while bo[row][col] == 0:
            row, col = (randint(0,8), randint(0,8))
        back_up = remove_number(bo, (row, col))
        copy_board = deepcopy(bo)
        counter = 0
        solver(copy_board)
        if counter != 1:
            bo[row][col] = back_up
            attempts -= 1
    print_board(bo)

generate_filled_board(empty_board)
playable_board = deepcopy(empty_board)
generate_playable_board(playable_board)
print("===================================")
print_board(playable_board)
# print(counter)
# solver(board)
# print(counter)
# print_board(board)