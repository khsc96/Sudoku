# Sudoku game and solver using python
# solver uses backtracking algorithm

import pprint

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

# Make a new game with new board
def generate_boarad():
    pass

# Solve the game
def solver(board):
    empty_slot = find_empty_slot(board)

    if not empty_slot:
        # Finish solving Sudoku
        return True

    row, col = empty_slot

    for i in range(1, 10):
        if valid_input(board, i, empty_slot):
            print(i)
            print(empty_slot)
            board[row][col] = i
            print("--- one iteration ---")
            print_board(board)

            if solver(board):
                return True
            
            board[row][col] = 0

    return False


def find_empty_slot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def valid_input(board, input, pos):
    row_pos = pos[0]
    col_pos = pos[1]

    for i in range(len(board[0])):
        if col_pos != i and board[row_pos][i] == input:
            return False   
        if row_pos != i and board[i][col_pos] == input:
            return False    

    box_row_pos = pos[0] // 3
    box_col_pos = pos[1] // 3

    for i in range(box_row_pos * 3, box_row_pos * 3 + 3):
        for j in range(box_col_pos * 3, box_col_pos * 3 + 3):
            if input == board[i][j] and (i, j) != pos:
                return False
    return True

def print_board(board): 
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)
print("------------------------")
solver(board)
print_board(board)
