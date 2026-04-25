
import random

# creates the board
def create_board():
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

def add_random_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

def print_board(board):
    for row in board:
        print(row)
    print()

def move_row_left(row):
    # Remove zeros
    new_row = [num for num in row if num != 0]

    # Merge equal neighbors
    i = 0
    while i < len(new_row) - 1:
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
            i += 1  # skip cause we merged
        i += 1

    # Remove zeros made from merging
    new_row = [num for num in new_row if num != 0]

    
    while len(new_row) < 4:
        new_row.append(0)

    return new_row

def move_left(board):
    for r in range(4):
        board[r] = move_row_left(board[r])

def move_right(board):
    for r in range(4):
        board[r] = move_row_left(board[r][::-1])[::-1]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board[:] = transpose(board)
    for r in range(4):
        board[r] = move_row_left(board[r])
    board[:] = transpose(board)

def move_down(board):
    board[:] = transpose(board)
    for r in range(4):
        board[r] = move_row_left(board[r][::-1])[::-1]
    board[:] = transpose(board)

# loop and user inputs
board = create_board()
add_random_tile(board)
add_random_tile(board)

while True:
    print_board(board)
    move = input("press the following-- W=up A=left D=right S=down or Q to quit):").strip().lower()

    if move == "q":
        print("Thanks for playing!")
        break

    old_board = [row[:] for row in board]

    if move == "a":
        move_left(board)
    elif move == "d":
        move_right(board)
    elif move == "w":
        move_up(board)
    elif move == "s":
        move_down(board)
    else:
        print("Invalid input!")
        continue

    # Tile add ins for space when numbers combine
    if board != old_board:
        add_random_tile(board)
