import random
import copy
import time

SUDOKU_BOARD = [
    [3, " ", " ", 4, " ", " ", 6, " ", " "],
    [7, " ", " ", " ", 9, " ", " ", " ", 3],
    [8, " ", " ", 3, " ", " ", " ", " ", " "],
    [" ", 3, " ", 5, 2, 1, " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", 9, " "],
    [" ", 2, " ", " ", 3, " ", " ", 4, " "],
    [" ", 4, 8, " ", " ", 2, " ", " ", " "],
    [" ", " ", 6, " ", " ", " ", 1, " ", " "],
    [" ", " ", " ", " ", " ", 7, 4, " ", " "],
]

VALID_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board(board):
    """
    Print sudoku board on console.
    """
    index = 0
    print("")
    for index, line in enumerate(board):
        row_string = f"{line[0]} {line[1]} {line[2]} | {line[3]} {line[4]} {line[5]} | {line[6]} {line[7]} {line[8]}"
        print(row_string)
        if (index + 1) % 3 == 0 and index != 8:
            print("-" * 6 + "+" + "-" * 7 + "+" + "-" * 6)


def used_values(sudoku_board, x, y):
    """
    Get used values.
    """

    # Get row and column used values
    used_values = []
    used_values += sudoku_board[y]
    for row in sudoku_board:
        used_values.append(row[x])

    square_index = get_square(x, y)
    used_values += get_square_values(sudoku_board, square_index)

    used_values = list(set(used_values))
    used_values.remove(" ")

    return used_values


def get_square(x, y):
    index = int(x / 3)
    index = index + int(y / 3) * 3
    return index


def get_square_values(sudoku_board, index):
    used_values = []
    if index == 0:
        used_values += sudoku_board[0][0:3]
        used_values += sudoku_board[1][0:3]
        used_values += sudoku_board[2][0:3]
    elif index == 1:
        used_values += sudoku_board[0][3:6]
        used_values += sudoku_board[1][3:6]
        used_values += sudoku_board[2][3:6]
    elif index == 2:
        used_values += sudoku_board[0][6:]
        used_values += sudoku_board[1][6:]
        used_values += sudoku_board[2][6:]
    elif index == 3:
        used_values += sudoku_board[3][0:3]
        used_values += sudoku_board[4][0:3]
        used_values += sudoku_board[5][0:3]
    elif index == 4:
        used_values += sudoku_board[3][3:6]
        used_values += sudoku_board[4][3:6]
        used_values += sudoku_board[5][3:6]
    elif index == 5:
        used_values += sudoku_board[3][6:]
        used_values += sudoku_board[4][6:]
        used_values += sudoku_board[5][6:]
    elif index == 6:
        used_values += sudoku_board[6][0:3]
        used_values += sudoku_board[7][0:3]
        used_values += sudoku_board[8][0:3]
    elif index == 7:
        used_values += sudoku_board[6][3:6]
        used_values += sudoku_board[7][3:6]
        used_values += sudoku_board[8][3:6]
    elif index == 8:
        used_values += sudoku_board[6][6:]
        used_values += sudoku_board[7][6:]
        used_values += sudoku_board[8][6:]
    return used_values


def valid_moves(used_val):
    return list(filter(lambda x: x not in used_val, VALID_VALUES))


def solved_sudoku(board):
    for x in board:
        if " " in x:
            return False
    return True


def next_empty(board):
    for index_y, row in enumerate(board):
        for index_x, value in enumerate(row):
            if value == " ":
                return index_x, index_y
    return None, None


def resolve_alg(board):
    if solved_sudoku(board):
        print_board(board)
        return True
    x, y = next_empty(board)
    if x == None:
        return True
    used_vals = used_values(board, x, y)
    valid_vals = valid_moves(used_vals)
    new_board = copy.deepcopy(board)
    result = False
    for val in valid_vals:
        new_board[y][x] = val
        result = resolve_alg(new_board)
        if result:
            return True
    return result


start = time.time()
resolve_alg(SUDOKU_BOARD)
end = time.time()
print(end - start)
